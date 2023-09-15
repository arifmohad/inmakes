from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import updateform

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
# Create your views here.


class viewlist(ListView):
    model = task
    template_name = 'details.html'
    context_object_name = 'obj'

class detailview(DetailView):
    model = task
    template_name = 'newdet.html'
    context_object_name = 'abc'

class updateview(UpdateView):
    model = task
    template_name = 'newupd.html'
    context_object_name = 'abc'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('dview',kwargs={'pk':self.object.id})

class detailview(DeleteView):
    model = task
    template_name = 'viewdetails.html'
    success_url = reverse_lazy('view')


def hello(request):
    obj = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority')
        date = request.POST.get('date')

        Task=task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,'details.html',{'obj':obj})

def delete(request,id):
    obj=task.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')

    return render(request,'viewdetails.html')


def update(request,id):
    obj = task.objects.get(id=id)
    form1=updateform(request.POST or None, instance=obj)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'update.html',{'form':form1,'obj':obj})




