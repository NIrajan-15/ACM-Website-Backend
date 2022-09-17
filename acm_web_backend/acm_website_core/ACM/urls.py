
from django.urls import path, include
from .views import *
from rest_framework import routers
from . import views
from .views import *



urlpatterns = [

    #path to post a event
    path('add_event', AddEvent.as_view(), name='add_event'),

    #path to get events 
    path('api/events/',EventView.as_view(), name='events'),

    #path to get flyers
    path('api/flyers/', HomepageFlyerView.as_view(),name='flyers'),

    #path to get topCoders
    path('api/topCoder/', TopCoderView.as_view(), name='topCoders'),

    

    #path to get members
    path('api/member/', MemberView.as_view(), name='members'),

    #path to get sponsers
    path('api/sponser/', PartnerSponserView.as_view(), name='sponsers'),

    #path to get the CsAlmunis
    path('api/almuni/', CsAlmuniView.as_view(),name='almunis'),

    #path to get DiscordLinks
    path('api/discord_links/', DiscordLinkView.as_view(), name='discord_link'),

    path('api/topfreshmens/', TopCoderView.as_view(),update_leaderBoardView(),name='topFreshmen'),

]
