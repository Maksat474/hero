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