"""
Runtime Verification Prioritizer
Usage: rvprio [options]

  -h --help         Show this screen.
  -k --kernel=rv    Violations to look for [default: javamop]
  -p --project=prj  Name of the current project.
  -i --input=file   Input file.
  -o --output=file  Output file.
"""
import cerberus
import docopt
import pandas as pd
import pickle
import pathlib
import sklearn
import operator

import rvprio.filesystem
import rvprio.kernels.javamop
import rvprio.plugins.method_analyzer
import rvprio.plugins.pmd
import rvprio.validator


RVPRIO_CACHE_FOLDER = ".rvprio"
PROJECT_NAME = "Project Name"

base_header = ["Project Name", "Specification", "Filename:Line number", "MethodName"]
final_header = ['NLOC', 'CC', 'TOKEN', 'PARAM', 'AssignmentInOperand', 'BeanMembersShouldSerialize', 'CheckSkipResult', 'CloneMethodMustImplementCloneable', 'CloseResource', 'CompareObjectsWithEquals', 'DataflowAnomalyAnalysis', 'DetachedTestCase', 'DontImportSun', 'EmptyCatchBlock', 'EmptyIfStmt', 'EmptyWhileStmt', 'EqualsNull', 'IdempotentOperations', 'InstantiationToGetClass', 'InvalidSlf4jMessageFormat', 'JumbledIncrementer', 'MethodWithSameNameAsEnclosingClass', 'MisplacedNullCheck', 'MissingBreakInSwitch', 'MoreThanOneLogger', 'NonStaticInitializer', 'ProperCloneImplementation', 'SuspiciousHashcodeMethodName', 'SuspiciousOctalEscape', 'UnnecessaryCaseChange', 'UnnecessaryConversionTemporary', 'UnusedNullCheckInEquals', 'UseCorrectExceptionLogging', 'UseLocaleWithCaseConversions', 'SPEC_is_Iterator_HasNext', 'SPEC_is_ByteArrayOutputStream_FlushBeforeRetrieve', 'SPEC_is_Collections_SynchronizedCollection', 'SPEC_is_Collections_SynchronizedMap', 'SPEC_is_Closeable_MultipleClose', 'SPEC_is_Long_BadParsingArgs', 'SPEC_is_SortedSet_Comparable', 'SPEC_is_TreeSet_Comparable', 'SPEC_is_CharSequence_NotInMap', 'SPEC_is_InputStream_UnmarkedReset', 'SPEC_is_URLDecoder_DecodeUTF8', 'SPEC_is_Closeable_MeaninglessClose', 'SPEC_is_URLConnection_Connect', 'SPEC_is_Map_UnsafeIterator', 'SPEC_is_Iterator_RemoveOnce', 'SPEC_is_ListIterator_hasNextPrevious', 'SPEC_is_ListIterator_Set', 'SPEC_is_StringTokenizer_HasMoreElements', 'SPEC_is_Object_MonitorOwner', 'SPEC_is_Map_ItselfAsValue', 'SPEC_is_OutputStream_ManipulateAfterClose', 'SPEC_is_Socket_Timeout', 'SPEC_is_Socket_OutputStreamUnavailable', 'SPEC_is_HttpURLConnection_SetBeforeConnect', 'SPEC_is_Byte_BadParsingArgs', 'SPEC_is_Short_BadParsingArgs', 'SPEC_is_Reader_ManipulateAfterClose', 'SPEC_is_InputStream_ManipulateAfterClose', 'SPEC_is_CharSequence_UndefinedHashCode', 'SEVERITY_is_warning', 'SEVERITY_is_suggestion', 'SEVERITY_is_error']

def get_nonbuggy_probabilities(predict_proba, indexes):
    return [(i, predict_proba[i][0]) for i in indexes]


def prioritize_probBased_afterCV(predict_proba, indexes):
    prioritized = get_nonbuggy_probabilities(predict_proba, indexes)
    prioritized.sort(key = operator.itemgetter(1))
    prioritized = [i[0] for i in prioritized]

    return prioritized

def main(kernel, project, input, output, **kwargs):
    """ Main function for rvprio. """
    kernel = rvprio.kernels.javamop.JavaMOP(input_file=input)
    violations = kernel.get_violations()

    filesystem = rvprio.filesystem.Filesystem(violations, RVPRIO_CACHE_FOLDER, RVPRIO_CACHE_FOLDER)
    filesystem.create_cache_dir()
    found_violations = filesystem.find_sources()
    filesystem.store_files()

    file_paths = [
        str(filesystem.find_file(subpath=violation.file_name)[0])
        for violation in found_violations
    ]

    pmd = rvprio.plugins.pmd.PMDPlugin(file_paths, "pmd-out.csv", RVPRIO_CACHE_FOLDER)
    pmd.run()

    final_violations = list()
    for violation in found_violations:
        final_violation = rvprio.models.RVprioViolation(violation)

        subpath = violation.file_name
        path = str(filesystem.find_file(subpath)[0])
        line = violation.line

        metadata = rvprio.plugins.method_analyzer.get_metadata(path, line)

        if metadata:
            final_violation.add_plugin_info(metadata)
            pmd_violation = pmd.get_range_analysis(
                path, metadata.start_line, metadata._end_line
            )
            final_violation.add_plugin_info(pmd_violation)
            final_violations.append(final_violation)

    rvprio_violations = [violation.to_dict() for violation in final_violations]
    df = pd.DataFrame(rvprio_violations).fillna(0)
    df[PROJECT_NAME] = project

    final_df = pd.DataFrame(columns=final_header)
    final_df = pd.concat([df, final_df], axis=0, ignore_index=True).fillna(0)

    final_df = final_df[final_header]

    cli_path = pathlib.Path(__file__).parent.absolute()
    with open(f'{cli_path}/rvprio/rvprio_clf.pkl', 'rb') as fid:
        prioritizer = pickle.load(fid)

    x_cols = list(final_df.columns.values)

    X = final_df[x_cols].values
    y_pred = final_df.index.tolist()

    predict_proba = prioritizer.predict_proba(X)
    prioritized = prioritize_probBased_afterCV(predict_proba, y_pred)

    print(prioritized)
    df = df.reindex(prioritized)
    df = df[base_header]
    df.to_csv(output)

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__, version="beta")
    cli_validator = cerberus.Validator(rvprio.validator.CLI_SCHEMA)
    is_valid = cli_validator.validate(arguments)
    if is_valid:
        arguments = {k.strip("--"): v for (k, v) in arguments.items()}
        main(**arguments)

    else:
        print(cli_validator.errors)
