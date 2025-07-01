from abc import ABC, abstractmethod
from enum import Enum, auto

class RoleEnum(Enum):
    """
    RoleEnum is an enumeration representing the various roles agents can be.
    """
    ASSASSIN = auto()
    ANALYST = auto()
    ARBITER = auto()
    BIOHACKER = auto()
    COURIER = auto()
    CRYPTOLOGIST = auto()
    DECOY = auto()
    DIPLOMAT = auto()
    DISRUPTOR = auto()
    DOUBLE_AGENT = auto()
    ENFORCER = auto()
    ENGINEER = auto()
    FOLLOWER = auto()
    GUARDIAN = auto()
    HACKER = auto()
    INFILTRATOR = auto()
    INSIDER = auto()
    LEADER = auto()
    MASTERMIND = auto()
    MEDIC = auto()
    MESSENGER = auto()
    NEGOTIATOR = auto()
    OBSERVER = auto()
    OUTSIDER = auto()
    PROTECTOR = auto()
    SABOTEUR = auto()
    SCOUT = auto()
    SMUGGLER = auto()
    SPY = auto()
    STRATEGIST = auto()
    TECHNICIAN = auto()
    WATCHER = auto()

class AbstractRole(ABC):
    """
    Abstract base class for all roles in the RL environment.
    All specific roles should inherit from this class and implement required methods.
    """

    faction = None # Placeholder for the faction this role belongs to
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
