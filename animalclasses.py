#!/usr/bin/env python

"""
INSTRUCTIONS:

From Terminal, run this file:

python animalclasses.py

Animals will bark or meow three times for a food they like, and only once for
the foods they don't like.

PROJECT REQUIREMENTS:
Create classes Cat, Dog, Chicken, CatFood, DogFood, HumanFood, Lemons

a cat likes CatFood, Chicken, and Milk
a dog likes DogFood, CatFood, Chicken, HumanFood
a Cat can meow and a Dog can bark (print "meow" or "bark" to STDOUT)
when an animal eats food it likes, it makes a noise three times
when an animal eats food it dislikes, it makes a noise one time

Include a driver file which requires the files, instantiates the classes,
and invokes the methods to demonstrate the functionality.
"""
from animals import *

cat = Cat()
dog = Dog()

cat.eat(CatFood())
cat.eat(Chicken())
cat.eat(DogFood())
cat.eat(Milk())
cat.eat(Lemons())

dog.eat(CatFood())
dog.eat(Chicken())
dog.eat(DogFood())
dog.eat(Milk())
dog.eat(Lemons())
