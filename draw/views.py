from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse

import json

def index(request):
    return render(request, 'draw/index.html', {})
  
# def edit_text(request):
#     return render(request, 'edit_text.html', {})

# def room(request, room_name):
#     return render(request, 'draw/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })
  
  
def allVersions(request):
   return render(request, "draw/allVersions.html")

def compare(request):
   return render(request, "draw/compare.html")