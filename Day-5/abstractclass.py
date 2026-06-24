from abc import ABC

class Animal(ABC):
    def eat():
        pass

    def sleep(self):
        return "I am sleeping"

class Dog:
    a = Animal()
