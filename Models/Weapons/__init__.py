from Models import Model

class Weapon(Model):
    def __init__(self, lv1_attack):
        super().__init__()
        if lv1_attack == 41:
            # estimated
            self.attack_base += 470
        elif lv1_attack == 42:
            # unverified
            # https://bbs.nga.cn/read.php?tid=24038793
            self.attack_base += 510
        elif lv1_attack == 44:
            # unverified
            # https://bbs.nga.cn/read.php?tid=24038793
            self.attack_base += 565
        elif lv1_attack == 46:
            # verified
            # energy_recharge 0.12->0.551
            self.attack_base += 608
        elif lv1_attack == 48:
            # unverified
            # https://bbs.nga.cn/read.php?tid=24038793
            self.attack_base += 674
        else:
            raise ValueError(f"Unknown weapon level 1 attack {lv1_attack}.")


    def __str__(self):
        return f"Weapon: {self.__class__.__name__}\n" \
               f"Attack: {self.attack}"