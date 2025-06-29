import random

class comms_factory:
    """
    Factory class for generating and validating communication actions in a multi-agent deduction environment.
    Handles communication templates, player and faction management, and action sampling.
    """

    COMMS_TEMPLATES = [
        "No Info",
        "I am {faction}",
        "I am {role}",
        "{target} is {role}",
        "{target} is {faction}",
        "I saw {target1} visit {target2}",
        "I am Voting for {target}"
    ]


    def __init__(self, player_names, factions):
        """
        Initialize the comms_factory with player names and factions.
        Args:
            player_names (list): List of player names.
            factions (list): List of faction names.
        """
        self.players = player_names
        self.player_count = len(player_names)
        self.factions = factions
        self.faction_count = len(factions)
        self.role_count = 12 #hard coding till roles are made


    def validate_comms_action(self, action):
        """
        Validate a communication action.
        Args:
            action (dict): The action to validate.
        Returns:
            bool: True if valid, False otherwise.
        """
        pass

    def print_action(self, comm_action, role=None, speaker_name=None):
        """
        Print a formatted communication action.
        Args:
            comm_action (dict): The communication action to print.
            role (str, optional): The role of the speaker.
            speaker_name (str, optional): The name of the speaker.
        """
        pass

    def get_player_name(self):
        """
        Get a random player name from the list of players.
        Returns:
            str: A player name.
        """
        pass

    def sample_action(self, policy=False):
        """
        Sample a communication action, either randomly or using a policy.
        Args:
            policy (bool): If True, sample using a policy; otherwise, sample randomly.
        Returns:
            dict: The sampled action.
        """
        if policy:
            return {}
        random_template =  random.choice(self.COMMS_TEMPLATES)
        print(random_template)

        l_faction = self.faction_count
        l_role = self.role_count
        t1 = self.player_count
        t2 = self.player_count


        if "faction" in random_template:
            l_faction = random.randrange(self.faction_count)
        if "role" in random_template:
            l_role = random.randrange(self.role_count)
        if "target" in random_template and "visit" not  in random_template:
            t1  = random.choice(self.players)
        if "target" in random_template and "visit" in random_template:
            t1  = random.choice(self.players)
            t2 = random.choice(self.players)

        template_index = self.COMMS_TEMPLATES.index(random_template)

        action = {
            "template": template_index,
            "target1": t1,
            "target2": t2,
            "label_role": l_role,
            "label_faction": l_faction,
        }
        return action




if __name__ == "__main__":
    """
    Example usage of comms_factory: creates a factory and samples an action.
    """
    commsfactory = comms_factory(["P1","P2","P3"],["faction 1","faction 2","faction 3"])

    v = commsfactory.sample_action()
