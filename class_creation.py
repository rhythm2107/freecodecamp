class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

    def smile(self):
        print("Smiling! :)")

user = Person(25, 80, 177, "Jon", "Snow", "You know nothing, Jon Snow")
user2 = Person(44, 102, 185, "Juliet", "Krosinski", "I Like coconuts")

print(user.catch_phrase, user.last_name)
user.smile()

print(user.first_name, user2.first_name)
print(user2.first_name, user2.last_name)