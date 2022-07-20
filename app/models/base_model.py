import os

import peewee

from app.helpers.exceptions import FailedToConnectToDatabaseError


class BaseModel(peewee.Model):
    """Represents base model."""

    class Meta:
        database = peewee.PostgresqlDatabase(
            host=os.getenv('DATABASE_HOST', 'localhost'),
            port=os.getenv('DATABASE_PORT', 5432),
            user=os.getenv('DATABASE_USER', 'postgres'),
            password=os.getenv('DATABASE_PASSWORD', 'postgres'),
            database=os.getenv('DATABASE_NAME', 'postgres'),
        )

        try:
            database.connect()
        except peewee.OperationalError as error:
            raise FailedToConnectToDatabaseError(error)
        finally:
            database.close()
