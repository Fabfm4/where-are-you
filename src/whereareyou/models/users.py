# -*- coding: utf-8 -*-
from ..models import db, TimeStampedMixin, UserMixin, PermissionMixin, CatalogueMixin,  MatrixPermissionMixin
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship


class Permission(PermissionMixin, db.Model):

    profiles = relationship("MatrixProfile")

    pass


class Profile(CatalogueMixin, db.Model):
    __tablename__ = 'profiles'

    users = relationship("User")
    permissions = relationship("MatrixProfile")


class User(UserMixin, db.Model):

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    profile = relationship("Profile", back_populates="users")


class MatrixProfile(MatrixPermissionMixin, db.Model):

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))

    profile = relationship("Profile", back_populates="permissions")
    permission = relationship("Permission", back_populates="profiles")
    __table_args__ = (
        UniqueConstraint(
            'profile_id',
            'permission_id',
            name='_profile_permission_uc'
        ),
    )


class UserProfile(TimeStampedMixin, db.Model):

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(50))
    __tablename__ = 'user_profiles'
