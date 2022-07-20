import os

import discord


class MessageAnalyzer:
    """Represents a message analyzer."""

    def __init__(self, message: discord.Message) -> None:
        """
        Initialize a new MessageAnalyzer.

        Args:
            message: discord.Message
        """
        self.entity = message
        self.text = message.content
        self.author_id = message.author.id
        self.words = message.content.split()
        self.length = len(message.content)

    @property
    def is_valid(self) -> bool:
        """
        Check is the message passing conditions.

        Returns:
            bool
        """
        if self.entity.mentions:
            return False
        if len(self.words) <= int(os.getenv('MA_WORDS_COUNT', '3')):
            return False
        if self.length <= int(os.getenv('MA_TEXT_LENGTH', '10')):
            return False
        if self.entity.author.bot is True:
            return False
        if '\n' in self.text:
            return False
        return True
