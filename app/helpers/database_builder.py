import logging
import os

from peewee import PostgresqlDatabase

from app.models.guild_model import GuildModel
from app.models.infractor_settings_model import InfractorSettingsModel
from app.models.saved_message_model import SavedMessageModel
from app.models.user_model import UserModel

database = PostgresqlDatabase(
    host=os.getenv('DATABASE_HOST', 'localhost'),
    port=os.getenv('DATABASE_PORT', 5432),
    user=os.getenv('DATABASE_USER', 'postgres'),
    password=os.getenv('DATABASE_PASSWORD', 'postgres'),
    database=os.getenv('DATABASE_NAME', 'postgres'),
)


def create_database_structure() -> bool:
    """
    Create the database structure.

    Returns:
        bool: True if database structure created successfully, otherwise False
    """
    try:
        database.create_tables(
            [
                GuildModel,
                InfractorSettingsModel,
                SavedMessageModel,
                UserModel,
            ],
        )
    except Exception as error:
        logging.error(error)
        return False
    return True
