#I have created this file - Jay Patel
from django.http import HttpResponse
from django.shortcuts import render


#code for video 6
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

# def about(request):
#     return HttpResponse("About Jay Patel")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off') 
    print(djtext)
    print(removepunc)
    #Analyze the text

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    else:
        return HttpResponse("Error")

    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("""capitalize first <br> <a href = "http://127.0.0.1:8000/" >Home</a>""")

# def newlineremove(request):
#     return HttpResponse(""" newline remove  <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)

# def spaceremove(request):
#     return HttpResponse(""" space remover  <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)

# def charcount(request):
#     return HttpResponse(""" charcount <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)