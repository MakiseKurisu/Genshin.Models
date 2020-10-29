class Model:
    @property
    def health(self):
        return self.health_base * (1 + self.health_bonus) + self.health_constant

    @property
    def attack(self):
        return self.attack_base * (1 + self.attack_bonus) + self.attack_constant

    @property
    def defense(self):
        return self.defense_base * (1 + self.defense_bonus) + self.defense_constant

    @property
    def health_constant(self):
        return self._health_constant
    @health_constant.setter
    def health_constant(self, value):
        self._health_constant = value

    @property
    def health_bonus(self):
        return self._health_bonus
    @health_bonus.setter
    def health_bonus(self, value):
        self._health_bonus = value

    @property
    def attack_constant(self):
        return self._attack_constant
    @attack_constant.setter
    def attack_constant(self, value):
        self._attack_constant = value

    @property
    def attack_bonus(self):
        return self._attack_bonus
    @attack_bonus.setter
    def attack_bonus(self, value):
        self._attack_bonus = value

    @property
    def defense_constant(self):
        return self._defense_constant
    @defense_constant.setter
    def defense_constant(self, value):
        self._defense_constant = value

    @property
    def defense_bonus(self):
        return self._defense_bonus
    @defense_bonus.setter
    def defense_bonus(self, value):
        self._defense_bonus = value

    @property
    def elemental_mastery(self):
        return self._elemental_mastery
    @elemental_mastery.setter
    def elemental_mastery(self, value):
        self._elemental_mastery = value

    @property
    def energy_recharge(self):
        return self._energy_recharge
    @energy_recharge.setter
    def energy_recharge(self, value):
        self._energy_recharge = value

    @property
    def elemental_damage_bonus(self):
        return self._elemental_damage_bonus
    @elemental_damage_bonus.setter
    def elemental_damage_bonus(self, value):
        self._elemental_damage_bonus = value

    @property
    def physical_damage_bonus(self):
        return self._physical_damage_bonus
    @physical_damage_bonus.setter
    def physical_damage_bonus(self, value):
        self._physical_damage_bonus = value

    @property
    def critical_rate(self):
        return self._critical_rate
    @critical_rate.setter
    def critical_rate(self, value):
        if value > 1:
            self._critical_rate = 1
        else:
            self._critical_rate = value

    @property
    def critical_damage(self):
        return self._critical_damage
    @critical_damage.setter
    def critical_damage(self, value):
        self._critical_damage = value

    @property
    def healing_bonus(self):
        return self._healing_bonus
    @healing_bonus.setter
    def healing_bonus(self, value):
        self._healing_bonus = value

    @property
    def hydro_damage_bonus(self):
        return self._hydro_damage_bonus
    @hydro_damage_bonus.setter
    def hydro_damage_bonus(self, value):
        self._hydro_damage_bonus = value

    @property
    def swirl_damage_bonus(self):
        return self._swirl_damage_bonus
    @swirl_damage_bonus.setter
    def swirl_damage_bonus(self, value):
        self._swirl_damage_bonus = value

    def __init__(self):
        self.health_base = 0
        self.health_bonus = 0
        self.health_constant = 0

        self.attack_base = 0
        self.attack_bonus = 0
        self.attack_constant = 0

        self.defense_base = 0
        self.defense_bonus = 0
        self.defense_constant = 0

        self.elemental_mastery = 0

        self.critical_rate = 0
        self.critical_damage = 0
        self.healing_bonus = 0
        self.incoming_healing_bonus = 0
        self.energy_recharge = 0
        self.reduce_cooldown = 0
        self.powerful_shield = 0
        
        self.pyro_damage_bonus = 0
        self.pyro_resistance = 0
        self.hydro_damage_bonus = 0
        self.hydro_resistance = 0
        self.dendro_damage_bonus = 0
        self.dendro_resistance = 0
        self.electro_damage_bonus = 0
        self.electro_resistance = 0
        self.anemo_damage_bonus = 0
        self.anemo_resistance = 0
        self.cryo_damage_bonus = 0
        self.cryo_resistance = 0
        self.geo_damage_bonus = 0
        self.geo_resistance = 0
        self.physical_damage_bonus = 0
        self.physical_resistance = 0

        self.normal_attack_bonus = 0
        self.charged_attack_bonus = 0
        self.elemental_skill_bonus = 0
        self.elemental_burst_bonus = 0

        self.additional_bonus = 0
        self.elemental_damage_bonus = 0
        self.swirl_damage_bonus = 0

    def __add__(self, o):
        m = self.__class__()
        m.health_base = self.health_base + o.health_base
        m.health_bonus = self.health_bonus + o.health_bonus
        m.health_constant = self.health_constant + o.health_constant

        m.attack_base = self.attack_base + o.attack_base
        m.attack_bonus = self.attack_bonus + o.attack_bonus
        m.attack_constant = self.attack_constant + o.attack_constant

        m.defense_base = self.defense_base + o.defense_base
        m.defense_bonus = self.defense_bonus + o.defense_bonus
        m.defense_constant = self.defense_constant + o.defense_constant

        m.elemental_mastery = self.elemental_mastery + o.elemental_mastery

        m.critical_rate = self.critical_rate + o.critical_rate
        m.critical_damage = self.critical_damage + o.critical_damage
        m.healing_bonus = self.healing_bonus + o.healing_bonus
        m.incoming_healing_bonus = self.incoming_healing_bonus + o.incoming_healing_bonus
        m.energy_recharge = self.energy_recharge + o.energy_recharge
        m.reduce_cooldown = self.reduce_cooldown + o.reduce_cooldown
        m.powerful_shield = self.powerful_shield + o.powerful_shield
        
        m.pyro_damage_bonus = self.pyro_damage_bonus + o.pyro_damage_bonus
        m.pyro_resistance = self.pyro_resistance + o.pyro_resistance
        m.hydro_damage_bonus = self.hydro_damage_bonus + o.hydro_damage_bonus
        m.hydro_resistance = self.hydro_resistance + o.hydro_resistance
        m.dendro_damage_bonus = self.dendro_damage_bonus + o.dendro_damage_bonus
        m.dendro_resistance = self.dendro_resistance + o.dendro_resistance
        m.electro_damage_bonus = self.electro_damage_bonus + o.electro_damage_bonus
        m.electro_resistance = self.electro_resistance + o.electro_resistance
        m.anemo_damage_bonus = self.anemo_damage_bonus + o.anemo_damage_bonus
        m.anemo_resistance = self.anemo_resistance + o.anemo_resistance
        m.cryo_damage_bonus = self.cryo_damage_bonus + o.cryo_damage_bonus
        m.cryo_resistance = self.cryo_resistance + o.cryo_resistance
        m.geo_damage_bonus = self.geo_damage_bonus + o.geo_damage_bonus
        m.geo_resistance = self.geo_resistance + o.geo_resistance
        m.physical_damage_bonus = self.physical_damage_bonus + o.physical_damage_bonus
        m.physical_resistance = self.physical_resistance + o.physical_resistance

        m.normal_attack_bonus = self.normal_attack_bonus + o.normal_attack_bonus
        m.charged_attack_bonus = self.charged_attack_bonus + o.charged_attack_bonus
        m.elemental_skill_bonus = self.elemental_skill_bonus + o.elemental_skill_bonus
        m.elemental_burst_bonus = self.elemental_burst_bonus  + o.elemental_burst_bonus 

        m.additional_bonus = self.additional_bonus + o.additional_bonus
        m.elemental_damage_bonus = self.elemental_damage_bonus + o.elemental_damage_bonus
        m.swirl_damage_bonus = self.swirl_damage_bonus + o.swirl_damage_bonus
        
        return m

    def __str__(self):
        return f"Model: {self.__class__.__name__}"

    # formula: https://bbs.nga.cn/read.php?tid=23723874
    @property
    def elemental_mastery_increase_rate(self):
        return 6.665 - 9340 / (self.elemental_mastery + 1401)
    
    @property
    def elemental_mastery_damage_bonus(self):
        return self.elemental_mastery_increase_rate / 2.4

    @property
    def critical_expectation(self):
        return 1 + self.critical_rate * self.critical_damage

    def specific_damage_expectation(self, elemental_bonus, talent_bonus):
        return self.attack * self.critical_expectation * (1 + self.additional_bonus + elemental_bonus + talent_bonus)

    @property
    def damage_expectation(self):
        max_talent_bonus = max(
            self.normal_attack_bonus,
            self.charged_attack_bonus,
            self.elemental_skill_bonus,
            self.elemental_burst_bonus
            )
        
        max_elemental_bonus = max(self.physical_damage_bonus, self.elemental_damage_bonus + max(
            self.pyro_damage_bonus,
            self.hydro_damage_bonus,
            self.dendro_damage_bonus,
            self.electro_damage_bonus,
            self.anemo_damage_bonus,
            self.cryo_damage_bonus,
            self.geo_damage_bonus
            ))
        return self.specific_damage_expectation(max_talent_bonus, max_elemental_bonus)

    def elemental_reaction_damage_expectation(self, reaction_multiplier):
        return self.damage_expectation * reaction_multiplier * (1 + self.elemental_mastery_damage_bonus)
    
    # formula: https://www.reddit.com/r/Genshin_Impact/comments/j580by/elemental_mastery_damage_increase/
    def overload_base_damage(self, level):
        return 0.0000556 * level ** 4 - 0.0046801 * level ** 3 + 0.2997675 * level ** 2 + 1.0962838 * level + 26.4887857

    def electro_charged_base_damage(self, level):
        return 0.0000265 * level ** 4 - 0.0016607 * level ** 3 + 0.1205241 * level ** 2 + 1.5494266 * level + 14.6657471

    def superconduct_base_damage(self, level):
        return 0.0008476 * level ** 3 - 0.0166807 * level ** 2 + 1.5968103 * level + 3.2636734

    def swirl_base_damage(self, level):
        return 0.0009943 * level ** 3 - 0.0187566 * level ** 2 + 1.9236568 * level + 2.0633444

    @property
    def swirl_damage_expectation(self):
        return self.swirl_base_damage(90) * self.elemental_mastery_increase_rate * (1 + self.swirl_damage_bonus)