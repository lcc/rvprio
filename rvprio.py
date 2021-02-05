"""
Runtime Verification Priorizator
Usage: rvprio [options]

  -h --help         Show this screen.
  -k --kernel=rv    Violations to look for [default: javamop]
  -i --input=file   Input file.
"""
import cerberus
import docopt

import rvprio.filesystem
import rvprio.kernels.javamop
import rvprio.plugins.method_analyzer
import rvprio.plugins.pmd
import rvprio.validator


RVPRIO_CACHE_FOLDER = ".rvprio"


def main(kernel, input, **kwargs):
    """ Main function for rvprio. """
    kernel = rvprio.kernels.javamop.JavaMOP(input_file=input)
    violations = kernel.get_violations()

    filesystem = rvprio.filesystem.Filesystem(violations, RVPRIO_CACHE_FOLDER)
    filesystem.create_cache_dir()
    found_violations = filesystem.find_sources()

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


if __name__ == "__main__":
    arguments = docopt.docopt(__doc__, version="beta")
    cli_validator = cerberus.Validator(rvprio.validator.CLI_SCHEMA)
    is_valid = cli_validator.validate(arguments)
    if is_valid:
        arguments = {k.strip("--"): v for (k, v) in arguments.items()}
        main(**arguments)
