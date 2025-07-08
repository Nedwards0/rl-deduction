from abc import ABC, abstractmethod
from enum import Enum, auto
from factions import Faction

class EvilFaction(Enum):
    """
    Enum representing the different evil factions in the game.
    Each faction has a unique identifier.
    """
    ASSASSIN = auto()
    DOUBLE_AGENT = auto()
    SABOTEUR = auto()
    INFILTRATOR = auto()
    SPY = auto()
    MASTERMIND = auto()
    DISRUPTOR = auto()



class EvilRole(ABC):
    """
    Abstract base class for all roles in the RL environment.
    All specific roles should inherit from this class and implement required methods.
    """

    faction = Faction.Evil
    armor = None # Placeholder for the armor this role might have


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

class Assassin(EvilRole):
    """
    Represents the Assassin role in the game.
    The Assassin can eliminate a player during the night phase.
    """
    faction = EvilFaction.ASSASSIN

    def night_action(self, game_state, player_id):
        # Implement the logic for the Assassin's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Assassin's day action
        pass

class DoubleAgent(EvilRole):
    """
    Represents the Double Agent role in the game.
    The Double Agent can perform actions that benefit the evil faction while appearing to be a good player.
    """
    faction = EvilFaction.DOUBLE_AGENT

    def night_action(self, game_state, player_id):
        # Implement the logic for the Double Agent's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Double Agent's day action
        pass

class Saboteur(EvilRole):
    """
    Represents the Saboteur role in the game.
    The Saboteur can disrupt the plans of the good players.
    """
    faction = EvilFaction.SABOTEUR

    def night_action(self, game_state, player_id):
        # Implement the logic for the Saboteur's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Saboteur's day action
        pass

class Infiltrator(EvilRole):
    """
    Represents the Infiltrator role in the game.
    The Infiltrator can gather information and perform actions that benefit the evil faction.
    """
    faction = EvilFaction.INFILTRATOR

    def night_action(self, game_state, player_id):
        # Implement the logic for the Infiltrator's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Infiltrator's day action
        pass

class Spy(EvilRole):
    """
    Represents the Spy role in the game.
    The Spy can gather information about other players and their actions.
    """
    faction = EvilFaction.SPY

    def night_action(self, game_state, player_id):
        # Implement the logic for the Spy's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Spy's day action
        pass

class Mastermind(EvilRole):
    """
    Represents the Mastermind role in the game.
    The Mastermind can orchestrate complex plans and manipulate other players.
    """
    faction = EvilFaction.MASTERMIND

    def night_action(self, game_state, player_id):
        # Implement the logic for the Mastermind's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Mastermind's day action
        pass

class Disruptor(EvilRole):

    """
    Represents the Disruptor role in the game.
    The Disruptor can interfere with the actions of other players, causing chaos.
    """
    faction = EvilFaction.DISRUPTOR

    def night_action(self, game_state, player_id):
        # Implement the logic for the Disruptor's night action
        pass

    def day_action(self, game_state, player_id):
        # Implement the logic for the Disruptor's day action
        pass

if __name__ == "__main__":
    # Example usage of the EvilRole classes
    assassin = Assassin("Assassin")
    print(f"Role: {assassin.name}, Faction: {assassin.faction.name}", f"Faction ID: {assassin.faction.value}")

    double_agent = DoubleAgent("Double Agent")
    print(f"Role: {double_agent.name}, Faction: {double_agent.faction.name}")
