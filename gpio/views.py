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
    # Picks the last data from the model
    system_data = models.SystemInfo.objects.values().last()
    # Handles POST call from html template
    if request.POST:
        # Collected dict keys, to get the name of the submit button that we are clicking 
        html_data = list(request.POST.keys())
        # The name will be available at the index position 1 of the keys list
        html_name = html_data[1]
        # Getlist is called on the particular queryse dict object to get the list of values passed for the name.
        # Here the list is generated with 2 index postion as for the same name we have checkbox and save button
        # If the check box is checked it returns value as "on". Checking using == operator, returns True or False
        html_state = request.POST.getlist(html_name)[0] == 'on'        
        # Models operation: 
        # Get the particular role using name of the row
        button_obj = models.Button.objects.get(name=html_name)
        # Replacing existing True/False state with new state
        button_obj.state = html_state
        # Saving the model changes
        button_obj.save()
        # Returns back to same page
        return redirect(reverse('gpio:home'))
    # Handles API transactions
    elif 'api/' in request.path:
        # Handles UPDATE method from api
        if request.method == 'UPDATE':
            # Decodes the json data from the request body
            json_data = json.loads(request.body.decode("utf-8"))
            # Iterates list of json data
            for data in json_data:
                # Models operation: 
                # Get the particular role using name of the row
                button_obj = models.Button.objects.get(name=data['name'])
                # Replacing existing True/False state with new state
                button_obj.state = data['state']
                # Saving the model changes
                button_obj.save()
            return HttpResponse(status=202, content='Status updated successfully')
        elif request.method == 'POST':
            # Delete existing values
            models.SystemInfo.objects.all().delete()
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