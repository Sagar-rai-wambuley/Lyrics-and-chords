from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator


def Home(request):
    template = 'home/index.html'
    category = Category.objects.all()
    popular = Chord.objects.filter(section__name = "popular").order_by("-id")[:10]
    catID = request.GET.get('category')
    if catID:
        allchord = Chord.objects.filter(category=catID).order_by("title_name")
        paginator = Paginator(allchord, 10000)
        req = request.GET.get('page')
        chord = paginator.get_page(req)
        total_page = chord.paginator.num_pages
    else:
        allchord = Chord.objects.all().order_by("-id")
        paginator = Paginator(allchord, 8)
        page_num = request.GET.get('page')
        chord = paginator.get_page(page_num)
        total_page = chord.paginator.num_pages
    

    context = {
        'allChords': chord,
        'category': category,
        'popular': popular,
        'last_page': total_page,
        'totalpagelist': [n+1 for n in range(total_page)]
    }
  
    return render(request, template, context)


def Lyric_And_Chord(request, id):
    template = 'home/content.html'
    YMLT_section = Chord.objects.filter(section__name = "You may like this").order_by("-id")[:12]
    category = Category.objects.all()
    single_content = Chord.objects.get(id=id)
    section = Section.objects.all()

    context = {
        'YMLT_section': YMLT_section,
        'category': category,
        'single_content': single_content,
        'section': section,
    }
    return render(request, template, context)

def Song_Request(request):
    context = {}
    template = 'home/request.html'

    requested_data = Request.objects.all().order_by('-id')
    category = Category.objects.all()


    if request.method == "POST":
       name = request.POST.get('name')
       requestsong = request.POST.get('requestsong')
       data = Request(name = name, request_song = requestsong)
       data.save()
       return HttpResponseRedirect('/request/')
    else:
        context = {
            "requested_data": requested_data,
            "category": category,
        }
        return render(request, template, context)

def Aboutus(request):
    template = 'home/aboutus.html'
    category = Category.objects.all()
    popular = Chord.objects.filter(section__name = "popular").order_by("-id")[:5]
    context = {
        "category": category,
        "popular": popular,
    }
    return render(request, template, context)


def Search(request):
    template = 'home/search.html'
    category = Category.objects.all()
    trending = Chord.objects.filter(section__name="trending").order_by("-id")[:5]
    query = request.GET.get('query')

    if len(query) > 20:
        searchResult = []
    else:
        searchResultTitle = Chord.objects.filter(title_name__icontains=query)
        searchResultContent = Chord.objects.filter(about__icontains=query)
        searchResult = searchResultTitle.union(searchResultContent)
    context = {
        "search": searchResult,
        "query": query,
        "category": category,
        "trending": trending
         }
       
    return render(request, template,context)

def chord_Section(request):
    template = 'home/section.html'
    ymlt = Chord.objects.filter(section__name = "you may like this").order_by("title_name")
    popular = Chord.objects.filter(section__name = "popular").order_by("title_name")
    trending = Chord.objects.filter(section__name = "trending").order_by("title_name")
    category = Category.objects.all()

    context = {
        "ymlt_section": ymlt,
        "popular_section": popular,
        "trending_section": trending,
        "category": category,
    }
    return render(request, template, context)
