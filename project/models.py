from django.db import models
from django.contrib.auth.models import User

SALES_CHOICES = [
    ('Sale', 'Sale'),
    ('Sold', 'Sold'),
    ('Rent', 'Rent'),
]

TYPE_CHOICES = [
    ('House', 'House'),
    ('Office Space', 'Office Space'),
]

STATE_CHOICES = [
    ('Alabama', 'Alabama'),
    ('California', 'California'),
    ('Florida', 'Florida'),
    ('Illinois', 'Illinois'),
    ('New York', 'New York'),
    ('Texas', 'Texas'),
]




class Agent(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    m_name = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='agents')
    p_number = models.CharField(max_length=200)
    email = models.EmailField()
    facebook = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    skype = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'agent_profile'

    def __str__(self):
        return f'{self.f_name} {self.l_name} {self.m_name}'


class Property(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)
    location = models.CharField(max_length=200)
    area = models.CharField(max_length=10)
    bedroom = models.CharField(max_length=10, blank=True)
    bathroom = models.CharField(max_length=10, blank=True)
    garage = models.CharField(max_length=10, blank=True)
    image = models.ImageField(null=True )
    video = models.CharField(max_length=250, blank=True)
    floor_plan = models.ImageField(blank=True)
    ubication = models.CharField(blank=True, max_length=250)
    price = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PropertyStatus(models.Model):
    asset = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='asset_status', null=True)
    status = models.CharField(choices=SALES_CHOICES, default='Sales', max_length=20)

    def __str__(self):
        return self.status


class PropertyType(models.Model):
    asset = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='types', null=True)
    type = models.CharField(choices=TYPE_CHOICES, default='House', max_length=20)

    def __str__(self):
        return self.type


class PropertyAmenity(models.Model):
    asset = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities', null=True)
    amenity = models.CharField(max_length=20)

    def __str__(self):
        return self.asset.name


class PropertyImage(models.Model):
    asset = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images', null=True)
    image = models.ImageField()

    def __str__(self):
        return self.asset.name

