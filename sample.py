from scipy.optimize import brute

from Models import Model
from Models.Artifacts import Artifact
from Models.Characters.Hydro import Barbara
from Models.Weapons.Catalysts import MappaMare
from Models.Artifacts.Sets import WanderersTroupe4Set

def generate_artifact(x):
    a = Artifact()

    a.attack_bonus_weight += x[0]
    a.critical_rate_weight += x[1]
    a.critical_damage_weight += x[2]
    a.elemental_damage_bonus_weight += x[3] * 8
    return a

def f(x):
    if (sum(x) + x[3] * 7) != 40:
        return 1
    a = generate_artifact(x)
    if a.is_valid() == False:
        return 1
    c = generate_character(a)
    # estimated lv10 / lv15 talent: https://bbs.nga.cn/read.php?tid=23915817
    return -1 * c.damage_expectation

def optimize():
    a = Artifact()
    ranges = (slice(0, a.max_legal_weight(3) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, a.max_legal_weight(1) + 1, 1),
              slice(0, 1 + 1, 1))
    return brute(f, ranges, finish = None)

def generate_character(a):
    return Barbara() + MappaMare() + WanderersTroupe4Set() + a

def main():
    #x = [16, 0, 0, 1]
    x = optimize()
    print(x)
    a = generate_artifact(x)
    a.is_valid(True)
    c = generate_character(a)
    print(c.damage_expectation, c.attack_bonus, c.critical_rate, c.critical_damage)

if __name__ == "__main__":
    main()