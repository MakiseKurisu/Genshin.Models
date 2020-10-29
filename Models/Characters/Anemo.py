from Models.Characters import Character

class Sucrose(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect
        
        self.attack_base += 200
        self.anemo_damage_bonus += 0.3
