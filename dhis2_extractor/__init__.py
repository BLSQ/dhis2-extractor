# init files are the perfect place to define top-level package exports
from .extractor import Dhis2Extractor

# __all__ defines the "public API" of your module
# it allows user you to import the names listed below straight from the dhis2_extractor module (other names
# won't be exported and would required a more targeted import)
__all__ = ["Dhis2Extractor"]
