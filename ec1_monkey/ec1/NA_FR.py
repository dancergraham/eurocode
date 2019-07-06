from math import log10, log

from . import Site

_document = ' +NA FR: 2008'
Site.rho = 1.225

Site.z0_by_terrain = {'O': 0.005, 'II': 0.05, 'IIIa': 0.2, 'IIIb': 0.5, 'IV': 1.}

Site.zmin_by_terrain = {'O': 1., 'II': 2., 'IIIa': 5., 'IIIb': 9., 'IV': 15.}

Site.Vb0NAFR = {1: 22., 2: 24., 3: 26., 4: 28.}

ec1_init = Site.__init__


def SiteFR_init(self, zone, terrain, co=1.0):
    vb0 = Site.Vb0NAFR[zone]
    ec1_init(self, vb0, terrain, co=1.0)
    self.document += _document


def iuFR(self, z):
    if z < self._zmin:
        z = self._zmin
    kI = 1 - 0.0002 * (log10(self._z0) + 3) ** 6
    return kI / (self._co * log(z / self._z0))


Site.__init__ = SiteFR_init
Site.iu = iuFR
