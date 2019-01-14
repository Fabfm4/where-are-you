# -*- coding: utf-8 -*-
from ..models import db


class User(db.Model):

    __tablename__ = 'usuario'  # Assign name to User Model table called usuario

    id = db.Column(db.Integer, primary_key=True, name='id_usuario', key="id")
    user_type_id = db.Column(db.Integer, nullable=False, name='id_tipo_usuario')
    email = db.Column(db.String(300), nullable=False)
    is_active = db.Column(db.Integer, name='activo')


class UserType(db.Model):

    __tablename__ = 'tipo_usuario'  # Assign name to UserType Model table called tipo_usuario

    id = db.Column(db.Integer, primary_key=True, name='id_tipo_usuario', key='id')
    nombre_tipo_usuario = db.Column(db.String(25), nullable=False)
