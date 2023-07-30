# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import timedelta
from pydantic import BaseModel, Field

from tasks.Component.config_scheduler import Scheduler as BaseScheduler
from tasks.Component.config_base import ConfigBase, TimeDelta

class Scheduler(BaseScheduler):
    success_interval: TimeDelta = Field(default=TimeDelta(days=7), description='success_interval_help')
    failure_interval: TimeDelta = Field(default=TimeDelta(days=7), description='failure_interval_help')


class WeeklyTrifles(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)

