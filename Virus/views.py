from django.shortcuts import render,HttpResponse
from .models import files,SuperUser

# Create your views here.
def hello(request):
    return render(request,'hello.html')
def file_upload(request):
    if request.method == 'POST':
        name = request.POST['Fname']
        file = request.FILES['file']
        f = files.objects.create(f_name=name,file=file)

        f.save()
        f1 = files.objects.all().filter(f_name='video')
        print(f1)
        context = {'f1':f1}
        return render(request,'File_U.html',context)
    else:
        return render(request,'File_U.html')
def S_user(request):
    data = SuperUser.objects.all().filter(last_name='Dinesh')

    return render(request,'SuperUser.html',{'data':data})



