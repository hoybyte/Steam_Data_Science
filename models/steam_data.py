# Standard Library
import datetime

# Third-Party Libraries
import sqlalchemy

# noinspection PyPackageRequirements
from models.model_base import ModelBase


class Steam(ModelBase):
    __tablename__ = 'steam'
