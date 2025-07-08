from factions import Faction
from abc import ABC, abstractmethod
from enum import Enum, auto

class NeutralFaction(Enum):
    """
    Enum representing the different neutral factions in the game.
    Each faction has a unique identifier.
    """
    MERCENARY = auto()
    BOUNTY_HUNTER = auto()
    WILDCARD = auto()

class NeutralRole(ABC):
    """
    Abstract base class for all neutral roles in the RL environment.
    All specific neutral roles should inherit from this class and implement required methods.
    """

    faction = Faction.Neutral
    armor = None  # Placeholder for the armor this role might have

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def night_action(self, game_state, player_id):
        """
        Perform the role's night action.
        Args:
            game_state: The current state of the game.
            player_id: The ID of the player performing the action.
        Returns:
            Any: The result of the night action.
        """
        pass

    @abstractmethod
    def day_action(self, game_state, player_id):
        """
        Perform the role's day action (if any).
        Args:
            game_state: The current state of the game.
            player_id: The ID of the player performing the action.
        Returns:
            Any: The result of the day action.
        """
        pass
class Mercenary(NeutralRole):
    """
    Represents the Mercenary role in the game.
    The Mercenary can perform actions for hire during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Mercenary's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Mercenary's day action
        pass
class BountyHunter(NeutralRole):
    """
    Represents the Bounty Hunter role in the game.
    The Bounty Hunter can target players for elimination during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Bounty Hunter's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Bounty Hunter's day action
        pass
class Wildcard(NeutralRole):
    """
    Represents the Wildcard role in the game.
    The Wildcard can perform unpredictable actions during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Wildcard's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Wildcard's day action
        pass

if __name__ == "__main__":
    print("Available Neutral Factions:")
    for faction in NeutralFaction:
        print(f"{faction.name} ({faction.value})")

    mercenary = Mercenary("Mercenary")
    print(f"Created role: {mercenary.name} with faction {mercenary.faction.name}")