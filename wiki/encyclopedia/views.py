from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
# whenever someone adds a title at /wiki/title, will load an html related to that entry
def loadEntry(request, title):
    if title.casefold() in [entry.casefold() for entry in util.list_entries()]:
        return render(request, "encyclopedia/title.html", {
        "title" : title,
        "content" : markdown2.markdown(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/404.html", {
            "title" : title
        })


def searchEntry(request):
    q = request.GET.get('q', 'not found')
    entries = [entry.lower() for entry in util.list_entries()]

    if q in entries:
        return render(request, "encyclopedia/title.html", {
            "title" : q,
            "content" : markdown2.markdown(util.get_entry(q))
        })


    else:
        matches = []
        for entry in entries:
            if q in entry:
                matches.append(entry)
        if matches:
            return render(request, "encyclopedia/searchpage.html", {
                "displaylist" : matches
            })
        else:
            return render(request, "encyclopedia/404.html", {
                "title" : q
            })

def createEntry(request):
    return render(request, "encyclopedia/createpage.html")
    