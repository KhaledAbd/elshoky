from django.db import models


# Create your models here.

class Maker(models.Model):
    name_maker = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    salary = models.IntegerField()
    telephone = models.IntegerField()
    pos = (('T', 'tailor'), ('E', 'engineer'), ('C', 'cutter'))
    position = models.CharField(max_length=1, choices=pos)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name_maker


class Machine(models.Model):
    machine = (
        ('Sm', 'Shima Seiki Computrized'),
        ('Sc', 'Scheller Brand Tricot '),
        ('St', 'STOLL ANVH BLM '),
        ('Kn', 'Knitting Machine'),
        ('Em', 'embroidery'),
    )
    name_machine = models.CharField(choices=machine, max_length=2)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_machine

    def price_machine(self):

        if self.name_machine == 'Sm':
            price = 100000
        elif self.name_machine == 'Sc':
            price = 200000
        elif self.name_machine == 'St':
            price = 450050
        elif self.name_machine == 'Kn':
            price = 800860
        else:
            price = 332000
        return price


class Raw(models.Model):
    type = (
        ('A', 'alpha'),
        ('S', 'Asher Ramadan'),
        ('M', 'Masrien'),
        ('G', 'Gawada'),
    )
    raw = models.CharField(max_length=1,choices=type)
    address_trade = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    machine = models.ManyToManyField(Machine)
    def __str__(self):
        return self.raw

class Model(models.Model):
    name = models.CharField(max_length=11)
    SIZE = (('sm', 'small'), ('ch', 'Chields'), ('M', 'medium'), ('gr', 'Girl'),)
    size = models.CharField(max_length=2,choices=SIZE)
    machine = models.ManyToManyField(Machine)

    def __str__(self):
        return self.name