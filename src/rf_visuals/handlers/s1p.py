import io
import sys

import skrf as rf


class NamedStringIO(io.StringIO):
    def __init__(self, data, name):
        super().__init__(data)
        self.name = name


def visualize_s1p(input_file: str):
    # If no input_file is provided, read from stdin
    if input_file:
        ntwk = rf.Network(input_file)
    else:
        data = sys.stdin.read()
        fobj = NamedStringIO(data, "stdin.s1p")
        ntwk = rf.Network(file=fobj)
    return ntwk
