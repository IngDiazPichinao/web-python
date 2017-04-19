import yaml


def get_or_fail(data, key, override=None):
    """ Provide the value at key in :param:'data' or falls back to the provided override.
        If no override is provide it throws a KeyError. """

    if override is not None:
        return override
    else:
        try:
            value = data[key]

            if value is None:
                raise KeyError("Missing expected value at field '{0}' in config".format(key))
        except KeyError as exc:
            raise KeyError("Could not find expected file '{0}' in config".format(key)) from exc
        else:
            return value


class Config(object):

    def __init__(self, args, cfg_path="/etc/cns/cns-web-sav-yml"):
        self._config = []
        self._args   = args

        try:
            with open(cfg_path, 'r') as files:
                buff         = files.read()
                self._config = yaml.load(buff)
        except IOError as exc:
            raise IOError("Could not open config file at: '{0}'".format(cfg_path)) from exc
        except Exception as exc:
            raise Exception("Failed to load configuration") from exc

    @property
    def db(self):
        return get_or_fail(self._config, 'database')

    @property
    def user(self):
        return get_or_fail(self.db, 'user', self._args['--db-user'])

    @property
    def passwd(self):
        return get_or_fail(self.db, 'passwd', self._args['--db-passwd'])

    @property
    def host(self):
        return get_or_fail(self.db, 'host', self._args['--db-host'])

    @property
    def port(self):
        return int(get_or_fail(self.db, 'port', self._args['--db-port']))

    @property
    def bd(self):
        return get_or_fail(self.db, 'bd', self._args['--db-name'])
