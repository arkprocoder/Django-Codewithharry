#I have created this file - Jay Patel
from django.http import HttpResponse
from django.shortcuts import render


#code for video 6
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

# def about(request):
#     return HttpResponse("About Jay Patel")

def ex1(request):
    return HttpResponse(''' 
    <h2>Navbar</h2> 
    <li><a href = "">Google</a></li>
    <li><a href = "">Youtube</a></li>
    <li><a href = "">Twitter</a></li>
    <li><a href = "">Facebook</a></li>
    <li><a href = "">Instagram</a></li>''')



def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #check the check box value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('countchar', 'off') 

    #Analyze the text
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Full Capitalise', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char

        params = {'purpose': 'Extra Space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == "on":
        count = 0
        for index, char in enumerate(djtext):
              if not(djtext[index] == " "):
                count = count + 1

        analyzed = "Characters in your Sentence are : {}".format(count)
        params = {'purpose' : 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("""capitalize first <br> <a href = "http://127.0.0.1:8000/" >Home</a>""")

# def newlineremove(request):
#     return HttpResponse(""" newline remove  <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)

# def spaceremove(request):
#     return HttpResponse(""" space remover  <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)

# def charcount(request):
#     return HttpResponse(""" charcount <br> <a href = "http://127.0.0.1:8000/" >Home</a> """)