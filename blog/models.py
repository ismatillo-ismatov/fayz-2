from django.db import models
from fontawesome_5.fields import IconField
from django.conf import settings


class Category(models.Model):
    name = models.CharField('Nomi',max_length=50)
    slug = models.SlugField('Slug',max_length=50)
    icon = IconField(blank=True)

    def __str__(self):
        return self.name

    def icon_class(self):
        i = str(self.icon).split(',')
        return f"fa fa-{i[1]}"



class Post(models.Model):
    category = models.ForeignKey(Category,related_name="postlar",on_delete=models.CASCADE,verbose_name="katalog",)
    name = models.CharField('Nomi',max_length=55)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='image',blank=True,null=True)
    old_price = models.PositiveIntegerField("Eski narhi",default=0,blank=True)
    price = models.PositiveIntegerField("Hozirgi narhi",default=0,blank=True)

    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="Userdata")
    phone = models.CharField("Telefon",max_length=50)
    adress = models.CharField("adress",blank=True,max_length=50)
    card_number = models.PositiveIntegerField(default=0)
    like_dislike = models.ManyToManyField(Post)



