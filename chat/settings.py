"""
Default ChatterBot settings for Django.
"""
from django.conf import settings
from chat.extras import constants


CHATTERBOT_SETTINGS = getattr(settings, 'CHATTERBOT', {})

CHATTERBOT_DEFAULTS = {
    'name': 'ChatterBot',
    'storage_adapter': 'chat.extras.storage.DjangoStorageAdapter',
    'input_adapter': 'chat.extras.input.VariableInputTypeAdapter',
    'output_adapter': 'chat.extras.output.OutputAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

CHATTERBOT = CHATTERBOT_DEFAULTS.copy()
CHATTERBOT.update(CHATTERBOT_SETTINGS)
