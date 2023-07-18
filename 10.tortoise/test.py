# -*- coding: utf-8 -*-
# @Time    : 2023/6/30 16:03
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : test.py.py
from tortoise.models import Model
from tortoise import fields


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')

    def __str__(self):
        return self.name


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name










