from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def djangorocks(request):
    return HttpResponse('This is a Jazzy Response')

def picture_detail(request, category, year=0, month=0, day=0):
    template = loader.get_template("apptwo/index.html")

    picture = {
        'filename': 'mountain.jpg',
        'categories': ['color', 'landscape',],
    }

    context={
        'page_title': 'this is the picture detail',
        'description': '<p>This <b>picture</b> was taken on Mount Fuji</p>',
        'category': category,
        'year': year,
        'month': month,
        'day': day,
        'picture': picture,
        "pictures": [{
            "name" : "Duck",
            "filename": "duck.jpg"
            },
            {
                "name": "Mountain",
                "filename": "mountain.jpg",
            },
            {
                "name": "Building",
                "filename": "building.jpg",
            },
        ],
    }

    return HttpResponse(template.render(context, request))