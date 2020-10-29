from Models import Model

class Weapon(Model):
    def __init__(self, lv1_attack):
        super().__init__()
        if lv1_attack == 41:
            self.attack_base += 475
        elif lv1_attack == 42:
            self.attack_base += 532
        elif lv1_attack == 44:
            self.attack_base += 580
        else:
            raise ValueError(f"Unknown weapon level 1 attack {lv1_attack}.")


    def __str__(self):
        return f"Weapon: {self.__class__.__name__}\n" \
               f"Attack: {self.attack}"