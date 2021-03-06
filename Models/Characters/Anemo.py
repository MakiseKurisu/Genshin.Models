from Models.Characters import Character

class Sucrose(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect
        
        self.health_base += 9244
        self.attack_base += 170
        self.defense_base += 703
        self.anemo_damage_bonus += 0.24
