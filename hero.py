class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f"Имя героя: {self.name}")

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Железный человек", "Айронмен", "Броня", 100, "Я – Железный человек!")

hero.display_name()
hero.double_health()
print(hero)
print(f"Длина коронной фразы: {len(hero)}")


class SuperHero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def increase_hp(self):
        self.hp **= 2
        self.fly = True

    def say_true(self):
        print(f"{self.name} in the True_phrase: True")


class AirHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


class EarthHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


class SpaceHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.fly = False


class Villain(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


air_hero = AirHero("Airman", 100, 10)
earth_hero = EarthHero("Earthman", 150, 15)
space_hero = SpaceHero("Spaceman", 200, 20)
villain = Villain("Evil", 100, 10)

air_hero.increase_hp()
earth_hero.increase_hp()
space_hero.increase_hp()
villain.crit()

#
print(f"{air_hero.name}'s HP: {air_hero.hp}, Fly: {air_hero.fly}")
print(f"{earth_hero.name}'s HP: {earth_hero.hp}, Fly: {earth_hero.fly}")
print(f"{space_hero.name}'s HP: {space_hero.hp}, Fly: {space_hero.fly}")
print(f"{villain.name}'s HP: {villain.hp}, People: {villain.people}, Damage: {villain.damage}")
