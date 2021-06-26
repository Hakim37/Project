from django.db import models
class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=100)
    car_engine = models.CharField(max_length=100)
    #car_model = models.CharField(max_length=100)
    production_year = models.IntegerField(max_length=10)
    def _str_(self):
        return self.car_brand
