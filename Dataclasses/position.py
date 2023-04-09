from dataclasses import dataclass, make_dataclass
from math import asin, cos, radians, sin, sqrt


# Dataclass is a regular Python class. The only difference is that it has basic
# data model methods like .__init__(), .__repr__() and .__eq__() which are 
# implemented for us.
@dataclass
class Position:
    
    ''' Dataclass that represent geographic positions. '''
    
    name: str
    lon: float = 0.0
    lat: float = 0.0
    
    # We can add methods to dataclass!
    def distance_to(self, other):
        
        r = 6371 # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        
        return 2 * r * asin(sqrt(h))

# Position dataclass may be created similar to how named tuples are created.
# Position = make_dataclass("Position", ['name', 'lat', 'lon'])
