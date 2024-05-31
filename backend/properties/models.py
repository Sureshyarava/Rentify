from django.db import models
from accounts.models import CustomUser


class Property(models.Model):
    property_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    place = models.CharField(max_length=150)
    area = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    near_by_hospital = models.CharField(max_length=100)
    near_by_college = models.CharField(max_length=100)

    def __str__(self):
        return f"Property at {self.place} which is of {self.area} sq Km"
