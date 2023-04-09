from dataclasses import dataclass
from typing import Any


@dataclass
class WithoutExplicitTypes:
    
    # A type hint is mandatory in data class. However, if do not want to use 
    # explicit typed, we can use typing.Any
    # Python is dynamically typed language so type hints (although mandatory) 
    # are not enforced at runtime!
    name: Any
    value: Any = 42
