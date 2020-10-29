from Models.Characters import Character

class Noelle(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect
        
        self.attack_base += 221
        self.defense_base += 823
        self.defense_bonus += 0.3

    @property
    def attack(self):
        if self.__enable_effect:
            return super().attack + super().defense * 1.42
        else:
            return super().attack
