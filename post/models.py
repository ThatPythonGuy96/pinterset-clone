from django.db import models
from user.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
    
    def pin_no(self):
        return self.post_tag.count()
    
class Pin(models.Model):
    profile = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="profile_post")
    pin = models.ImageField(upload_to='pins')
    pin_tag = models.ManyToManyField(Tag, related_name="post_tag", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{str(self.id)} - {self.description}"

class Board(models.Model):
    name = models.CharField(max_length=20)
    profile = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="board_profile")
    pin = models.ManyToManyField(Pin, related_name="board_pin")