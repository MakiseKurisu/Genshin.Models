from Models.Weapons import Weapon

class FavoniusGreatsword(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(41)
        self.energy_recharge += 0.558
        if enable_effect:
            pass

class WhiteBlind(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(42)
        self.defense_bonus += 0.518
        if enable_effect:
            self.attack_bonus += 0.48
            self.defense_bonus += 0.48

class SerpentSpine(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(42)
        self.critical_rate += 0.251
        if enable_effect:
            self.additional_bonus += 0.5
