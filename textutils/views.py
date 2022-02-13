# I have created this file - Rishi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    uppercaps = request.POST.get('uppercaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spacerem = request.POST.get('spacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check Which Checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:,.'"\<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Puctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(uppercaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if(spacerem=="on"):
        analyzed = ""
        #First Method
        # for char in djtext:
        #     if char != "  ":
        #         analyzed = analyzed + char
        #Second Method
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            analyzed+=1
        params = {'purpose': 'Number of Characters.', 'analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc != 'on' and uppercaps!="on" and newlineremover!="on" and spacerem!="on" and charcount != "on"):
        return HttpResponse("<h1>Please select any operation and try again!</h1>")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
