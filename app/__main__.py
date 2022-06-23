import logging
from os import environ

from app.cogs.infractor_cog import InfractorCog
from app.cogs.sayer_cog import SayerCog
from app.entrypoints import luna_instance

logging.basicConfig(
    level=environ.get('DEBUG_LEVEL', 'INFO'),
    format=environ.get(
        'DEBUG_FORMAT',
        '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    ),
    datefmt=environ.get('DEBUG_DATEFMT', '%H:%M:%S'),
)

luna_instance.add_cog(SayerCog(luna_instance))
luna_instance.add_cog(InfractorCog(luna_instance))

if __name__ == '__main__':
    luna_instance.run(environ.get('BOT_TOKEN'))
