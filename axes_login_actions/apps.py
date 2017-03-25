# -*- coding: utf-8 -*-

from django.apps import AppConfig


# #######################################################################
class AxesLoginActionsConfig(AppConfig):
    name = 'axes_login_actions'

    # ----------------------------------------------------------------------
    def ready(self):
        import axes_login_actions.signals
