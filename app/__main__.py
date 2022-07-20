import logging
import sys
import os

from app.cogs.infractor_cog import InfractorCog
from app.cogs.sayer_cog import SayerCog
from app.entrypoints import luna_instance
from app.helpers.database_builder import create_database_structure

logging.basicConfig(
    level=os.getenv('DEBUG_LEVEL', 'INFO'),
    format=os.getenv(
        'DEBUG_FORMAT',
        '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    ),
    datefmt=os.getenv('DEBUG_DATEFMT', '%H:%M:%S'),
)

luna_instance.add_cog(SayerCog(luna_instance))
luna_instance.add_cog(InfractorCog(luna_instance))

if os.getenv('DEBUG') in {'true', 'false', '1', '0'}:
    logging.debug('Variable DEBUG is equal to true, running migrations...')
    create_result = create_database_structure()

    if create_result is False:
        logging.error('Unable to create database structure')
        sys.exit(1)


if __name__ == '__main__':
    luna_instance.run(os.getenv('TOKEN'))
