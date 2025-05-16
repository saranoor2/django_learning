from django.db import models
from django.utils import timezone
# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     # this function basically modify the way an Ad object is displayed. 
    #     # if there was no __str__ fn and we call Ad we will <QuerySet [<Ad: Ad object (2)>, <Ad: Ad object (3)>]>
    #     # since we have we will now get <QuerySet [<Ad: Property>, <Ad: books>, <Ad: Medicine>, <Ad: Medicine>, <Ad: Kitchen>]>
    #     return self.type
    
    def make_live(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta:
        db_table = 'ad' #if not table would be Ad
