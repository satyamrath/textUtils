# this file is created by me - User

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):

    # get the text
    djtext = request.POST.get('text', 'default') # will take value as default if no text parameter is found

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    print(djtext)
    purpose = ""
    # check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    
        purpose = purpose + "Remove Punctuations, "
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        purpose = purpose + "Upper Case, "
        djtext = analyzed
    
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
    
        purpose = purpose + "Remove New Lines, "
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and index+1 < len(djtext) and djtext[index+1] == " "):
                analyzed = analyzed + char

        purpose = purpose + "Remove Extra Spaces, "
        djtext = analyzed

    if charcount == 'on':
        count = 0
        for char in djtext:
            count = count + 1
        
        purpose = purpose + "Count Characters"
        djtext = '"'+djtext + '"' + f" is having {count} characters"
            
    # if purpose != "":
    params = {'purpose': purpose, 'analyzed_text': djtext}
    return render(request, 'analyze.html', params)

    # else:
        # return HttpResponse("Error")
