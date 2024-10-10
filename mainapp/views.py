from django.http import HttpResponse
from django.shortcuts import render
# from .tasks import parse_and_save_rss
from .tasks import rand

# Create your views here.
def test(request):
    # parse_and_save_rss.delay()
    rand.delay()
    return HttpResponse("Done")