from django.contrib.auth.models import User
from django.db import models




class Image(models.Model):           #  connected with FK from Cat_Off
    image = models.ImageField(upload_to="cats") # this designates where you upload - it can be anywhere
    image_name = models.TextField()

    def __unicode__(self):
        return u"{0}".format(self.image) # forgot to change the self.TITLE to self.IMAGE


class Post(models.Model):            #  connected with FK from Cat_Off
    fb_post_id = models.BigIntegerField()

    owner = models.ForeignKey(User)


class CatOff(models.Model):  #TODO trademark "catoff"
    event_time = models.DateTimeField(auto_now_add=True)
    win_lose = models.BooleanField()

    judge = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    post = models.ForeignKey(Post)
