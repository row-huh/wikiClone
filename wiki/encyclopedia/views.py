from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponse
import random
import os


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
    q = request.GET.get('q', '')
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


def create(request):
    return render(request, "encyclopedia/createpage.html")

 
def createEntry(request):
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    entries = [entry.lower() for entry in util.list_entries()]
    if title in entries:
        # throw some error because you cannot create two entries of the same name
        return HttpResponse("Page already exists, try again")
    else: 
        f = open("entries/"+title+".md", 'w')
        f.write(content) 
        f.close()
        return render(request, "encyclopedia/title.html", {
            "title" : title,
            "content" : markdown2.markdown(util.get_entry(title))
        })


def randompage(request):
    randompage = random.choice(util.list_entries())
    return render(request, "encyclopedia/title.html", {
        "title" : randompage,
        "content" : markdown2.markdown(util.get_entry(randompage))
    })
    
def editpage(request, title):
    return render(request, "encyclopedia/edit.html", {
        "title" : title, 
        # not converting to markdown because the user needs to see .md structure
        "content" : util.get_entry(title)
    })
    
def saveEntry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        f = open(os.path.join('entries/', title + '.md'), 'w')
        f.seek(0)
        f.write(content)
        f.close()
        return render(request, "encyclopedia/title.html", {
            "title" : title,
            "content" : markdown2.markdown(util.get_entry(title))
        })