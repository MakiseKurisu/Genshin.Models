from Models.Weapons import Weapon

# Claymore base stats: https://genshin.honeyhunterworld.com/claymore/
class FavoniusGreatsword(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(41)
        self.energy_recharge += 0.613

class WhiteBlind(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(42)
        self.defense_bonus += 0.517
        if enable_effect:
            self.attack_bonus += 0.48
            self.defense_bonus += 0.48

class SerpentSpine(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(42)
        self.critical_rate += 0.276
        if enable_effect:
            self.additional_bonus += 0.5
