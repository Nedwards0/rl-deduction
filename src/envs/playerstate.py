class PlayerSate:
    def __init__(self, player_id: int, role,  faction):
        self.player_id = player_id
        self.role = role
        self.faction = faction

        self.is_alive = True
        self.has_voted = False
        self.has_used_night_action = False
        self.has_used_day_action = False
        self.vote_target = None
        self.night_action_target = None
        self.day_action_target = None

        self.chat_history = []

        self.claimed_role = None
        self.claimed_faction = None

        # Role specific attributes
        #TODO

    def night_reset(self):
        pass

    def apply_status_effect(self, effect):
        """
        Apply a status effect to the player.
        Args:
            effect: The status effect to apply.
        """
        # Implement logic to apply the effect
        pass
    def remove_status_effect(self, effect):
        """
        Remove a status effect from the player.
        Args:
            effect: The status effect to remove.
        """
        # Implement logic to remove the effect
        pass
    def add_chat_message(self, message):
        """
        Add a chat message to the player's chat history.
        Args:
            message (str): The chat message to add.
        """
        self.chat_history.append(message)
    def __repr__(self):
        return f"<PlayerSate(player_id={self.player_id}, role={self.role}, faction={self.faction}, is_alive={self.is_alive})>"
    def mark_dead(self):
        """
        Mark the player as dead.
        """
        self.is_alive = False
        self.vote_target = None
        self.chat_history.clear()


if __name__ == "__main__":
    # Example usage
    player = PlayerSate(player_id=1, role="FakeRole", faction="Evil")
    player.add_chat_message("Test message")
    player.night_reset()
    player.apply_status_effect("poisoned")
    player.remove_status_effect("poisoned")
    player.mark_dead()
    print(player)