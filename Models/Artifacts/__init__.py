import numpy
from Models import Model

class Artifact(Model):
    @property
    def health_constant(self):
        return self.weight_to_value((209, 239, 269, 299), self.health_constant_weight) + 4780
    @health_constant.setter
    def health_constant(self, value):
        pass

    @property
    def health_bonus(self):
        return self.weight_to_value((0.041, 0.047, 0.053, 0.058), self.health_bonus_weight)
    @health_bonus.setter
    def health_bonus(self, value):
        pass

    @property
    def attack_constant(self):
        return self.weight_to_value((14, 16, 18, 19), self.attack_constant_weight) + 311
    @attack_constant.setter
    def attack_constant(self, value):
        pass

    @property
    def attack_bonus(self):
        return self.weight_to_value((0.041, 0.047, 0.053, 0.058), self.attack_bonus_weight)
    @attack_bonus.setter
    def attack_bonus(self, value):
        pass

    @property
    def defense_constant(self):
        return self.weight_to_value((16, 19, 21, 23), self.defense_constant_weight)
    @defense_constant.setter
    def defense_constant(self, value):
        pass

    @property
    def defense_bonus(self):
        return self.weight_to_value((0.051, 0.058, 0.066, 0.073), self.defense_bonus_weight)
    @defense_bonus.setter
    def defense_bonus(self, value):
        pass

    @property
    def elemental_mastery(self):
        return self.weight_to_value((16, 19, 21, 23), self.elemental_mastery_weight)
    @elemental_mastery.setter
    def elemental_mastery(self, value):
        pass

    @property
    def energy_recharge(self):
        return self.weight_to_value((0.045, 0.052, 0.058, 0.065), self.energy_recharge_weight)
    @energy_recharge.setter
    def energy_recharge(self, value):
        pass

    @property
    def elemental_damage_bonus(self):
        if self.elemental_damage_bonus_weight == 8:
            return 0.466
        elif self.elemental_damage_bonus_weight == 0:
            return 0
        else:
            raise ValueError(f"Invalid elemental_damage_bonus_weight, expects 0 or 8, get {self.elemental_damage_bonus_weight}")
    @elemental_damage_bonus.setter
    def elemental_damage_bonus(self, value):
        pass

    @property
    def physical_damage_bonus(self):
        if self.physical_damage_bonus_weight == 8:
            return 0.583
        elif self.physical_damage_bonus_weight == 0:
            return 0
        else:
            raise ValueError(f"Invalid physical_damage_bonus_weight, expected 0 or 8, get {self.physical_damage_bonus_weight}")
    @physical_damage_bonus.setter
    def physical_damage_bonus(self, value):
        pass

    @property
    def critical_rate(self):
        value = self.weight_to_value((0.027, 0.031, 0.035, 0.039), self.critical_rate_weight)
        if value > 1:
            return 1
        else:
            return value
    @critical_rate.setter
    def critical_rate(self, value):
        pass

    @property
    def critical_damage(self):
        return self.weight_to_value((0.054, 0.062, 0.07, 0.078), self.critical_damage_weight)
    @critical_damage.setter
    def critical_damage(self, value):
        pass

    @property
    def healing_bonus(self):
        if self.healing_bonus_weight == 8:
            return 0.359
        elif self.healing_bonus_weight == 0:
            return 0
        else:
            raise ValueError(f"Invalid healing_bonus_weight, expected 0 or 8, get {self.healing_bonus_weight}")
    @healing_bonus.setter
    def healing_bonus(self, value):
        pass

    def __init__(self, x0 = (0,) * 13, growth_rate = 3, max_total_weight = None):
        super().__init__()
        self.growth_rate = growth_rate
        if max_total_weight is None:
            self.max_total_weight = self.max_legal_total_weight()
        else:
            self.max_total_weight = max_total_weight
        self.from_tuple(x0)
    
    def __str__(self):
        return f"Artifact: {self.__class__.__name__}"
        
    def from_tuple(self, x0):
        self.health_constant_weight = x0[0]
        self.health_bonus_weight = x0[1]
        self.attack_constant_weight = x0[2]
        self.attack_bonus_weight = x0[3]
        self.defense_constant_weight = x0[4]
        self.defense_bonus_weight = x0[5]
        self.elemental_mastery_weight = x0[6]
        self.energy_recharge_weight = x0[7]
        self.elemental_damage_bonus_weight = x0[8]
        self.physical_damage_bonus_weight = x0[9]
        self.critical_rate_weight = x0[10]
        self.critical_damage_weight = x0[11]
        self.healing_bonus_weight = x0[12]

    def to_tuple(self):
        return (
            self.health_constant_weight,
            self.health_bonus_weight,
            self.attack_constant_weight,
            self.attack_bonus_weight,
            self.defense_constant_weight,
            self.defense_bonus_weight,
            self.elemental_mastery_weight,
            self.energy_recharge_weight,
            self.elemental_damage_bonus_weight,
            self.physical_damage_bonus_weight,
            self.critical_rate_weight,
            self.critical_damage_weight,
            self.healing_bonus_weight,
        )
    
    def weight_to_value(self, x, weight):
        return x[self.growth_rate] * weight

    def adjusted_max_weight(self, local_max):
        m = local_max - (self.max_legal_total_weight() - self.max_total_weight)
        if m < 0:
            m = 0
        return m
        
    def main_stat_weight(self):
        return (11, 10, 9, 8)[self.growth_rate]
    
    def max_legal_total_weight(self):
        return self.main_stat_weight() * 3 + 9 * 5

    def max_legal_weight(self, main_count = 0):
        return self.adjusted_max_weight(self.main_stat_weight() * main_count + 6 * (5 - main_count))

    def is_valid(self, print_reason = False):
            if sum(self.to_tuple()) > self.max_legal_total_weight():
                return False
            if sum(self.to_tuple()) > self.max_total_weight:
                if print_reason:
                    print(f"The sum of all weights {sum(self.to_tuple())} cannot be greater than {self.max_total_weight}.")
                return False
            elif self.health_bonus_weight > self.max_legal_weight(3) or \
                 self.attack_bonus_weight > self.max_legal_weight(3) or \
                 self.defense_bonus_weight > self.max_legal_weight(3) or \
                 self.elemental_mastery_weight > self.max_legal_weight(3):
                if print_reason:
                    print(f"is_valid:1")
                return False
            elif self.energy_recharge_weight > self.max_legal_weight(1) or \
                 self.critical_rate_weight > self.max_legal_weight(1) or \
                 self.critical_damage_weight > self.max_legal_weight(1):
                if print_reason:
                    print(f"is_valid:2")
                return False
            elif self.health_constant_weight > self.max_legal_weight() or \
                 self.attack_constant_weight > self.max_legal_weight() or \
                 self.defense_constant_weight > self.max_legal_weight():
                if print_reason:
                    print(f"is_valid:3")
                return False
            elif self.elemental_damage_bonus_weight not in (0, self.main_stat_weight()) or \
                 self.physical_damage_bonus_weight not in (0, self.main_stat_weight()) or \
                 self.healing_bonus_weight not in (0, self.main_stat_weight()):
                if print_reason:
                    print(f"is_valid:4")
                return False
            elif self.elemental_damage_bonus_weight + self.physical_damage_bonus_weight not in (0, self.main_stat_weight()):
                if print_reason:
                    print(f"Artifact set can only have either Elemental Damage Bonus ({self.elemental_damage_bonus_weight}) or Physical Damage Bonus ({self.physical_damage_bonus_weight}) as main stats.")
                return False
            elif self.critical_rate_weight + self.critical_damage_weight > self.adjusted_max_weight(37):
                if print_reason:
                    print(f"When choosing Critical Rate ({self.critical_rate_weight}) or Critical Damage ({self.critical_damage_weight}) as the main stats, the overall weight cannot be greater than {self.adjusted_max_weight(37)}.")
                return False
            elif self.critical_rate_weight + self.critical_damage_weight + self.healing_bonus_weight > self.adjusted_max_weight(38):
                if print_reason:
                    print(f"When choosing Healing Bonus ({self.healing_bonus_weight}) as the main stats, the weight combined with Critical Rate ({self.critical_rate_weight}) and Critical Damage ({self.critical_damage_weight}) cannot be greater than {self.adjusted_max_weight(38)}.")
                return False
            elif self.health_bonus_weight + self.attack_bonus_weight + self.defense_bonus_weight + self.elemental_mastery_weight > self.adjusted_max_weight(51):
                if print_reason:
                    print(f"is_valid:5")
                return False
            elif sum(1 for i in (self.health_bonus_weight, self.attack_bonus_weight, self.defense_bonus_weight, self.elemental_mastery_weight, \
                 self.energy_recharge_weight, \
                 self.elemental_damage_bonus_weight, self.physical_damage_bonus_weight, \
                 self.critical_rate_weight, self.critical_damage_weight, self.healing_bonus_weight) if i >= 8) < 3:
                if print_reason:
                    print(f"is_valid:6")
                return False
            else:
                return True
