from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import cohere
#
class newForm(forms.Form):
    userInput = forms.CharField(label='userInput')


# Create your views here.
def outputPoem(request,*args, **kwargs):
    form = newForm(request.POST)
    #check whether the form is valid
    if form.is_valid():
        userInput = form.cleaned_data["userInput"]
        
        #work with cohere api to write a poem about user's input (save t output variable)
        co = cohere.Client('sC2sHJQzVNhDbXiQZtYlUYvJbUc1OnnmIQPpAAff')
        response = co.generate(
        model='command-xlarge-nightly',
        prompt='Write me a haiku about '+userInput+' using imagery, metaphors, rhymes, and proper punctuation',
        temperature=0.4,
        
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        return_likelihoods='NONE')
        output='Poem: {}'.format(response.generations[0].text)

        return render(request,"output.html",{
            "output": output
        })
    else:
    #if form is not valid, render home again
        return render(request, "home.html",{
        "form": newForm()
    })

def home(request, *args, **kwargs):
    return render(request, "home.html",{
        "form": newForm()
    })