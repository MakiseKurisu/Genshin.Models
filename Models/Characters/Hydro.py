from Models.Characters import Character

class Barbara(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect

        self.attack_base += 165
        if self.__enable_effect:
            self.hydro_damage_bonus += 0.15
