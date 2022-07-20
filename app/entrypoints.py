import logging
import os
from typing import Union

import discord
from discord.commands.context import ApplicationContext
from discord.ext import commands

from app.models.guild_model import GuildModel
from app.models.infractor_settings_model import InfractorSettingsModel
from app.models.user_model import UserModel

intents = discord.Intents(messages=True, message_content=True)

luna_instance = commands.Bot(
    command_prefix=os.getenv('COMMAND_PREFIX', '-'),
    case_insensitive=os.getenv('CASE_INSENSITIVE', False),
    owner_id=os.getenv('OWNER_ID', None),
    strip_after_prefix=os.getenv('STRIP_AFTER_PREFIX', True),
    intents=intents,
)


@luna_instance.event
async def on_ready() -> None:
    """Event when bot is ready."""
    logging.info('The bot is ready [{0.user}]'.format(luna_instance))


async def check_for_user_registration(
    ctx: Union[commands.Context, ApplicationContext],
) -> None:
    """
    Check user's and guild's registration.

    Args:
        ctx: Union[Context, ApplicationContext]
    """
    if ctx.author.bot is True:
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


@luna_instance.event
async def on_message(message: discord.Message) -> None:
    """
    Handle new messages.

    Args:
        message: discord.Message
    """
    ctx: discord.Context = await luna_instance.get_context(message)
    await check_for_user_registration(ctx)
    await luna_instance.process_commands(message)
