from abc import ABC, abstractmethod
from enum import Enum, auto
from factions import Faction

class GoodFaction(Enum):
    INVESTIGATOR = auto()
    GUARDIAN = auto()
    MEDIC = auto()
    PROTECTOR = auto()
    TECHNICIAN = auto()
    ANALYST = auto()
    DIPLOMAT = auto()


class GoodRole(ABC):
    """
    Abstract base class for all roles in the RL environment.
    All specific roles should inherit from this class and implement required methods.
    """

    faction = Faction.Good
    armor = None  # Placeholder for the armor this role might have

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def night_action(self, game_state, player_id):
        pass

    @abstractmethod
    def day_action(self, game_state, player_id):
        pass

class Investigator(GoodRole):
    """
    Represents the Investigator role in the game.
    The Investigator can investigate a player during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Investigator's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Investigator's day action
        pass
class Guardian(GoodRole):
    """
    Represents the Guardian role in the game.
    The Guardian can protect a player during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Guardian's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Guardian's day action
        pass
class Medic(GoodRole):
    """
    Represents the Medic role in the game.
    The Medic can heal a player during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Medic's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Medic's day action
        pass
class Protector(GoodRole):
    """
    Represents the Protector role in the game.
    The Protector can shield a player from harm during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Protector's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Protector's day action
        pass
class Technician(GoodRole):
    """
    Represents the Technician role in the game.
    The Technician can repair or enhance a player's abilities during the night phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Technician's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Technician's day action
        pass
class Analyst(GoodRole):
    """
    Represents the Analyst role in the game.
    The Analyst can analyze game state and provide insights during the day phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Analyst's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Analyst's day action
        pass
class Diplomat(GoodRole):
    """
    Represents the Diplomat role in the game.
    The Diplomat can negotiate and influence other players during the day phase.
    """

    def night_action(self, game_state, player_id):
        # Implement the logic for the Diplomat's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Diplomat's day action
        pass
if __name__ == "__main__":
    # Example usage
    investigator = Investigator("John Doe")
    print(f"Name: {investigator.name}, Faction: {investigator.faction.name}")
    # You can implement the game_state and player_id to test the night_action and day_action methods.
