# -*- encoding: utf-8 -*-

from django.conf import settings

EMAILTEMPLATES_SITE_NAME = getattr(settings, "EMAILTEMPLATES_SITE_NAME", "my.site.com")
EMAILTEMPLATES_FROM = getattr(settings, "EMAILTEMPLATES_FROM", "foo@my.site.com")
EMAILTEMPLATES_FROM_NAME = getattr(settings, "EMAILTEMPLATES_FROM_NAME", "Foo Bar")
