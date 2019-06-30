# import numpy as np
from math import log

"""Structural wind loading according to Eurocode EN 1991-1-4:2005. 
Initial proof of concept of an OOP approach using Python. 
By Graham Knapp
"""

rho = 1.25  # density kg/m3 from base Eurocode


class Site():
	"""represents a site with a given terrain roughness and basic wind speed. 
	
	test from https://eurocodes.jrc.ec.europa.eu/doc/WS2008/SX016a-EN-EU.pdf
	
	>>> round(Site(26, 'II').qp(7.3))
	911
	"""
	z0_by_terrain = {'O': 0.003, 'I': 0.01, 'II': 0.05, 'III': 0.3, 'IV': 1.}
	
	zmin_by_terrain = {'O': 1., 'I': 1., 'II': 2., 'III': 5., 'IV': 10.}
	
	def __init__(self, vb, terrain, co = 1.0):
		self.vb = vb
		self._terrain = terrain
		self._z0 = self.z0_by_terrain[terrain]
		self._zmin = self.zmin_by_terrain[terrain]
		self._co = co
		
	def iu(self, z):
		"""Calclate turbulence intensity at a given height z
		"""
		z = max(z, self._zmin)
		return 1 / (self._co * log(z / self._z0))
		
	def cr(self, z):
		"""Calculate mean wind speed ratio at a given height z
		"""
		z = max(z, self._zmin)
		return (0.19 * ((self._z0 / 0.05))**0.07) * log(z / self._z0)
			
	def qp(self, z):
		"""Calculate peak wind velocity pressure in Pa at a given height
		"""
		U = self.cr(z) * self.vb
		_qp = 0.5 * rho * (U**2.) * (1 + 7 * self.iu(z))
		return _qp
		
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
