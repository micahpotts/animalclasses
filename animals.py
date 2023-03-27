"""
PROJECT REQUIREMENTS:
Create classes Cat, Dog, Chicken, CatFood, DogFood, HumanFood, Lemons

a cat likes CatFood, Chicken, and Milk
a dog likes DogFood, CatFood, Chicken, HumanFood
a Cat can meow and a Dog can bark (print "meow" or "bark" to STDOUT)
when an animal eats food it likes, it makes a noise three times
when an animal eats food it dislikes, it makes a noise one time
"""


class Cat:
    """ A cat likes CatFood, Chicken, and Milk """

    def __init__(self):
        pass

    def meow_like(self):
        print("meow, meow, meow")

    def meow_dislike(self):
        print("meow")

    def eat(self, food):
        if food.is_liked_by(self):
            self.meow_like()
        else:
            self.meow_dislike()


class Dog:
    """ A dog likes DogFood, CatFood, Chicken, HumanFood """

    def __init__(self):
        pass

    def bark_like(self):
        print("bark, bark, bark")

    def bark_dislike(self):
        print("bark")

    def eat(self, food):
        if food.is_liked_by(self):
            self.bark_like()
        else:
            self.bark_dislike()


class Chicken:
    """ Liked by cats and dogs """

    def is_liked_by(self, animal):
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            return True
        return False


class CatFood:
    """ Liked by cats and dogs """

    def is_liked_by(self, animal):
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            return True
        return False


class DogFood:
    """ Liked by dogs """

    def is_liked_by(self, animal):
        if isinstance(animal, Dog):
            return True
        return False


class HumanFood:
    """ Liked by dogs """

    def is_liked_by(self, animal):
        if isinstance(animal, Dog):
            return True
        return False


class Lemons:
    """ Liked by no one """

    def is_liked_by(self, _animal):
        return False


class Milk:
    """ Liked by cats """

    def is_liked_by(self, animal):
        if isinstance(animal, Cat):
            return True
        return False
