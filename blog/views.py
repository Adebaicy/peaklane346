from django.shortcuts import render, get_object_or_404
from blog.models import News

# Create your views here.
def blog_home(request):
    news=News.objects.all().order_by('-created_on')[0:10]
    return render(request, "blog_home.html", {
        
        "posts":news})


def blog_detail(request, title1):
    detail=get_object_or_404(News, slug=title1)
    return render(request, "blog_show.html", {
        
        "details":detail})