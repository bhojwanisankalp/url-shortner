from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from . models import Url
import random
import string
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    """ Home page view """
    return render(request, "index.html")

@require_http_methods(['POST'])
def generate_shorter_url(request):
    """ API to Generate short urls for provied """
    source_url  = request.POST.get('source_url')
    name = request.POST.get('name', '')
    
    if source_url is None or name is None:
        return JsonResponse({'message':'This field is required [source_url, name]'}, status=400)
    
    # Create random sequence
    slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
    
    obj = Url(original_url=source_url, slug=slug, name=name)
    obj.save()

    new_url = get_slug_external(request, slug)
    
    context = { 'url':source_url, slug:slug, 'name': name, 'new_url': new_url}
    return JsonResponse({'success': True, 'data':context}, status=201)

def get_slug_external(request, slug):
    """ Helper function to create supported urls"""
    url = ''
    if request.is_secure():
        url += 'https://'
    else:
        url += 'http://'
    url += f'{request.META["HTTP_HOST"]}/u/{slug}'
    return url

@require_http_methods(['GET'])
def url_redirect(request, slugs):
    """ To redirect from shortened url to original"""
    obj = Url.objects.get(slug=slugs)
    if obj.name == 'local':
        messages.success(request, f'You are redirected from {get_slug_external(request, slugs)} to {obj.original_url}')
    return HttpResponseRedirect(obj.original_url)


def page_not_found_view(request, exception):
    """ Custom 404 page"""
    return render(request, 'not_found.html')