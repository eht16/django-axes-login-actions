# -*- coding: utf-8 -*-

from importlib import import_module

from axes.models import AccessAttempt
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


DEFAULT_ACTION = 'axes_login_actions.actions.email.notify'
ACTIONS = getattr(settings, 'AXES_LOGIN_ACTIONS', [DEFAULT_ACTION])


# ----------------------------------------------------------------------
def import_dotted_path(path):
    """
    Takes a dotted path to a member name in a module, and returns
    the member after importing it.
    """
    # stolen from Mezzanine (mezzanine.utils.importing.import_dotted_path)
    try:
        module_path, member_name = path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, member_name)
    except (ValueError, ImportError, AttributeError) as e:
        raise ImportError('Could not import the name: {}: {}'.format(path, e))


# ----------------------------------------------------------------------
@receiver(post_save, sender=AccessAttempt, dispatch_uid='axes_login_actions_post_save')
def access_attempt_handler(sender, instance, **kwargs):
    for action_path in ACTIONS:
        action = import_dotted_path(action_path)
        action(instance, **kwargs)
