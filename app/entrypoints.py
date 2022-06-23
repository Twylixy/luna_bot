import logging
from os import environ
from typing import Union

import discord
from discord.commands.context import ApplicationContext
from discord.ext import commands
from discord.ext.commands import Context

from app.models.guild_model import GuildModel
from app.models.infractor_settings_model import InfractorSettingsModel
from app.models.user_model import UserModel

intents = discord.Intents(messages=True, message_content=True)

luna_instance = commands.Bot(
    command_prefix=environ.get('BOT_COMMAND_PREFIX', '-'),
    case_insensitive=environ.get('BOT_CASE_INSENSITIVE', False),
    owner_id=environ.get('BOT_OWNER_ID', None),
    strip_after_prefix=environ.get('BOT_STRIP_AFTER_PREFIX', True),
    intents=intents,
)


@luna_instance.event
async def on_ready() -> None:
    """Callback when bot is ready"""
    logging.info('The bot is ready [{0.user}]'.format(luna_instance))


@luna_instance.event
async def on_message(message: discord.Message) -> None:
    """
    Handler for new messages

    Params:
        message: discord.Message
    """
    await luna_instance.process_commands(message)


@luna_instance.before_invoke
async def check_for_user_registration(ctx: Union[Context, ApplicationContext]) -> None:
    """
    Action before bot invoke event

    Params:
        ctx: Union[Context, ApplicationContext]
    """
    if ctx.user.bot is True:
        return

    GuildModel.get_or_create(
        guild_id=ctx.guild.id,
    )

    UserModel.get_or_create(
        discord_id=ctx.author.id,
    )

    InfractorSettingsModel.get_or_create(
        guild_id=ctx.guild.id,
    )
