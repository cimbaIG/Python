from dataclasses import dataclass, make_dataclass, field
from math import asin, cos, radians, sin, sqrt


# Dataclass is a regular Python class. The only difference is that it has basic
# data model methods like .__init__(), .__repr__() and .__eq__() which are 
# implemented for us.
@dataclass
class Position:
    
    ''' Dataclass that represent geographic positions. '''
    
    name: str
    # lon: float = 0.0
    # lat: float = 0.0
    # What if we want to customize the field to hide it in the .__repr__() ?
    # We can use repr=False parameter!
    # lon: float = field(default=0.0, metadata={'unit': 'degrees'}, repr=False)
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
    # The metadata parameter is not used by the data classes themselves but is 
    # available for you (or third party packages) to attach information to 
    # fields. In the Position example, you could for instance specify that 
    # latitude and longitude should be given in degrees!
    # The metadata (and other information about a field) can be retrieved using 
    # the .fields() function!
    
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
