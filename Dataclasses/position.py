from dataclasses import dataclass, make_dataclass


# Dataclass is a regular Python class. The only difference is that it has basic
# data model methods like .__init__(), .__repr__() and .__eq__() which are 
# implemented for us.
@dataclass
class Position:
    
    ''' Dataclass that represent geographic positions. '''
    
    name: str
    lon: float
    lat: float

# Position dataclass may be created similar to how named tuples are created.
# Position = make_dataclass("Position", ['name', 'lat', 'lon'])
