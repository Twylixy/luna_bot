import discord
import peewee
from discord.ext import commands

from app.helpers.message_analyzer import MessageAnalyzer
from app.models.saved_message_model import SavedMessageModel


class SayerCog(commands.Cog):
    """Represent a `sayer` cog-module."""

    def __init__(self, luna_instance: commands.Bot) -> None:
        """
        Initialize a new `sayer` instance.

        Args:
            luna_instance: discord.ext.commands.Bot
        """
        self.luna_instance = luna_instance

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """
        Handle a messages.

        Args:
            message: discord.Message
        """
        if self.luna_instance.user.mentioned_in(message):
            # ignore E712, due to that is database query
            random_message = (
                SavedMessageModel.select()
                .where(SavedMessageModel.hidden == False)  # noqa: E712
                .order_by(peewee.fn.Random())
                .limit(1)
            ).get()

            await message.reply(random_message.text)
            return

        analyzer = MessageAnalyzer(message)

        if analyzer.is_valid:
            SavedMessageModel.create(
                discord_id=message.author.id,
                text=message.content,
            )
