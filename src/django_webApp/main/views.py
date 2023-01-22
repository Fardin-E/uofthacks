from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import cohere
import requests #for location tracking

#
class newForm(forms.Form):
    userInput = forms.CharField(label='Place of adventure')

#for getting user's location information
def get_location():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()["ip"]
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    return response.get("city")


# Create your views here.
def outputPoem(request,*args, **kwargs):
    if request.method == "POST": #the searchbar was used
        form = newForm(request.POST)
        #check whether the form is valid
        if form.is_valid():
            userInput = form.cleaned_data["userInput"]
            
            #work with cohere api to write a poem about user's input (save t output variable)
            co = cohere.Client('sC2sHJQzVNhDbXiQZtYlUYvJbUc1OnnmIQPpAAff')
            response = co.generate(
            model='command-xlarge-nightly',
            prompt='Write a positive haiku about '+userInput+' using literary devices such as imagery, metaphors, rhymes, with commas seperating sentences',
            temperature=0.6,
            k=0,
            p=0.75,
            max_tokens=400,
            frequency_penalty=0,
            presence_penalty=0,
            return_likelihoods='NONE')
            output=' {}'.format(response.generations[0].text)

            return render(request,"output.html",{
                "output": output
            })
        else:
        #if form is not valid, render home again
            return render(request, "home.html",{
            "form": newForm()
        })
    else: # GET request "use my location" button was used

        #input is the current location
        userInput = get_location()

        #work with cohere api to write a poem about user's input (save t output variable)
        co = cohere.Client('sC2sHJQzVNhDbXiQZtYlUYvJbUc1OnnmIQPpAAff')
        response = co.generate(
        model='command-xlarge-nightly',
        prompt='Write a positive haiku about '+userInput+' using literary devices such as imagery, metaphors, rhymes, with commas seperating sentences',
        temperature=0.6,
        k=0,
        p=0.75,
        max_tokens=400,
        frequency_penalty=0,
        presence_penalty=0,
        return_likelihoods='NONE')
        output=' {}'.format(response.generations[0].text)

        return render(request,"output.html",{
                "output": output
            })




#goes to home page
def home(request, *args, **kwargs):
    return render(request, "home.html",{
        "form": newForm()
    })

