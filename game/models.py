from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class RoleCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cards")
    shots = models.IntegerField()
    sheild = models.BooleanField()
    disapear = models.BooleanField()
    allsheild = models.BooleanField()
    disable = models.IntegerField()
    repeat_disable = models.BooleanField()
    bomb = models.BooleanField()
    fast_bomb = models.BooleanField()
    waking = models.IntegerField()
    gun = models.IntegerField()
    fake_gun = models.IntegerField()
    query = models.IntegerField()
    heal = models.IntegerField()

    def get_image(self):
        return self.image


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.ForeignKey(RoleCard, on_delete=models.CASCADE)


class ZodiacGameStatus(models.Model):
    turns = models.BooleanField(default=False, blank=True)
    challenge = models.BooleanField(default=False, blank=True)
    challenger = models.IntegerField(null=True, blank=True)
    challenger_wanters = models.JSONField(null=True, blank=True)
    room_name = models.CharField(max_length=100, blank=True)
    day = models.BooleanField(default=True, blank=True)
    days = models.IntegerField(null=True, blank=True)
    speak_turn = models.IntegerField(null=True, blank=True)
    magicman = models.IntegerField(default=0, blank=True)
    bomber = models.BooleanField(default=False, blank=True)
    zodiac = models.IntegerField(default=0, blank=True)
    ocean = models.JSONField(null=True, blank=True)
    gunner_fake = models.IntegerField(default=0, blank=True)
    gunner_real = models.BooleanField(default=False, blank=True)
    died = models.JSONField(null=True, blank=True)


class ZodiacRoom(models.Model):
    level = models.IntegerField()
    Winners = models.CharField(max_length=100)
    roles = models.ManyToManyField(Role, max_length=12)
    status = models.ForeignKey(
        ZodiacGameStatus, on_delete=models.CASCADE, null=True, related_name="room"
    )
