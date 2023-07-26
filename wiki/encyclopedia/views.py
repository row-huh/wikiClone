from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
# whenever someone adds a title at /wiki/title, will load an html related to that entry
def loadEntry(request, title):
    return render(request, "encyclopedia/title.html", {
        "title" : title,
        "content" : util.get_entry(title)
        })