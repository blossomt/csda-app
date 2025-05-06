from django.http import HttpResponse
from django.template import loader

from .models import Quote

import random

def index(request):
    quotes = list(Quote.objects.all())
    selected_quote = random.choice(quotes)
    template = loader.get_template("polls/index.html")
    context = {"quote": selected_quote}
    return HttpResponse(template.render(context, request))