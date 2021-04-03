import cmd
import replclient

class Cmd(cmd.Cmd):

    prompt = "$> "

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.client = None
        self.sep = " "


    def do_connect(self, args):
        host, port = "localhost", 27450
        print "Connecting to %s:%s" % (host, port)
        self.client = replclient.connect(host, port)

    def do_shell(self, command):
        if self.client:
            self.client.sendall(command)
            print self.client.recv(1024)
        else:
            print "no remote REPL connected! Type 'connect' first."

    def do_quit(self, *args):
        print "bye!"
        if self.client:
            self.client.close()
            self.client = None

        return 1

    do_exit = do_quit
    do_q = do_quit

    def precmd(self, line):
        # print "precmd: %s" % (line,)

        return line

    def parse(self, line, *spec):
        """Parses line accoring to spec.
        
        :param line: line to parse
        :param spec: sequence of types, associated with line elements.
        
        >>> parse("localhost 27450", str, int)
        ["localhost", 27450]
        """

        parsed = line.split(self.sep)
        if len(parsed) != len(spec):
            print "Error: function requires %s arguments, got %s" % (len(spec), len(parsed))

        def _apply(pair):
            return pair[0](pair[1])

        return map(_apply, zip(spec, parsed))

    def parse_sep(self, line, sep, *spec):
        pass


def main():
    repl = Cmd()
    repl.cmdloop()

if __name__ == "__main__":
    main()