from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Category, Photo
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('login')

    else:
        form = CreateUserForm()

        if request.method =='POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}


        return render(request, 'photos/register.html',context)

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('gallery')

            else:
                messages.info(request,'Username or Password is incorrect')


        context ={}

    return render(request,'photos/login.html',context)

def logoutPage(request):
    logout(request)

    return redirect('login')

@login_required(login_url='login')
def gallery(request):
    user = request.user
    

    category = request.GET.get('category')
    photos = Photo.objects.filter(category__user=user)

    
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(category__user=user)

    categories = Category.objects.filter(user=user)
    
    
    
    context = {'categories': categories, 'photos': photos}
    return render(request,'photos/gallery.html', context)

@csrf_exempt
@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method =="POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] !='none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user = user, name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'], 
            image = image,
        )

        return redirect('gallery')

    context = {'categories':categories}
    return render(request,'photos/add.html', context)


@login_required(login_url='login')
def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

@login_required(login_url='login')
def delete(request,pk):

    photo = Photo.objects.filter(id=pk)
    photo.delete()
    messages.success(request,"deleted successfully")
    


    return redirect('gallery')



    
    
    
    

    



            
