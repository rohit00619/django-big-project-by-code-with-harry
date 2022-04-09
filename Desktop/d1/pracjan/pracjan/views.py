# I have created this file Rohit Chandoriya

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    exspaceremover = request.POST.get('exspaceremover', 'off')
    # Anaylyze the text
    if removepunc=='on':
        punctuations = '''!@#$%^&*()_+=-[]\|}{;'":,./?><~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if capitalize=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Capitalization', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Newline Remover', 'analyzed_text': analyzed}
        djtext = analyzed
    if exspaceremover=='on':
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]== " "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext=analyzed
    if (removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and exspaceremover != 'on'):
        return HttpResponse("Error")
    return render(request,'analyze.html',params)

def about(request):
    return HttpResponse(" About wala Hello")
