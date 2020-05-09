from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import BindMetaMixin, Model
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


class NoNameMeta(BindMetaMixin, DeclarativeMeta):
    pass


db = SQLAlchemy(
    model_class=declarative_base(cls=Model, metaclass=NoNameMeta, name="Model")
)
