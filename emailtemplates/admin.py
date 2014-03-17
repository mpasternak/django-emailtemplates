# -*- encoding: utf-8 -*-

from django.contrib import admin
from emailtemplates.models import EmailTemplate
from emailtemplates.models import MailServerFailure


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['desc', 'subject']
    readonly_fields = ['uid']
    pass

admin.site.register(EmailTemplate, EmailTemplateAdmin)


class MailServerFailureAdmin(admin.ModelAdmin):
    list_display = ['when', 'client_ip', 'reason']
    readonly_fields = ['when', 'client_ip', 'reason']
    pass

admin.site.register(MailServerFailure, MailServerFailureAdmin)
