#!/usr/bin/env python


def get_reply():
    if sys.stdin.isatty():
        return raw_input('?')
    else:
        #assert False, 'platform is not supported'
        read_value = open('/dev/tty').readline().rstrip()
        print read_value
        return read_value


def more(text, num_lines = 15):
    """
    Prints a maximum of num_lines, and ask
    user if wants to see more.

    :text: string
    :num_lines: int
    :return: None
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print line
        if lines and get_reply() not in ('y', 'Y'):
            break

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read(), 10)
