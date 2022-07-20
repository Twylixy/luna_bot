from __future__ import annotations

from dataclasses import dataclass

from app.models.infractor_settings_model import InfractorSettingsModel


@dataclass
class TextedInfractorSettings:
    """Represents texted `infractor` settings."""

    infractor_is_enabled: str
    bad_words_is_enabled: str
    link_filter_is_enabled: str
    spam_detector_is_enabled: str

    @classmethod
    def get_texted_settings(
        cls: TextedInfractorSettings,
        settings: InfractorSettingsModel,
    ) -> TextedInfractorSettings:
        """
        Build texted settings from model.

        Args:
            settings: InfractorSettingsModel

        Returns:
            TextedInfractorSettings
        """
        texted_settings = {}

        if settings.infractor_is_enabled is True:
            texted_settings['infractor_is_enabled'] = '🟢'
        else:
            texted_settings['infractor_is_enabled'] = '⚫️'

        if settings.bad_words_is_enabled is True:
            texted_settings['bad_words_is_enabled'] = '☑️ Enabled'
        else:
            texted_settings['bad_words_is_enabled'] = '❌ Disabled'

        if settings.link_filter_is_enabled is True:
            texted_settings['link_filter_is_enabled'] = '☑️ Enabled'
        else:
            texted_settings['link_filter_is_enabled'] = '❌ Disabled'

        if settings.spam_detector_is_enabled is True:
            texted_settings['spam_detector_is_enabled'] = '☑️ Enabled'
        else:
            texted_settings['spam_detector_is_enabled'] = '❌ Disabled'

        return cls(**texted_settings)
