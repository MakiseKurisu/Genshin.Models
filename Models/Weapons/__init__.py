from Models import Model

class Weapon(Model):
    def __init__(self, lv1_attack):
        super().__init__()
        if lv1_attack == 23:
            self.attack_base += 185
        elif lv1_attack == 33:
            self.attack_base += 243
        elif lv1_attack == 38:
            self.attack_base += 354
        elif lv1_attack == 39:
            self.attack_base += 401
        elif lv1_attack == 40:
            self.attack_base += 448
        elif lv1_attack == 41:
            self.attack_base += 454
        elif lv1_attack == 42:
            self.attack_base += 510
        elif lv1_attack == 44:
            self.attack_base += 565
        elif lv1_attack == 46:
            self.attack_base += 608
        elif lv1_attack == 48:
            self.attack_base += 674
        else:
            raise ValueError(f"Unknown weapon level 1 attack {lv1_attack}.")


    def __str__(self):
        return f"Weapon: {self.__class__.__name__}\n" \
               f"Attack: {self.attack}"