from django.contrib import admin
from .models import *

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['title','date']

class TopCoderAdmin(admin.ModelAdmin):
    model = TopCoder
    list_display = ['first_name','middle_name','last_name']

class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ['first_name','middle_name','last_name','classification']

class CsAlmuniAdmin(admin.ModelAdmin):
    model = CsAlumni
    list_display = ['first_name','middle_name','last_name']

class DiscordLinkAdmin(admin.ModelAdmin):
    model = DiscordLink
    list_display = ['title','link']

admin.site.register(Event,EventAdmin)
admin.site.register(TopCoder,TopCoderAdmin)
admin.site.register(HomePageFlyer)
admin.site.register(Member,MemberAdmin)
admin.site.register(PartnerSponser)
admin.site.register(CsAlumni,CsAlmuniAdmin)
admin.site.register(DiscordLink, DiscordLinkAdmin)




admin.site.site_header = "ACM Website Admin"
admin.site.site_title = "ACM Website Admin"
admin.site.index_title = "Welcome to ACM Website's Admin page !"