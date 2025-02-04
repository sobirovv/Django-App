from django.shortcuts import render

posts = [                                   #blog.views we created dummy data
    {                                       #which is list of dictionaries has 2 dummy posts
        'author': 'Gaddar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2025'
    },
    {
        'author': 'Mesut Dandun',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
