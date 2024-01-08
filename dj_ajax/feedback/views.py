from django.shortcuts import render
from .forms import FeedbackForm
from django.http import JsonResponse
from django.core.mail import send_mail

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def feedback(request):
    return render(request, 'feedback/index.html', {'form': FeedbackForm})

def feedback_form(request):
    form = FeedbackForm()
    if request.method == "POST":
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if not is_ajax:
            print('not ajax requests!')
            return render(request, "contact.html", {"form": form})
        ip = get_client_ip(request)
        print(ip)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            form.save()
            
            return JsonResponse({"name": name, "email": email}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "feedback/index.html", {"form": form})