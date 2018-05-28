from . import models


class User(models.UserMixin, models.db.Model):
    pass


class UserProfile(models.TimeStampedMixin, models.db.Model):

    user_id = models.db.Column(models.db.Integer, models.db.ForeignKey('user.id'))
    name = models.db.Column(models.db.String(50))
