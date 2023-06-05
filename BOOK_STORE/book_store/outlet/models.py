from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text  import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Country"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postalcode = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Address Entries"

    def __str__(self):
        return f"{self.street} {self.city}"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    # id = models.AutoField() # This is added to every identity by Django
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default = "", blank = True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country,null=True)


    def get_absolute_url(self):
        return reverse("book_detail", args= [self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save( *args, **kwargs)
    

    def __str__(self):
        return f"{self.title}({self.rating})"
