import peewee

from app.models.base_model import BaseModel


class GuildModel(BaseModel):
    """Represents a guild model."""

    id = peewee.PrimaryKeyField()
    guild_id = peewee.BigIntegerField(null=False, unique=True)

    class Meta:
        db_table = 'guilds'
