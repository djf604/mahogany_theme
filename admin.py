__author__ = 'Dominic Fitzgerald'
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import Page, RichTextPage
from models import HomePage, Event, EventsPage, OptionalRichtextPage
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'time')

# Insert background into all Page admin
page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]['fields'].insert(2, u'background')
PageAdmin.fieldsets = page_fieldsets

admin.site.register(Event, EventAdmin)
admin.site.unregister(RichTextPage)
admin.site.unregister(Page)
admin.site.register(RichTextPage, PageAdmin)
admin.site.register(OptionalRichtextPage, PageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(HomePage, PageAdmin)
admin.site.register(EventsPage, PageAdmin)
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)
