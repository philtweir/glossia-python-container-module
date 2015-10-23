import yaml

_parameters = None
_parameter_info = None


def setup(parameters):
    global _parameters, _parameter_info
    if isinstance(parameters, basestring):
        try:
            with open(parameters, 'r') as f:
                _parameter_info = yaml.safe_load(f)
                _parameters = _parameter_info.keys()
        except Exception as e:
            raise RuntimeError(
                "Go-Smart setup argument appears to be a string\n"
                "(%s)\nbut we cannot read parameters from it: %s" % (parameters, repr(e))
            )
    else:
        try:
            _parameters = parameters.keys()
            _parameter_info = parameters
        except:
            try:
                _parameters = [k for k in parameters]
                _parameter_info = {k: {} for k in parameters}
            except Exception as e:
                raise RuntimeError(
                    "Go-Smart could not understand your parameter "
                    "format for setup. Please use a filename, dict "
                    "or iterable over strings: %s" % repr(e)
                )