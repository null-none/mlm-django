from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from News.models import NewsItem

def archive(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/")
    else:
        posts = NewsItem.objects.all()
        t = loader.get_template("archive.html")
        c = Context({'posts': posts})
        return HttpResponse(t.render(c))
