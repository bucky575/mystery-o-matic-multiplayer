# Location submodules are imported directly by _registry.py
# This file re-exports the public API
from mystery_o_matic.locations.locations import (
    locations,
    get_location_data,
    Locations,
    TutorialLocations,
)
