from django.shortcuts import render,redirect,get_object_or_404
from .forms import PictureForm
from .models import Pictures, Category
from django.http import HttpResponseForbidden
def index(request):
    pictures=Pictures.objects.all().order_by('-created_at')
    categories=Category.objects.all()
    category_id=request.GET.get('category')
    search_query=request.GET.get('q')
    if category_id:
        pictures=pictures.filter(category=category_id)
    if search_query:
        pictures=pictures.filter(title__icontains=search_query)
    context = {'pictures':pictures,'categories':categories}

    return render(request, 'gallery/index.html', context)
def addPicture(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture=form.save(commit=False)
            picture.user=request.user
            picture.save()
            return redirect('index')
    else:
        form=PictureForm()

    return render(request, 'gallery/addPicture.html', {'form':form})
def picture_detail(request, pk):
    picture= Pictures.objects.get(pk=pk)
    return render(request, 'gallery/picture_detail.html', {'picture':picture})

def edit_picture(request,pk):
    picture = Pictures.objects.get(pk=pk)
    if request.user!=picture.user:
        return HttpResponseForbidden('У вас нет прав на изменение работы')
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=picture)
        picture.user=request.user
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=PictureForm(instance=picture)

    return render(request,'gallery/edit_picture.html',{'form':form,'picture':picture})
def delete_picture(request,pk):
    picture = Pictures.objects.get(pk=pk)
    if request.user!=picture.user:
        return HttpResponseForbidden('У вас нет прав на удаление работы')
    if request.method == "POST":
        picture.delete()
        return redirect('index')
    return render(request,'gallery/delete_picture.html',{'picture':picture})

# Create your views here.
