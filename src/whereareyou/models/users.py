# -*- coding: utf-8 -*-
from ..models import db, TimeStampedMixin, UserMixin, PermissionMixin, CatalogueMixin,  MatrixPermissionMixin


class Permission(PermissionMixin, db.Model):

    matrix_profiles = db.relationship(
        'MatrixProfile',
        backref='permission',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )


class Profile(CatalogueMixin, db.Model):
    __tablename__ = 'profiles'

    matrix_permissions = db.relationship(
        'MatrixProfile',
        backref='profile',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )

    users = db.relationship(
        'User',
        backref='profile',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )

    never_delete = db.Column(db.Boolean, default=False, nullable=True)


class User(UserMixin, db.Model):

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


class MatrixProfile(MatrixPermissionMixin, db.Model):

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))
    __table_args__ = (
        db.UniqueConstraint(
            'profile_id',
            'permission_id',
            name='profile_permission'),
    )


# class UserProfile(TimeStampedMixin, db.Model):
# 
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     name = db.Column(db.String(50))
#     __tablename__ = 'user_profiles'
