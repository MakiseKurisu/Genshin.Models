from scipy.optimize import brute

from Models import Model
from Models.Characters.Anemo import Sucrose
from Models.Weapons.Catalysts import SolarPearl, MappaMare
from Models.Artifacts import Artifact
from Models.Artifacts.Sets import ViridescentVenerer4Set

def generate_artifact(x):
    a = Artifact()
    c = 3 - x[1] - x[4]
    if c > 0:
        a.attack_constant_weight += c

    a.attack_bonus_weight += x[0]
    a.elemental_mastery_weight += x[1]
    a.critical_rate_weight += x[2]
    a.critical_damage_weight += x[3]
    a.elemental_damage_bonus_weight += x[4] * 8
    return a

def f(x):
    a = generate_artifact(x)
    if a.is_valid() == False:
        return 1
    c = generate_character(a)
    # estimated lv10 / lv15 talent: https://bbs.nga.cn/read.php?tid=23915817
    return -1 * (
        c.specific_damage_expectation(c.anemo_damage_bonus + c.elemental_damage_bonus, c.charged_attack_bonus) * 1.2 * 1.8 + \
        #c.specific_damage_expectation(c.anemo_damage_bonus + c.elemental_damage_bonus, c.elemental_skill_bonus) * 2.11 * 2.4 + \
        #c.specific_damage_expectation(c.anemo_damage_bonus + c.elemental_damage_bonus, c.elemental_burst_bonus) * 1.48 * 2.4 * 4 + \
        c.swirl_damage_expectation * 5
        )

def optimize():
    a = Artifact()
    ranges = (slice(0, a.max_legal_weight(3) + 1, 1),
              slice(0, a.max_legal_weight(3) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, 1 + 1, 1))
    return brute(f, ranges, finish = None)

def generate_character(a):
    return Sucrose() + ViridescentVenerer4Set() + MappaMare() + a

def main():
    #x = [0, 15, 14, 16]
    x = optimize()
    print(x)
    a = generate_artifact(x)
    c = generate_character(a)
    print(-1 * f(x), c.attack, c.elemental_mastery, c.critical_rate, c.critical_damage)

if __name__ == "__main__":
    main()