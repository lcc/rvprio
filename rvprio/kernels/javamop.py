""" Implementations related to the javamop kernel. """

import re

import rvprio.kernels.javamop_models


class JavaMOP:

    _READ_ONLY_MODE = "r"
    _N_VIOLATIONS_REGEX = "[0-9]*"
    _SPECIFICATION_REGEX = "[A-Za-z0-9_]*"
    _JAVA_FILE_REGEX = "[A-Za-z0-9\.]*"
    _FILE_PATH_REGEX = "[A-Za-z0-9\.\>\<\$]*"
    _METHOD_NAME_REGEX = "[A-Za-z0-9\_\.\>\<$]*"
    _LINE_NUMBER_REGEX = "[0-9]*"
    _MATCH_EXPRESSION = f"({_N_VIOLATIONS_REGEX})\s?Specification ({_SPECIFICATION_REGEX}) has been violated on line \[({_FILE_PATH_REGEX}){_METHOD_NAME_REGEX}\.({_METHOD_NAME_REGEX})\(({_JAVA_FILE_REGEX})\:({_LINE_NUMBER_REGEX}).*"

    def __init__(self, input_file, directory="."):
        super().__init__()
        self.directory = directory
        self._input_file = input_file

        self._violations = set()

    def get_violations(self):
        violations = set()
        with open(self._input_file, self._READ_ONLY_MODE) as violation_file:
            for violation in violation_file:
                curr_vio = self._parse_violation(violation)

                if curr_vio:
                    violations.add(curr_vio)

        return violations

    def _parse_violation(self, violation):
        re_match = re.findall(self._MATCH_EXPRESSION, violation)

        if re_match:
            re_match = re_match[0]
        else:
            return None

        return rvprio.kernels.javamop_models.JavaMOPViolation(*re_match, violation)
