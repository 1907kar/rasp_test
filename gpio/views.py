from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from . import models
from django.urls import reverse
from django.middleware import csrf
import json

# Create your views here.
def home(request):
    """
    This handles both api/ui request/response/render
    """
    # Collect data from Button model
    button_data = models.Button.objects.values()
    system_data = models.SystemInfo.objects.values().last()
    # Handles POST call from html template
    if request.POST:
        html_data = list(request.POST.keys())
        html_name = html_data[1]
        html_state = request.POST.getlist(html_name)[0] == 'on'
        button_obj = models.Button.objects.get(name=html_name)
        button_obj.state = html_state
        button_obj.save()
        return redirect(reverse('gpio:home'))
    # Handles API transactions
    elif 'api/' in request.path:
        # Handles UPDATE method from api
        if request.method == 'UPDATE':
            json_data = json.loads(request.body.decode("utf-8"))
            for data in json_data:
                button_obj = models.Button.objects.get(name=data['name'])
                button_obj.state = data['state']
                button_obj.save()
            return HttpResponse(status=202, content='Status updated successfully')
        elif request.method == 'POST':
            pi_data = request.body.decode("utf-8")
            system_info_obj = models.SystemInfo()
            system_info_obj.data = pi_data
            system_info_obj.save()
            return HttpResponse(status=201, content='Information saved successfully')
        else:
            # Handles GET method from api
            return JsonResponse(list(button_data), safe=False)
    # Handles GET call from html template
    else:
        return render(request, 'gpio/home.html', context={'data': button_data, 'system': system_data})  
    

def get_csrf(request):
    """
    This is for Generating csrf token, which is essential for sending UPDATE request via postman or any means
    """
    return HttpResponse(csrf.get_token(request))