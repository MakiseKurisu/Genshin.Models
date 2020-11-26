from Models.Characters import Character

class Barbara(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect

        self.health_base += 9787
        self.attack_base += 159
        self.defense_base += 669
        self.health_bonus += 0.24

        if self.__enable_effect:
            self.hydro_damage_bonus += 0.15
