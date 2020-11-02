from scipy.optimize import brute

from Models import Model
from Models.Characters import Character
from Models.Artifacts import Artifact

def generate_artifact(x):
    a = Artifact()

    a.attack_bonus_weight += x[0]
    a.critical_rate_weight += x[1]
    a.critical_damage_weight += x[2]
    return a

def f(x):
    if sum(x) != 39:
        return 1
    a = generate_artifact(x)
    #if a.is_valid() == False:
        #return 1
    c = generate_character(a)
    # estimated lv10 / lv15 talent: https://bbs.nga.cn/read.php?tid=23915817
    return -1 * (1 + c.attack_bonus) * (1 + c.critical_rate * c.critical_damage)

def optimize():
    a = Artifact()
    ranges = (slice(0, a.max_legal_weight(3) + 10, 1),
              slice(0, a.max_legal_weight(1) + 10, 1),
              slice(0, a.max_legal_weight(1) + 10, 1))
    return brute(f, ranges, finish = None)

def generate_character(a):
    c = Character() + a
    c.attack_base += 500
    return c

def main():
    #x = [4, 20, 15]
    x = optimize()
    print(x)
    a = generate_artifact(x)
    a.is_valid(True)
    c = generate_character(a)
    print((1 + c.attack_bonus) * (1 + c.critical_rate * c.critical_damage), c.attack_bonus, c.critical_rate, c.critical_damage)

if __name__ == "__main__":
    main()