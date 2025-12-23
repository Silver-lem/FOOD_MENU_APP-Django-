from django.db import models

# Create your models here.
class Item(models.Model):

    # Defining the string representation of objects -- esentially saying when the objects are retrived display them in a particular manner
    def __str__(self):
        return self.item_name


    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    #To add images -- add CharField which stores the URL of the image
    item_image = models.CharField(max_length=500,default="https://theme-assets.getbento.com/sensei/193414f.sensei/assets/images/catering-item-placeholder-704x520.png")
    