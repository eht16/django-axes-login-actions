# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.core.mail import mail_admins
from django.template import loader, Context
from logging import getLogger as get_logger
from socket import gethostbyaddr, error as SocketError

logger = get_logger(__name__)


#----------------------------------------------------------------------
def notify(access_attempt, **kwargs):
    site = Site.objects.get_current()
    ip_address = access_attempt.ip_address
    fqdn = _resolve_ip_address_to_fqdn(ip_address)

    if access_attempt.failures == 0:
        login_success_msg = u'successful'
        login_success = True
    else:
        login_success_msg = u'failed'
        login_success = False

    context = dict(
        attempt_time=access_attempt.attempt_time,
        failures=access_attempt.failures,
        fqdn=fqdn,
        site_domain=site.domain,
        site=site,
        ip_address=ip_address,
        login_success=login_success,
        login_success_msg=login_success_msg,
        user_agent=access_attempt.user_agent,
        username=access_attempt.username)

    subject = u'Security: %(site_domain)s: %(login_success_msg)s login attempt by %(ip_address)s (%(fqdn)s)' % context
    message = _render_email_message(context)

    mail_admins(subject, message, fail_silently=False)


#----------------------------------------------------------------------
def _resolve_ip_address_to_fqdn(ip_address):
    if ip_address is None:
        return None
    try:
        return gethostbyaddr(ip_address)[0]
    except SocketError, e:
        logger.warn(u'IP -> FQDN resolution failed for "%s": %s', ip_address, unicode(e))


#----------------------------------------------------------------------
def _render_email_message(context):
    template = loader.get_template("axes_login_actions/email_notify.txt")
    return template.render(Context(context))
