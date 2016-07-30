#!/usr/bin/python


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s.' % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    def swat_string(self):
        print('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))


class BadCat(Animal):
    def bite(self):
        print('{0} bites you!'.format(self.name))

    def show_affection(self):
        print('{0} bites your hand!  She must like you'.format(self.name))


for a in (Dog('Casey'), BadCat('Snickers'), Dog('Penny'), Cat('KitKat')):
    a.show_affection()
