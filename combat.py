"""

"""

import tbc


def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 15
    hero.hitChance = 40
    hero.maxDamage = 7
    hero.armor = 2

    villian = tbc.Character()
    villian.name = "Villian"
    villian.hitPoints = 25
    villian.hitChance = 30
    villian.maxDamage = 6
    villian.armor = 1

    hero.printStats()
    villian.printStats()

    tbc.fight(hero, villian)

if __name__ == "__main__":
    main()