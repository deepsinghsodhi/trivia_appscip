from django.db import models
from django.urls import reverse
# Create your models here.


# This model contains all the information abouth quizz and user
class Quizz(models.Model):
    name = models.CharField("What is your Name ?",max_length = 30,default = "") # name field to enter name which is present on homepage
    created = models.DateTimeField(auto_now_add = True) # datetime field to add date and time automatically
    PLAYER_CHOICES = (('Sachin Tendulkar','sachin tendulkar'),('Virat Kohli','virat kohli'),('Adam Gilchirst','adam gilchirst'),('Jacques Kallis','jacques kallis'))
    cricketer_name = models.CharField("who is the Best cricketer in the world ?",max_length = 45, choices = PLAYER_CHOICES, default="virat kohli") # field with cricketer name choices in dropdown
    white = models.BooleanField("WHITE color present in indian flag ?", default = False)
    yellow = models.BooleanField("YELLOW color present in indian flag ?", default = False)
    orange = models.BooleanField("ORANGE color present in indian flag ?", default = False)
    green = models.BooleanField("GREEN color present in indian flag ?", default = False)
    def __str__(self): # this will return the name of the user on the admin panel in model "Quizz"
        return self.name
    def get_absolute_url(self): # to redirect on the specified page after submitting form
        return reverse("result")
