"""Little logging module reimplementation for python2.2."""

class Logger:
    """Simple file logger.
    
    Supports log levels: NOLOG, DEBUG, WARNING, ERROR.
    Customizing log format is not supported.
    """

    NOLOG = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3

    SUPPORTED_LOGLEVELS = [
        NOLOG,
        DEBUG,
        WARNING,
        ERROR,
    ]

    def __init__(self, logfile):
        if isinstance(logfile, str):
            self._log = open(logfile, "w")
        else:
            self._log = logfile

        self._loglevel = self.DEBUG

    def close(self):
        self._log.close()
        
    def set_loglevel(self, level):
        if level not in self.SUPPORTED_LOGLEVELS:
            raise Exception("Loglevel %s is not supported" % (level,))

    def debug(self, fmt, *args):
        if self._loglevel < self.DEBUG:
            return

        self._message("DEBUG", fmt, *args)

    def warning(self, fmt, *args):
        if self._loglevel < self.WARNING:
            return

        self._message("WARNING", fmt, *args)

    def error(self, fmt, *args):
        if self._loglevel < self.ERROR:
            return

        self._message("ERROR", fmt, *args)

    def exception(self, fmt, *args):
        pass

    def _message(self, prefix, fmt, *args):
        self._log.write("%s: %s\n" % (prefix, fmt % args))
        self._log.flush()