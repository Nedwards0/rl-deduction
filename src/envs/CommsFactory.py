import random

class CommsFactory:

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
        self.players = player_names
        self.player_count = len(player_names)
        self.factions = factions
        self.faction_count = len(factions)
        self.role_count = 12 #hard coding till roles are made


    def validate_comms_action(self, action):
        pass

    def template_to_string(self, comm_action, role=None, speaker_name=None):
        pass

    def get_player_name(self):
        pass

    def sample_action(self, policy=False):
        
        if(policy):
            pass
        else:
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
    commsfactory = CommsFactory(["P1","P2","P3"],["faction 1","faction 2","faction 3"])

    v = commsfactory.sample_action()
    print(v)
