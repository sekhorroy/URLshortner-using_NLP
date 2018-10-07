from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.conf import settings
from django.http import HttpResponse
from .models import Urls
import json
from contextualizer import context_manager


# Create your views here.
def index(request):
    return render(request, 'tinyurl/index.html')

def re_direct_url(request, urls_id):
    url = get_object_or_404(Urls, pk=urls_id)
    url.count = url.count+1
    url.save()
    return redirect(url.httpurl)

def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        request_content = context_manager.get_context_from_article(url)
        request_content_join = '-'.join(request_content)
        b = Urls(httpurl=url, short_id=request_content_join)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + request_content_join
        print(response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


