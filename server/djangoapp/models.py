from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=200)
    
    def __str__(self):
        return "Name: " + self.name + ", " \
            "Description: " + self.description


# <HINT> Create a Car Model model
class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=80)
    dealer_id = models.IntegerField(null=False)
    year = models.DateField()

    SUV = 'suv'
    SEDAN = 'sedan'
    WAGON = 'wagon'
    VAN = 'microvan'
    PICKUP = 'pickup'

    TYPES = [
        (SUV, 'suv'),
        (SEDAN, 'sedan'),
        (WAGON, 'wagon'),
        (VAN, 'van'),
        (PICKUP, 'pickup'),
    ]

    type = models.CharField(null=False, max_length=20, choices=TYPES)

    def __str__(self):
        return "Name: " + self.name + " Make: " \
            + self.make.name + " Type: " \
            + self.type + " Year: " \
            + str(self.year) + " Dealer ID: " + str(self.dealer_id)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
