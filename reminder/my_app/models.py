from django.db import models
#import Sel
#from multiselectfield import MultiSelectField

# Create your models here.
class Reminder(models.Model):
    """
    TIME_CHOICES = (('00:00:00', 'Midnight'),
                    ('01:00:00', '01 AM'),
                    ('02:00:00', '02 AM'),
                    ('03:00:00', '03 AM'),
                    ('04:00:00', '04 AM'),
                    ('05:00:00', '05 AM'),
                    ('06:00:00', '06 AM'),
                    ('07:00:00', '07 AM'),
                    ('08:00:00', '08 AM'),
                    ('09:00:00', '09 AM'),
                    ('10:00:00', '10 AM'),
                    ('11:00:00', '11 AM'),
                    ('12:00:00', 'Noon'),
                    ('13:00:00', '01 PM'),
                    ('14:00:00', '02 PM'),
                    ('15:00:00', '03 PM'),
                    ('16:00:00', '04 PM'),
                    ('17:00:00', '05 PM'),
                    ('18:00:00', '06 PM'),
                    ('19:00:00', '07 PM'),
                    ('20:00:00', '08 PM'),
                    ('21:00:00', '09 PM'),
                    ('22:00:00', '10 PM'),
                    ('23:00:00', '11 PM'),)"""
    name=models.CharField(max_length=100)
    #date=models.DateTimeField()

    time = models.TimeField(format('%H:%M'))
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    #2
    # created1=models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.time}'