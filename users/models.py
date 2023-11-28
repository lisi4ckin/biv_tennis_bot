from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tennis_users'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_rating = models.IntegerField(null=False, blank=False, default=1000)

    def __str__(self):
        return self.user.username + ' ' + str(self.user_rating)

    class Meta:
        db_table = 'tennis_user_profiles'
