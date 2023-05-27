
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')
sys.path.append(r'C:\Users\cmem\onedrive_cmem\OneDrive - ENUSA Industrias Avanzadas, S.A., S.M.E\python')

from physics.drivers.body import Body


def test_body_2d():

    g = (0.0, -9.81)
    p = (0.0, 1.0)

    body = Body()

    body.set('gravity', g)
    body.set('position', p[0], axis='x')
    body.set('position', p[1], axis='y')
    body.help()

def test_body_3d():

    g = (0.0, 0.0, -9.81)
    p = (0.0, 1.0, 2.0)

    body = Body(dimensions=3)

    body.set('gravity', g)
    body.set('position', p[0], axis='x')
    body.set('position', p[1], axis='y')
    body.set('position', p[2], axis='z')
    body.help()