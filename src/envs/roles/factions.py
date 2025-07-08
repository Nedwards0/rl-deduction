from abc import ABC, abstractmethod
from enum import Enum, auto

class Faction(Enum):
    """
    Faction is an enumeration representing the various Factions agents can be.
    """
    Evil = auto()
    Good = auto()
    Neutral = auto()

if __name__ == "__main__":
    # Example usage
    print("Available Factions:")
    for faction in Faction:
        print(f"{faction.name} ({faction.value})")
