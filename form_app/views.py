from django.shortcuts import render, redirect
from django.views import View
from .forms import FormModelForm
from django.contrib import messages

class IndexView(View):
    
    def get(self, request):
        form = FormModelForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context=context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = FormModelForm(data)
        
        if form.is_valid():
            messages.success(request, 'Form added')
            form.save()

        context = {
            'form': form
        }
        return render(request, 'index.html', context=context)
