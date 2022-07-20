import peewee

from app.models.base_model import BaseModel


class UserModel(BaseModel):
    """Represents a user model."""

    id = peewee.PrimaryKeyField()
    discord_id = peewee.BigIntegerField(null=False, unique=True)

    class Meta:
        db_table = 'users'
