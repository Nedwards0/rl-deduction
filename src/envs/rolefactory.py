class RoleFactory:
    """
    Factory class for creating and managing roles for a RL environment.
    Provides methods to retrieve role information and instantiate role objects.
    """

    def __init__(self, roles):
        """
        Initialize the RoleFactory with a list of role names
        Args:
            roles (list): List of role names to use in the environment.
        """
        self.roles = list(roles)
        self.role_to_index = {role: idx for idx, role in enumerate(self.roles)}
        self.index_to_role = {idx: role for idx, role in enumerate(self.roles)}

    def create_role(self, role_name):
        """
        Create a role object (as a dictionary for now) for the given role name

        Args:
            role_name (str): The name of the role to create.
        Returns:
            dict: A dictionary representing the role, or None if not found.
        """

        #TODO: Replace with actual role instantiation logic using roles.py
        if role_name in self.roles:
            return {"name": role_name}
        return None

    def sample_role(self):
        """
        Randomly sample a role from the available roles.
        Returns:
            str: The name of the sampled role.
        """
        import random
        return random.choice(self.roles)

    def role_to_idx(self, role_name):
        """
        Convert a role name to its RL-friendly index.
        Args:
            role_name (str): The name of the role.
        Returns:
            int: The index of the role, or None if not found.
        """
        return self.role_to_index.get(role_name, None)

    def idx_to_role(self, idx):
        """
        Convert an index to its corresponding role name.
        Args:
            idx (int): The index of the role.
        Returns:
            str: The role name, or None if not found.
        """
        return self.index_to_role.get(idx, None)

    def num_roles(self):
        """
        Get the total number of roles (for RL action/state spaces).
        Returns:
            int: Number of roles.
        """
        return len(self.roles)

if __name__ == "__main__":
    # Example roles for testing
    roles = [
        "Analyst", "Arbiter", "Biohacker", "Courier", "Cryptologist"
    ]
    factory = RoleFactory(roles)

    print("All roles:", factory.roles)
    print("Number of roles:", factory.num_roles())

    # Test sampling
    print("Sampled role:", factory.sample_role())

    # Test create_role
    print("Create role 'Analyst':", factory.create_role("Analyst"))
    print("Create role 'Nonexistent':", factory.create_role("Nonexistent"))
