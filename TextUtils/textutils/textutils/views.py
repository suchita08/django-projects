from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcap=request.POST.get('fullcap','off')
    newlinerremover=request.POST.get('newlinerremover','off')
    extraspaceremover=request.POST.get('spaceremover','off')
    purpose=''
    if(removepunc=='on'):
        analyze_txt=" "
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtxt:
            if char not in punctuations:
                analyze_txt=analyze_txt+char
        purpose+='Removing Punctuaion'+" "
        params={'purpose':purpose,'analyzed_text':analyze_txt}
        djtxt=analyze_txt
    if(fullcap=='on'):
        analyze_txt=" "
        for char in djtxt:
            analyze_txt=analyze_txt+char.upper()
        purpose += 'Uppercase' + " "
        params = {'purpose': purpose, 'analyzed_text': analyze_txt}
        djtxt = analyze_txt
    if (newlinerremover == 'on'):
        analyze_txt = " "
        for char in djtxt:
            if char!='\n' and char!='\r':
                analyze_txt = analyze_txt + char.upper()
        purpose += 'Removing Newline' + " "
        params = {'purpose': purpose, 'analyzed_text': analyze_txt}
        djtxt = analyze_txt
    if (extraspaceremover == 'on'):
        analyze_txt = " "
        for index, char in enumerate(djtxt):
            if not (djtxt[index] == " " and djtxt[index + 1] == " "):
                analyze_txt = analyze_txt + char
        purpose += 'Removing Extraspace'
        params = {'purpose': purpose, 'analyzed_text': analyze_txt}
    if(removepunc!='on' and fullcap!='on' and newlinerremover!='on' and extraspaceremover!='on'):
        return HttpResponse("Please select any Operation and try again!!")
    return render(request,'analyze.html',params)
