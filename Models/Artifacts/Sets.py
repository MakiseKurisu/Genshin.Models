from Models import Model

class GladiatorsFinale2Set(Model):
    def __init__(self):
        super().__init__()
        self.attack_bonus += 0.18

class GladiatorsFinale4Set(GladiatorsFinale2Set):
    def __init__(self):
        super().__init__()
        self.normal_attack_bonus += 0.35

class WanderersTroupe2Set(Model):
    def __init__(self):
        super().__init__()
        self.elemental_mastery += 80

class WanderersTroupe4Set(WanderersTroupe2Set):
    def __init__(self):
        super().__init__()
        self.charged_attack_bonus += 0.35

class ViridescentVenerer2Set(Model):
    def __init__(self):
        super().__init__()
        self.anemo_damage_bonus += 0.15

class ViridescentVenerer4Set(ViridescentVenerer2Set):
    def __init__(self):
        super().__init__()
        self.swirl_damage_bonus += 0.6
