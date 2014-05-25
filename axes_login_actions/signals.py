# -*- coding: utf-8 -*-

from axes.models import AccessAttempt
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.importlib import import_module


DEFAULT_ACTION = 'axes_login_actions.actions.email.notify'
ACTIONS = getattr(settings, 'AXES_LOGIN_ACTIONS', [DEFAULT_ACTION])


#----------------------------------------------------------------------
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
    except (ValueError, ImportError, AttributeError), e:
        raise ImportError("Could not import the name: %s: %s" % (path, e))


#----------------------------------------------------------------------
@receiver(post_save, sender=AccessAttempt)
def access_attempt_handler(sender, instance, **kwargs):
    for action_path in ACTIONS:
        action = import_dotted_path(action_path)
        action(instance, **kwargs)
