from Models.Characters import Character

class Noelle(Character):
    def __init__(self, enable_effect = True):
        super().__init__()
        self.__enable_effect = enable_effect
        
        self.health_base += 12071
        self.attack_base += 191
        self.defense_base += 799
        self.defense_bonus += 0.3

    @property
    def attack(self):
        if self.__enable_effect:
            # estimated lv15 skill: https://bbs.nga.cn/read.php?tid=23915817
            return super().attack + super().defense * 1.46
        else:
            return super().attack
