import os
import sys
from contextlib import redirect_stdout

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.universe import Universe


def test_universe_help():

    file = r'tests/ref/equations.txt'

    if os.path.exists(file):
        os.remove(file)

    with open(file, 'w') as f:
        with redirect_stdout(f):
    
            universe = Universe()
            universe.help()

    assert os.path.exists(file)