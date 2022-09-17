from distutils.command.upload import upload
from django.db import models
import datetime


# Create your models here.

# Event Model to store all the upcoming events.
class Event(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


# HomepageFlyer Model to store the flyers in the homepage.
class HomePageFlyer(models.Model):
    flyer1 = models.ImageField()
    flyer2 = models.ImageField()
    flyer3 = models.ImageField()

    


# TopCoder Model to store tocoders info.
class TopCoder(models.Model):

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+self.last_name

# Choices for classification of the member
CLASSIFICATIONS = (("Freshmen","Freshmen"),("Sophomore","Sophomore"),("Junior","Junior"),("Senior","Senior"))
    
# Member Model to store all acm members
class Member(models.Model):

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20)
    classification = models.CharField(max_length=20,choices=CLASSIFICATIONS)
    github_username = models.CharField(max_length=20)
    leetcode_url = models.CharField(max_length=20,null=True,blank=True)
    linkedin_url = models.CharField(max_length=40)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name+self.last_name

#Model to store all partner sponser's logos.
class PartnerSponser(models.Model):
    sponser_logo = models.ImageField()


#Model to store all computer science aluminis.
class CsAlumni(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    alumni_photo = models.ImageField(null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+self.last_name

#Model to store discore links
class DiscordLink(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title