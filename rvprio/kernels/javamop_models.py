""" Model files and constants for the javamop kernel. """

WARNING_LABEL = "warning"
SUGGESTION_LABEL = "suggestion"
ERROR_LABEL = "error"

VIOLATION_SEVERITY_MAP = {
    "ByteArrayOutputStream_FlushBeforeRetrieve": WARNING_LABEL,
    "Byte_BadParsingArgs": WARNING_LABEL,
    "CharSequence_NotInMap": WARNING_LABEL,
    "Closeable_MeaninglessClose": SUGGESTION_LABEL,
    "Closeable_MultipleClose": SUGGESTION_LABEL,
    "Collection_UnsafeIterator": ERROR_LABEL,
    "Collections_SynchronizedCollection": ERROR_LABEL,
    "Collections_SynchronizedMap": ERROR_LABEL,
    "Comparable_CompareToNull": ERROR_LABEL,
    "Enum_NoExtraWhiteSpace": ERROR_LABEL,
    "File_LengthOnDirectory": ERROR_LABEL,
    "HttpURLConnection_SetBeforeConnect": ERROR_LABEL,
    "InetSocketAddress_Port": ERROR_LABEL,
    "InputStream_UnmarkedReset": ERROR_LABEL,
    "Iterator_HasNext": WARNING_LABEL,
    "Iterator_RemoveOnce": ERROR_LABEL,
    "ListIterator_Set": ERROR_LABEL,
    "ListIterator_hasNextPrevious": WARNING_LABEL,
    "Long_BadParsingArgs": WARNING_LABEL,
    "Map_ItselfAsValue": WARNING_LABEL,
    "Map_UnsafeIterator": ERROR_LABEL,
    "Math_ContendedRandom": SUGGESTION_LABEL,
    "Object_MonitorOwner": ERROR_LABEL,
    "OutputStream_ManipulateAfterClose": ERROR_LABEL,
    "Reader_ManipulateAfterClose": ERROR_LABEL,
    "Serializable_NoArgConstructor": ERROR_LABEL,
    "ServerSocket_Backlog": WARNING_LABEL,
    "ServerSocket_ReuseAddress": WARNING_LABEL,
    "Short_BadParsingArgs": WARNING_LABEL,
    "ShutdownHook_LateRegister": ERROR_LABEL,
    "Socket_InputStreamUnavailable": ERROR_LABEL,
    "Socket_OutputStreamUnavailable": ERROR_LABEL,
    "Socket_Timeout": ERROR_LABEL,
    "SortedSet_Comparable": ERROR_LABEL,
    "StringTokenizer_HasMoreElements": WARNING_LABEL,
    "TreeSet_Comparable": ERROR_LABEL,
    "URLConnection_Connect": WARNING_LABEL,
    "URLConnection_SetBeforeConnect": ERROR_LABEL,
    "URLDecoder_DecodeUTF8": WARNING_LABEL,
    "Collection_UnsynchronizedAddAll": ERROR_LABEL,
    "Collection_HashCode": WARNING_LABEL,
    "CharSequence_UndefinedHashCode": WARNING_LABEL,
    "Writer_ManipulateAfterClose": ERROR_LABEL,
    "CharSequence_NotInSet": WARNING_LABEL,
    "URLConnection_OverrideGetPermission": ERROR_LABEL,
    "TreeMap_Comparable": ERROR_LABEL,
    "InputStream_MarkReset": ERROR_LABEL,
    "Collections_UnnecessaryNewSetFromMap": SUGGESTION_LABEL,
    "ServerSocket_SetTimeoutBeforeBlocking": ERROR_LABEL,
    "PushbackInputStream_UnreadAheadLimit": ERROR_LABEL,
    "Comparable_CompareToNullException": ERROR_LABEL,
    "InputStream_ReadAheadLimit": ERROR_LABEL,
    "URLEncoder_EncodeUTF8": WARNING_LABEL,
}


class JavaMOPViolation:
    """Class for keeping track of an item in inventory."""

    def __init__(
        self, n_violations, spec, package, method, file_name, line, raw_violation
    ):
        self._n_violations = n_violations
        self._spec = spec
        self._set_package(package)
        self._method = method
        self._file_name = file_name
        self._severity = VIOLATION_SEVERITY_MAP[spec]
        self._line = int(line)

    def get_file_subpath(self):
        package = self.package.replace(".", "/")
        return f"{package}.java"

    def to_dict(self):
        return {
            "Filename:Line number": f"{self._package}.java:{self._line}",
            "Specification": self._spec,
            "Severity": self._severity,
            "MethodName": self._method,
        }

    @property
    def n_violations(self):
        return self._n_violations

    @property
    def spec(self):
        return self._spec

    @property
    def package(self):
        return self._package

    @property
    def method(self):
        return self._method

    @property
    def file_name(self):
        return self._file_name

    @property
    def line(self):
        return self._line

    def _set_package(self, package):
        if "$" in package:
            package = package.split("$")[0]

        self._package = package

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, violation):
        if (
            self._spec == violation.spec
            and self._package == violation.package
            and self._method == violation.method
            and self._file_name == violation.file_name
            and self._line == violation.line
        ):
            return True

        return False

    def __repr__(self):
        return f"{self._file_name}:{self._line},{self._spec},{self._severity},{self._method}"
