# -*- coding: utf-8 -*-
from ..models import db, TimeStampedMixin, UserMixin


class User(UserMixin, db.Model):
    pass


class UserProfile(TimeStampedMixin, db.Model):

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50))
