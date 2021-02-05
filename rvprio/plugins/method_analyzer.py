""" Analyzes source code to extract metrics from them. """

import collections

import lizard

import rvprio.models


class MethodMetadata:
    def __init__(self, nloc, ccn, token, param, mname, start_line, end_line):
        self._start_line = start_line
        self._end_line = end_line
        self._nloc = nloc
        self._ccn = ccn
        self._token = token
        self._param = param
        self._mname = mname

    def to_dict(self):
        return {
            "StartLine": self._start_line,
            "EndLine": self._end_line,
            "NLOC": self._nloc,
            "CC": self._ccn,
            "TOKEN": self._token,
            "PARAM": self._param,
        }


def get_metadata(file_, line):
    violated_method = _find_violated_function(file_, line)

    if not violated_method:
        return None

    return MethodMetadata(
        violated_method.nloc,
        violated_method.cyclomatic_complexity,
        violated_method.token_count,
        len(violated_method.parameters),
        violated_method.name,
        violated_method.start_line,
        violated_method.end_line,
    )


def _find_violated_function(file_, line):
    i = lizard.analyze_file(file_)
    violated_method = None
    for func in i.function_list:
        start_line = func.__dict__["start_line"]
        end_line = func.__dict__["end_line"]
        if line >= start_line and line <= end_line:
            violated_method = func
            break

    return violated_method
