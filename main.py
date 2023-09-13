from hello import hello

class Person:
    def __init__(self, name, age, city='Moscow'):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name}: age {self.age}, city {self.city }'


mike = Person('Mike', 32)
nick = Person('Nick', 28, 'Saint-Petersburg')
print(mike)
hello(nick)
