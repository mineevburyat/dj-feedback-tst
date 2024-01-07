from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def feedback(request):
    return render(request, 'feedback/index.html', {'form': FeedbackForm})

