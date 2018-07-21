class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age


def dictionary(obj):
    new_dict = obj.__dict__
    for j in new_dict.keys():
        print("key=", j, "value=", new_dict[j])


def main():
    animal_1 = Animal("shark", "Edward", 5)
    dictionary(animal_1)


if __name__ == '__main__':
    main()
