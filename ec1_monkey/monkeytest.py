import ec1
from ec1 import NA_FR

# TODO: Refactor with pytest.

s = ec1.Site(2, 'II')
print(s.document)
print(s.qp(10))

t = ec1.Site(4, 'IV')
print(t.qp(50))

# NAFR
for zone, terrain, z in [(2, 'IIIb', 90),
                         (4, 'IV', 5),
                         (4, 'IV', 15),
                         (4, 'IV', 150),
                         ]:
    s = ec1.Site(zone, terrain)
    print(zone, terrain, z, s.iu(z), s.qp(z))
