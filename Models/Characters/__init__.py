from Models import Model

# Character base stats: https://genshin.honeyhunterworld.com/db/char/characters/
class Character(Model):
    def __init__(self):
        super().__init__()
        self.critical_rate += 0.05
        self.critical_damage += 0.5
        self.energy_recharge += 1

    def __str__(self):
        return f"Character: {self.__class__.__name__}\n" \
               f"Health: {self.health}\n" \
               f"Attack: {self.attack}\n" \
               f"Defense: {self.defense}\n" \
               f"Critical Rate: {self.critical_rate}\n" \
               f"Critical Damage: {self.critical_damage}"