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
    # If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
    if q in entries:
        return render(request, "encyclopedia/title.html", {
            "title" : q,
            "content" : markdown2.markdown(util.get_entry(q))
        })
    # If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays 
    # a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should 
    # appear in the search results.
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
    