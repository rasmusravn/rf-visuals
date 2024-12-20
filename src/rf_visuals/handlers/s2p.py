import io
import sys

import skrf as rf


class NamedStringIO(io.StringIO):
    def __init__(self, data, name):
        super().__init__(data)
        self.name = name


def visualize_s2p(input_file: str):
    if input_file:
        ntwk = rf.Network(input_file)
    else:
        data = sys.stdin.read()
        # Create a NamedStringIO with a fake filename
        fobj = NamedStringIO(data, "stdin.s2p")
        ntwk = rf.Network(file=fobj)

    print(f"Loaded S2P file: {input_file if input_file else 'from stdin'}")
    print(ntwk)
