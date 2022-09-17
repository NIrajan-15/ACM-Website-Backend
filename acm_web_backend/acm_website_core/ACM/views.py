from urllib import request
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
import json
import operator
import datetime
import requests


# view to post event of Event Model
class AddEvent(generics.CreateAPIView):
    querySet = Event.objects.all()
    serializer_class = EventSerializer

#view to get all events of Event Model
class EventView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

#view to get all flyers of HomePageFlyer Model
class HomepageFlyerView(generics.ListAPIView):
    queryset = HomePageFlyer.objects.all()
    serializer_class = HomePageFlyerSerializer

#view to get all topCoders of TopCoder MOdel
class TopCoderView(generics.ListAPIView):
    queryset = TopCoder.objects.all()
    serializer_class = TopCoderSerializer

#view to get all acm members of Members Model
class MemberView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

#view to get all partner sopnsers of PartnerSponserModel  
class PartnerSponserView(generics.ListAPIView):
    queryset = PartnerSponser.objects.all()
    serializer_class = PartnerSponserSerializer

#view to get all Cs almunis of CsAlmunis Model
class CsAlmuniView(generics.ListAPIView):

    queryset = CsAlumni.objects.all()
    serializer_class = CsAlumniSerializer

#view to get all Discord Links of DiscordLink Model
class DiscordLinkView(generics.ListAPIView):
    queryset = DiscordLink.objects.all()
    serializer_class = DiscordLinkSerializer

#view to get topcoders for each classification of the member model
class TopCoderView(generics.ListAPIView):
    
    # Retriving top 5 members from each classification as queryset
    topFreshmen = Member.objects.filter(classification='Freshmen').order_by('-score')[:5]
    topSophomre = Member.objects.filter(classification='Sophomore').order_by('-score')[:5]
    topJunior = Member.objects.filter(classification='Junior').order_by('-score')[:5]
    topSenior = Member.objects.filter(classification='Senior').order_by('-score')[:5]

    
    # append all classifications to queryset
    queryset= topFreshmen|topSophomre|topJunior|topSenior
    
    serializer_class = TopCoderSerializer
 
# Leaderboard view to update leetcode learderboard each month
def update_leaderBoardView():
        
        #update leaderboard if today is the 17th of the month
        if datetime.datetime.now().day == 17:
        
            #get all objects of member model
            members = Member.objects.all()

            for mem in members:

                # consumimg current members information using API
                response = requests.get("https://leetcode-stats-api.herokuapp.com/"+str(mem.leetcode_url))
                
                #convert json object to python dictionary
                leetcodedata = json.loads(response.text)
                
                #Finally update the member score in database
                Member.objects.filter(first_name=mem.first_name).update(score=leetcodedata["contributionPoints"])

    
    

    




            




    


    


