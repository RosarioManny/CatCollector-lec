from django.db import models
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
#TOY
class Toy (models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self): 
        return self.name

#CAT
class Cat (models.Model) :
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
        # return (f'{self.breed}, {self.name}')

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
        
# FEEDING
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # get_nameofdata_display() is a DJANGO Model built-in-function. NOTE: It needs to have the choices passed. 
        return f"{self.cat} | {self.get_meal_display()} on {self.date}"
    
    class Meta :
        ordering = ['-date']