from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# For now we are doing re-direct to that register page only.
# In 1st page it is acting like a model and in 2nd part it is acting like a form since it is model-form.
def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        context={
            'form': form
        }
        if(form.is_valid()):
            form.save()
        return redirect('/authenticate/login')
    else:
        form = UserCreationForm()
        context={
            'form': form
        }
    return render(request,'authenticate/register.html',context)