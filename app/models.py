from django.db import models

# Create your models here.
class phone(models.Model):

    name_of_phone = models.CharField(max_length=100)
    name_of_brand=models.CharField(max_length=150,default="")
    price = models.IntegerField()
    cetegory=[
        ('select','Select'),
        ('leptop','Leptop'),
        ('ipad','Ipad'),
        ('phone','Phone'),
        ('watch','Watch'),
    ]

    cetegory_of_phone = models.CharField(
        max_length=25,
        choices=cetegory,
        default='select'
    )
    color_of_phone=[
        ('select','Select'),
        ('silver','Silve r'),
        ('red','Red'),
        ('blue','Blue'),
        ('green','Green'),
        ('orange','Orange'),
    ]
    color = models.CharField(
        max_length=20,
        choices=color_of_phone,
        default='select'   
    )
    description=models.TextField(max_length=500,default="")


    def __str__(self):
        return self.name_of_phone