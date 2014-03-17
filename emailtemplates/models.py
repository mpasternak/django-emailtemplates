# -*- encoding: utf-8 -*-

from django.core.mail import EmailMultiAlternatives
from django.core.mail import get_connection
from django.db import models
from django.template import loader, Context
from django.utils.translation import ugettext as _

from emailtemplates.conf import settings


class EmailTemplate(models.Model):
    """I am an e-mail template. I can be sent. 
    """

    uid = models.CharField(max_length = 50, db_index = True, unique = True)
    desc = models.CharField(max_length = 200)

    subject = models.CharField(max_length = 200)
    html = models.TextField(max_length = 40960)
    text = models.TextField(max_length = 40960)

    # Perhaps in the future:
    # email_class = models.ForeignKey(EmailClass)
    # lang = models.CharField(max_length = 2)

    class Meta:
        verbose_name = _("e-mail template")
        verbose_name_plural = _("e-mail templates")

        
    def __unicode__(self):
        return self.desc


    def _subst(self, s, **subst):
        t = loader.get_template_from_string(s)
        c = Context(subst)
        return t.render(c)


    def send(self, to, toName, _from = None, _fromName = None, **kw):
        """Send me to a user "toName" <to>". 

        **kw is a dictionary of values for the template.
        """

        if _from is None:
            _from = settings.EMAILTEMPLATES_FROM

        if _fromName is None:
            _fromName = settings.EMAILTEMPLATES_FROM_NAME

        if 'siteName' not in kw:
            kw['siteName'] = settings.EMAILTEMPLATES_SITE_NAME

        subj = self._subst(self.subject, **kw)
        textBody = self._subst(self.text, **kw)
        htmlBody = self._subst(self.html, **kw)

        connection = get_connection(fail_silently=False)
        email = EmailMultiAlternatives(subject = subj,
            body = 'This is a multi-part message in MIME format.',
            from_email = _from, to = [to], connection = connection)
        email.attach_alternative(textBody, "text/plain")
        email.attach_alternative(htmlBody, "text/html")
        return email.send()



class MailServerFailure(models.Model):
    when = models.DateTimeField(auto_now_add = True)
    reason = models.CharField(max_length = 2500)
    client_ip = models.CharField(max_length = 250)
