import collections
import os.path
import subprocess

import pandas

import rvprio.models


class PMDPlugin:

    _HEADER_PROBLEM_LABEL = "Problem"
    _HEADER_FILE_LABEL = "File"
    _HEADER_PACKAGE_LABEL = "Package"
    _HEADER_LINE_LABEL = "Line"
    _HEADER_PRIORITY = "Priority"
    _HEADER_DESCRIPTION_LABEL = "Description"
    _HEADER_RULE_SET_LABEL = "Rule set"
    _HEADER_RULE_LABEL = "Rule"

    def __init__(self, files, output_file, dst_dir):
        self._output_file = os.path.join(dst_dir, output_file)
        self._cache_file = f"{dst_dir}/pmd.cache"
        self._out_file = f"{dst_dir}/{output_file}"
        self._files = files
        self._violations = collections.defaultdict(list)

    def run(self):
        self._run_pmd()
        self._load_pmd_violations()

    def get_range_analysis(self, file_, start_line, stop_line):
        file_violations = self._violations[file_]
        return [
            violation
            for violation in file_violations
            if violation.line >= start_line and violation.line <= stop_line
        ]

    def _load_pmd_violations(self):
        pmd_df = self._load_dataframe()

        for index, row in pmd_df.iterrows():
            problem = row[self._HEADER_PROBLEM_LABEL]
            package = row[self._HEADER_PACKAGE_LABEL]
            file_ = row[self._HEADER_FILE_LABEL]
            priority = row[self._HEADER_PRIORITY]
            line = row[self._HEADER_LINE_LABEL]
            description = row[self._HEADER_DESCRIPTION_LABEL]
            rule_set = row[self._HEADER_RULE_SET_LABEL]
            rule = row[self._HEADER_RULE_LABEL]

            violation = PMDViolation(
                problem, package, file_, priority, line, description, rule_set, rule
            )
            curr_key = f"{file_}"
            self._violations[curr_key].append(violation)

    def _load_dataframe(self):
        return pandas.read_csv(self._output_file)

    def _run_pmd(self):
        file_list = ",".join(self._files)
        pmd_command = f"pmd -cache {self._cache_file} -R rulesets/internal/all-java.xml -d {file_list} -l java -f csv -r {self._out_file}"
        process = subprocess.Popen(pmd_command, stdout=subprocess.PIPE, shell=True)
        process.communicate()


class PMDViolation:
    def __init__(
        self, problem, package, file_, priority, line, description, rule_set, rule
    ):
        self._problem = problem
        self._package = package
        self._file_ = file_
        self._priority = priority
        self._line = line
        self._description = description
        self._rule_set = rule_set
        self._rule = rule

    def to_dict(self):
        return {self._rule: 1}

    @property
    def problem(self):
        return self._problem

    @property
    def package(self):
        return self._package

    @property
    def file_(self):
        return self._file_

    @property
    def priority(self):
        return self._priority

    @property
    def line(self):
        return self._line

    @property
    def description(self):
        return self._description

    @property
    def rule_set(self):
        return self._rule_set

    @property
    def rule(self):
        return self._rule

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f"{self._problem},{self._package},{self._file_},{self._priority},{self._line},{self._description},{self._rule_set},{self._rule}"
