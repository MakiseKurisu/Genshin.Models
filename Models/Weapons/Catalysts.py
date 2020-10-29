from Models.Weapons import Weapon

class SolarPearl(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(42)
        self.critical_rate += 0.3
        if enable_effect:
            self.normal_attack_bonus += 0.4
            self.elemental_skill_bonus += 0.4
            self.elemental_burst_bonus += 0.4

class MappaMare(Weapon):
    def __init__(self, enable_effect = True):
        super().__init__(44)
        self.elemental_mastery += 110
        if enable_effect:
            self.elemental_damage_bonus += 0.32