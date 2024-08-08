from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadedFile
from django.core.files.storage import FileSystemStorage

# Create your views here.
#Upload file function to handle- you guessed it- file uploads
#
fix issue  with repo test words