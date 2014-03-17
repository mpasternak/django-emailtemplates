# -*- encoding: utf-8 -*-

from django.test import TestCase
from django.core import mail
from emailtemplates.models import EmailTemplate

class TestEmailTemplate(TestCase):

    def setUp(self):
        e = EmailTemplate(uid = 'TEST', desc = 'This is a test', 
                          subject = 'Test subject', html = '<h1>Test!</h1>{{ parameter }}',
                          text = 'Test!\r\n{{parameter}}')
        e.save()


    def test__subst(self):
        e = EmailTemplate.objects.get(uid = 'TEST')
        self.assertEquals(e._subst('test {{param}} {{ param }}', param = '500'), 'test 500 500')


    def test_send(self):
        mail.outbox = []

        e = EmailTemplate.objects.get(uid = 'TEST')
        e.send('foo@bar.pl', 'This is a test e-mail', parameter = '123')
        self.assertEquals(len(mail.outbox), 1)

        # TODO: should parse the e-mail & check for parameter substitution too...



