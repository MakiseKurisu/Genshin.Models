from scipy.optimize import brute

from Models import Model
from Models.Artifacts import Artifact
from Models.Characters.Anemo import Sucrose
from Models.Weapons.Catalysts import *
from Models.Artifacts.Sets import ViridescentVenerer4Set

def generate_artifact(x):
    a = Artifact()

    a.attack_bonus_weight += x[0]
    a.critical_rate_weight += x[1]
    a.critical_damage_weight += x[2]
    a.elemental_damage_bonus_weight += x[3] * 8
    a.elemental_mastery_weight += x[4]
    return a

def f(x):
    if (sum(x) + x[3] * 7) != 69:
        return 1
    a = generate_artifact(x)
    if a.is_valid() == False:
        return 1
    c = generate_character(a)
    return -1 * sum(damage_model(c))

def optimize():
    a = Artifact()
    ranges = (slice(0, a.max_legal_weight(3) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, 1 + 1, 1),
              slice(0, a.max_legal_weight(3) + 1, 1))

    return brute(f, ranges, finish = None)

def generate_character(a):
    return Sucrose() + SacrificialFragments() + ViridescentVenerer4Set() + a

def damage_model(c):
    # estimated lv10 / lv15 talent: https://bbs.nga.cn/read.php?tid=23915817
    return ( 0.5 * (0.335 + 0.306 + 0.384 + 0.479) / 4 * 2.4 * c.damage_expectation, 2 * c.swirl_damage_expectation )

def main():
    x = [24, 21, 16, 1, 0]
    #x = optimize()
    print(x)
    a = generate_artifact(x)
    a.is_valid(True)
    c = generate_character(a)
    d = damage_model(c)
    print(sum(d), d, c.attack_bonus, c.critical_rate, c.critical_damage, c.elemental_mastery)

if __name__ == "__main__":
    main()