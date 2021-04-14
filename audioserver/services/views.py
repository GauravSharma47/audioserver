from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core import serializers
import json

def index(request):
    return render(request,"services/index.html")

def create(request,type_of_data):
    if request.method=="POST":
        if request.POST.get('id')<1:
            return HttpResponse("Id cannot be less than 1")
        response=None
        if type_of_data.lower()=="song":
            song=Song(ID=request.POST.get('id'),
                    name=request.POST.get('name'),
                    duration=request.POST.get('duration'))

            song.save()
            response="created song"
        
        elif type_of_data.lower()=="podcast":
            participants=request.POST.getlist("participants")
            print("here",*participants)
            # Checking participants names
            if len(participants)>10:
                return HttpResponse("Only 10 Participants are allowed.")
            for participant in participants:
                if len(participant)>100:
                    return HttpResponse("participant's name cannot be more than 100 letters.")
            
            podcast=Podcast(ID=request.POST.get('ID'),
                            name=request.POST.get('name'),
                            duration=request.POST.get('duration'),
                            host=request.POST.get('host'),
                            participants="_".join(participants))

            podcast.save()
            response="created podcast"
        
        elif type_of_data.lower()=="audiobook":
            audiobook=AudioBook(ID=request.POST.get('ID'),
                    name=request.POST.get('name'),
                    author=request.POST.get('author'),
                    narrator=request.POST.get('narrator'),
                    duration=request.POST.get('duration'))

            audiobook.save()
            response="created Audiobook"

        else:
            response="Please check the type of audio. Types of audio available are Song, Podcast, Audio" 
        return HttpResponse(response)

def get(request,type_of_data,id):
    if id<1:
        return HttpResponse("Wrong id!")
    
    if type_of_data.lower()=="song":
        song=get_object_or_404(Song,ID=id)
        if song:
            serialized={"id":song.ID,"name":song.name,"duration":song.duration,"uploaded":str(song.uploaded_time)}
            return HttpResponse(json.dumps(serialized))
        
    elif type_of_data.lower()=="podcast":
        podcast=get_object_or_404(Podcast,ID=id)
        if podcast:
            participants=podcast.participants
            participants=participants.split("_")    
            serialized={"id":podcast.ID,"name":podcast.name,"host":podcast.host,"duration":podcast.duration,"uploaded":str(podcast.uploaded_time),"participants":participants}
            return HttpResponse(json.dumps(serialized))
    
    elif type_of_data.lower()=="audiobook":
        audiobook=get_object_or_404(AudioBook,ID=id)
        if audiobook:
            serialized={"id":audiobook.ID,"name":audiobook.name,"author":audiobook.author,"narrator":audiobook.narrator,"duration":audiobook.duration,"uploaded":str(audiobook.uploaded_time)}
            return HttpResponse(json.dumps(serialized))
    
    else:
        return HttpResponse("Please check the audio type!")

def update(request,type_of_data,id):
    if request.method=="POST":
        types_of_audio={"song":Song,"podcast":Podcast,"audiobook":AudioBook}
        if type_of_data.lower() in types_of_audio:
            obj=get_object_or_404(types_of_audio[type_of_data.lower()],ID=id)
            try:
                for key,value in request.POST.items():
                    if key=="id":
                        return HttpResponse("Cannot change ID!")
                    print(key,value)
                    setattr(obj,key,value)
                obj.save()
            except:
                return HttpResponse("Please check attribute names from localhost/type_of_audio/get/id")
        else:
            return HttpResponse("Please check type of audio")
        return HttpResponse("Updated!")

def delete(request,type_of_data,id):
    if id<1:
        return HttpResponse("Wrong id!")
    
    if type_of_data.lower()=="song":
        song=get_object_or_404(Song,ID=id)
        song.delete()
        return HttpResponse("Successfully deleted Song")
    elif type_of_data.lower()=="podcast":
        podcast=get_object_or_404(Podcast,ID=id)
        podcast.delete()
        return HttpResponse("Successfully deleted Podcast")
    
    elif type_of_data.lower()=="audiobook":
        audiobook=get_object_or_404(AudioBook,ID=id)
        audiobook.delete()
        return HttpResponse("Successfully deleted AudioBook")

    else:
        return HttpResponse("Check audio type!")