from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm, NewPageForm, EditPageForm
from . import util
from random import randrange

import markdown2

def do_markdown(text):
    return markdown2.markdown(text)


def save_edit(request,title):
    form = NameForm()

    editform = EditPageForm(request.POST)
    if editform.is_valid():
        edited_content = editform.cleaned_data['page_edit_content']
        util.save_entry(title,edited_content)
        markdown = do_markdown(util.get_entry(title))
    return render(request,"encyclopedia/page.html",{
    "name":title,
    "entries": markdown,
    'form': form,
    'editpage': editform})

def random_page(request):
    entries = util.list_entries()
    nb_entries = len(entries)
    random_page = randrange(nb_entries)
    name = entries[random_page]
    form = NameForm()
    editform = EditPageForm()
    content =  util.get_entry(name)
    markdown_content = do_markdown(content)
    return render(request,"encyclopedia/page.html",{
    "name":name,
    "entries": markdown_content,
    'form': form,
    'editpage': editform
    })

def edit_page(request,title):
    if request.method == 'GET':
        content = util.get_entry(title)
        editform = EditPageForm({'page_edit_content':content})
        return render(request, "encyclopedia/edit_page.html", {
            "entries": title,
            "editpageform": editform,
            "name":title
        })
    else:
        content = util.get_entry(title)
        editform = EditPageForm()

        return render(request, "encyclopedia/edit_page.html", {
            "entries": "Call from edit",
            "editpageform": editform,
            "name":title
        })




def new_page(request):
    name_form = NameForm(request.POST)

    alert = False
    if request.method == 'POST':
        page_form = NewPageForm(request.POST)
        if page_form.is_valid():
            page_name = page_form.cleaned_data['page_name']
            page_content = page_form.cleaned_data['page_content']

            entries = util.list_entries()

            if page_name in entries:
                page_form = NewPageForm()
                alert = True
                return render(request, "encyclopedia/new_page.html", {'pageform': page_form, 'alert':alert,'form':name_form})
            else:
                util.save_entry(page_name,page_content)

    page_form = NewPageForm()
    return render(request, "encyclopedia/new_page.html", {'pageform': page_form, 'alert':alert,'form':name_form})



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data['search']
            entries = util.list_entries()
            matches = []
            for entry in entries:
                if entry.find(data) != -1:
                    matches.append(entry)
            return render(request, "encyclopedia/search_results.html", {
                "matches": matches,
                'form': form
            })
    else:
        form = NameForm()

    return render(request, 'encyclopedia/index.html', {'form': form})

def index(request):
    form = NameForm(request.POST)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': form
    })

def load_page(request,name):
    form = NameForm(request.POST)
    if util.get_entry(name) == None:
        return render(request, "encyclopedia/page.html", {
            "name":"No existing page ",
            "entries":"Sorry, Such a page does not exist.",
            'form': form
        })
    else:
        editform = EditPageForm()
        markdown_content = do_markdown(util.get_entry(name))
        return render(request,"encyclopedia/page.html",{
        "name":name,
        "entries": markdown_content,
        'form': form,
        'editpage': editform
        })
