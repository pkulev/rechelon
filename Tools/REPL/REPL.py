import socket
from socket import socket as Socket, AF_INET, SOCK_DGRAM
import os.path
import sys
#import Game

import logging


#log = logging.Logger(os.path.join(Game.getPath(), "replserver.log"))
LOG = None


import threading


class REPLServer:

    def __init__(self):
        self.host = "localhost"
        self.port = 27450
        self.server = Socket(AF_INET, SOCK_DGRAM)
        self.server.bind((self.host, self.port))

        self.running = 1
        LOG.debug("Server running at %s:%s", self.host, self.port)

    def worker(self):
        while self.running:
            msg = self.server.recv(1024)
            LOG.debug("Got message: %s", msg)

            if msg == "quit":
                self.running = 0
                continue

            try:
                result = eval(msg, globals(), locals())
            except Exception, e:
                LOG.error(str(e))
                result = e
            else:
                LOG.debug("Eval result: %s", str(result))

            try:
                self.server.sendall(str(result))
            except Exception, e:
                if isinstance(result, Exception):
                    result = "Error %s happend after: %s" % (str(e), result)
                else:
                    result = str(e)
                LOG.error(result)

        LOG.debug("Stopping server...")

    def run(self):
        t = threading.Thread(target=self.worker)
        t.start()


def main(args):
    global LOG

    debug = "-d" in args or "--debug" in args
    to_stdout = "-s" in args or "--stdout" in args

    if to_stdout:
        sys.ps1 = ""
        LOG = logging.Logger(sys.stdout)
    else:
        LOG = logging.Logger("replserver.log")

    if debug:
        LOG.set_loglevel(logging.Logger.DEBUG)

    LOG.debug("Hostname: %s, python: %s", socket.gethostname(), sys.version)

    server = REPLServer()
    server.run()


if __name__ == "__main__":
    main(sys.argv)