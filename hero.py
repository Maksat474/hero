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


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_the_true_phrase(self):
        print(f"True in the True_phrase for {self.nickname}")


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_the_true_phrase(self):
        print(f"True in the True_phrase for {self.nickname}")


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_the_true_phrase(self):
        print(f"True in the True_phrase for {self.nickname}")


class Villain(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


air_hero = AirHero("Airman", "Летчик", "Летать", 100, "Небо!", 10)
earth_hero = EarthHero("Earthling", "Земляк", "Сила земли", 120, "Земля!", 15)
space_hero = SpaceHero("Spaceman", "Космонавт", "Покорение космоса", 150, "Звезды!", 20)
villain = Villain("Evil", "Злодей", "Злоба", 200, "Зло победит!", 25)

air_hero.double_health()
earth_hero.double_health()
space_hero.double_health()


air_hero.true_in_the_true_phrase()
earth_hero.true_in_the_true_phrase()
space_hero.true_in_the_true_phrase()
