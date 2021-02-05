""" Base models for whole application """
import collections.abc


class RVprioViolation:
    def __init__(self, kernel_violation):
        self._plugin_violations = list()
        self._kernel_violation = kernel_violation

    def add_plugin_info(self, plugin):
        self._plugin_violations.append(plugin)

    def to_dict(self):
        kernel_dict = self._kernel_violation.to_dict()
        plugin_dict = {}
        for plugin in self._plugin_violations:
            if isinstance(plugin, collections.abc.Iterable):
                for plugin_values in plugin:
                    plugin_dict = {**plugin_dict, **plugin_values.to_dict()}
            else:
                plugin_dict = {**plugin_dict, **plugin.to_dict()}

        return {**kernel_dict, **plugin_dict}
