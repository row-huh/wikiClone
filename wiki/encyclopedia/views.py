from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
# whenever someone adds a title at /wiki/title, will load an html related to that entry
def loadEntry(request, title):
    if title in util.list_entries():
        return render(request, util.list_entries())
        return render(request, "encyclopedia/title.html", {
        "title" : title,
        "content" : markdown2.markdown(util.get_entry(title))
        })
    else:
        return render(util.list_entries())
        return render(request, "encyclopedia/404.html", {
            "title" : title
        })

def searchEntry(request, query):
    if query in util.list_entries():
        return render(request, "encyclopedia/title.html"), {
            "title" : query,
            "content" : markdown2.markdown(util.get_entry(query))
        }
    display_list = []
    for entry in util.list_entries():
        if query in entry:
            display_list.append(query)
    return render(request, "encyclopedia/searchpage.html"), {
        "displaylist" : display_list
    }
    
    