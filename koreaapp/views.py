from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Koreaapp
from .forms import KoreaappForm
from django.db.models import Q

# Create your views here.

def home(request):
    koreaapps = Koreaapp.objects.all()
    return render(request,'home.html',{'koreaapps':koreaapps})

def detail(request,id):
    koreaapp = get_object_or_404(Koreaapp, pk = id)
    return render(request,'detail.html',{'koreaapp':koreaapp})

def new(request):
    form = KoreaappForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = KoreaappForm(request.POST,request.FILES)
    if form.is_valid():
        new_koreaapp = form.save(commit=False)
        new_koreaapp.date = timezone.now()
        new_koreaapp.save()
        return redirect ('detail', new_koreaapp.id)
    return redirect('home')
def edit(request,id):
    edit_koreaapp = Koreaapp.objects.get(id=id)
    return render(request, 'edit.html', {'koreaapp':edit_koreaapp})

def update(request,id):
    update_koreaapp = Koreaapp.objects.get(id=id)
    update_koreaapp.title = request.POST['title']
    update_koreaapp.writer = request.POST['writer']
    update_koreaapp.body = request.POST['body']
    update_koreaapp.date = timezone.now()
    update_koreaapp.save()
    return redirect ('detail', update_koreaapp.id)

def delete(request,id):
    delete_koreaapp = Koreaapp.objects.get(id=id)
    delete_koreaapp.delete()
    return redirect('home')

def list(request):
    list = Koreaapp.objects.all()
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        list = list.filter(title__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'search.html', {'list':list})
    