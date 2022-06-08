#new created file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    dtext = request.POST.get('text', 'default')
    print(dtext)
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('UPPERCASE', 'off')
    print(removepunc)
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!@#$%^&*()_+<>?:"'''
    analyzed = ""
    if uppercase == 'on' and removepunc == 'on' and charcount == 'on':
        for char in dtext:
            if char not in punctuations:
                analyzed += char.upper()

        params = {'purpose': 'Remove and upper character', 'analyze_text': analyzed}
        return (render(request, 'analyze.html', params))
    elif uppercase == 'on' or removepunc == 'on' or charcount == 'on':
        if removepunc == 'on':

            for char in dtext:
                if char not in punctuations:
                    analyzed += char
            analyzed += '\n'


            params = {'purpose': 'Remove Punctuation', 'analyze_text': analyzed}
            return (render(request, 'analyze.html', params))
        elif uppercase == 'on':

            for char in dtext:
                analyzed += char.upper()

            params = {'purpose': 'Counting character', 'analyze_text': analyzed}
            return (render(request, 'analyze.html', params))
        else:
            if charcount == 'on':

                for char in dtext:
                    if not char == " ":
                        analyzed += char





                params = {'purpose': 'Counting character', 'analyze_text': len(analyzed)}
                return (render(request, 'analyze.html', params))


    else:
        params = {'purpose': 'Do nothing', 'analyze_text': dtext}
        return render(request, 'analyze.html', params)


# def about(request):
#     return HttpResponse('About Saru')

# def index(request):
#     return HttpResponse('<button>Home</button>')

# def removepunc(request):
#     return HttpResponse("removepunc")
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlinermv(request):
#     return HttpResponse("newlinermv")
# def spacermv(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     print(request.GET.get('text', 'default'))
#     return HttpResponse("charcount")
