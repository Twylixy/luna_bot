import peewee

from app.models.base_model import BaseModel
from app.models.user_model import UserModel


class SavedMessageModel(BaseModel):
    """Represents a saved message model."""

    id = peewee.PrimaryKeyField()
    text = peewee.TextField(null=False)
    discord_id = peewee.ForeignKeyField(
        UserModel,
        to_field='discord_id',
        on_delete='CASCADE',
    )
    hidden = peewee.BooleanField(default=False)

    class Meta:
        db_table = 'saved_messages'
