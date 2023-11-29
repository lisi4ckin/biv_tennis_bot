from django.db import models


class UserProfile(models.Model):
    user_rating = models.IntegerField(null=False, blank=False, default=1000)
    user_telegram_chat_id = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'tennis_user_profiles'


class User(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                   primary_key=False, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tennis_users'
