# -*- encoding: utf-8 -*-

from django.core.mail import send_mail

from emailtemplates.models import MailServerFailure


def get_client_ip(request):
    """get a client IP like:

        "remote_addr=255.255.255.255 forwarded_for=10.0.0.0 42.0.32.12 ..."

    ... up to 250 characters.
    """

    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    ra = request.META.get('REMOTE_ADDR')

    if xff and ra:
        ret = "remote_addr=%s forwarded_for=%s" % (ra, xff)

    elif xff:
        ret = "forwarded_for=%s" % xff

    elif ra:
        ret = "remote_addr=%s" % ra

    else:
        ret = "unknown"

    return ret[:250]


def check_mail_server(request):
    """When you absolutley must have a working e-mail server, you can check it.

    This function tries to send a test e-mail. If there are any exceptions during
    sendind the e-mail, it saves the reason to the database using MailServerFailure
    object.
    """

    try:

        send_mail('Test email', 'This is e-mail server test. Please ignore it.',
                  'nobody@localhost', ['mail-server-test@localhost'], fail_silently = False)

    except Exception, e:

        MailServerFailure(client_ip = get_client_ip(request),
                          reason = ("%r" % str(e))[:2500]).save()

        return False

    return True
