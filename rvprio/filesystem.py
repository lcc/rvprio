""" Filesystem utilities for rvprio. """

import os
import pathlib


class Filesystem:
    def __init__(self, violations, cache_dir, dst=None):
        super().__init__()

        self._dir = os.getcwd()
        self._violations = violations
        self._dst = dst
        self._cache_dir = cache_dir

        self._found_sources = set()
        self._too_many_sources = set()

        self._sources_path_cache = dict()

    def find_sources(self):
        """Looks for present in the violations that were received and separates
        then in 3 sets: found files, not found files and too-many files."""
        IDEAL_FOUND_FILES = 1
        for violation in self._violations:
            expected_subpath = violation.get_file_subpath()
            sources = self.find_file(expected_subpath)
            n_of_sources = len(sources)

            if n_of_sources == IDEAL_FOUND_FILES:
                self._found_sources.add(violation)
                violation.full_path = str(sources[0])

            elif n_of_sources > IDEAL_FOUND_FILES:
                self._too_many_sources.add(violation)

        return self._found_sources

    def store_files(self):
        """Saves the found sources to the specified dir, if an outdir was
        not specified to the CLI, this method does nothing."""

        if not self._dst:
            return

        for violation in self._found_sources:
            full_path = violation.full_path
            dst = violation.get_file_subpath()
            dst = dst[: dst.rfind("/")]
            rvprio.finder.copy_source(full_path, self._dst)

    def find_file(self, subpath):
        source_files = list()

        if subpath in self._sources_path_cache:
            return self._sources_path_cache[subpath]

        for path in pathlib.Path(".").rglob(subpath):
            abs_path = os.path.join(self._dir, path)
            source_files.append(abs_path)

        self._sources_path_cache[subpath] = source_files

        return source_files

    def create_cache_dir(self):
        pathlib.Path(".rvprio").mkdir(parents=True, exist_ok=True)

    def _copy_source(src, dst):
        dst = os.path.join(SOURCES_DST, dst)
        if not os.path.exists(dst):
            os.makedirs(dst)

        shutil.copy2(src, dst)
