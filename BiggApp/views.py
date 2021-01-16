from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Ecommerce,my_image
from django.contrib import messages
import requests
import random
import qrcode
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EcommerceSerializer
from Virus.models import cart



def logout(request):
    auth.logout(request)
    if auth.logout(request):
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def log(request):
    global av,user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            av = random.randint(1000, 9999)
            print(av)
            return redirect('/otp')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']
        mobile_no = request.POST['mobile_no']
        e_mail = request.POST['email']
        image = request.POST['image']
        user = User.objects.create_user(username=user_name, email=e_mail, password=password1, first_name=first_name,
                                        last_name=last_name,Mobile_No=mobile_no,Image=image)
        if password1 == password2:
            user.save()
            return redirect('/login')
        else:
            return redirect('/register')
    else:
        return render(request, 'hom.html')
def VS(req):
    return render(req, 'home.html')
def redmi(req):
    return render(req, 'home1.html')
def Nrzo(req):
    return render(req, 'home2.html')
def Note(req):
    return render(req, 'home3.html')
def diwali(req):
    return render(req, 'diwali.html')
def ele(req):
    return render(req, 'electronic')
def index(req):
    time = datetime.datetime.now()
    return render(req,'index.html',{'time':time})
def profile(request):
    try:
        qrdata = ['First Name', request.user.first_name,
                  'Second name', request.user.last_name,
                  'date joined', request.user.date_joined]
        sec_qr = qrcode.make(qrdata)
        file = 'static/' + request.user.username + '.jpg'
        file1 = request.user.username + '.jpg'
        sec_qr.save(file)
        return render(request, 'profile.html', {'file': file1})
    except:
        mess =  'You have No account please create...'

        return render(request,'hom.html',{'mess':mess})


def more(request):
    if request.method == 'POST':
        brand = request.POST['Brand']
        ser = Ecommerce.objects.all().filter(Brand=brand)
        return render(request,'more.html',{'ser': ser})
    else:
        return render(request,'more.html')
def otp(request):
    try:
        url = 'https://www.fast2sms.com/dev/bulk'
        params = {
        'authorization': 'v2q3bHculXsYBPVwdEGV7wz8tZaJqwGpqbXtXP7Z8a6eqKemMUinuWOeCSS1',
        'sender_id': 'FSTSMS',
        'message': av,
        'language': 'english',
        'route': 'p',
        'numbers': user.Mobile_No}
        response = requests.get(url, params=params)
        if request.method == 'POST':
            OTP = request.POST['OTP']
            if av == int(OTP):
                return render(request,'index.html')
            else:
                return redirect('/otp')
    except:
        return render(request, 'index.html')
    return render(request,'otp.html')
def video(req):
    return render(req,'video.html')
def forgotpass(request):

    return render(request,'forgotpass.html')
def Ecom(request):
    if request.method == 'POST':
        name = request.POST['name']
        features = request.POST['feature']
        brand = request.POST['brand']
        num = request.POST['num']
        price = request.POST['price']
        img = request.FILES['pic']
        ecom = Ecommerce.objects.create(Brand=brand,Name=name,features=features,price=price,mobile_no=num,image=img)
        ecom.save()
    return render(request,'moreUploads.html')
def img(request):

    if request.method == 'POST':
        name = request.POST['Pname']
        file = request.FILES['img']
        data = my_image.objects.create(image=file,Name=name)
        data.save()
        pic = my_image.objects.all()
        return render(request, 'pic.html',{"pic":pic})
def qr(request):
    qrdata = ['First Name', request.user.first_name,
            'Second name', request.user.last_name,
            'date joined', request.user.date_joined]
    sec_qr = qrcode.make(qrdata)
    file = 'static/' + request.user.username + '.jpg'
    file1 = request.user.username + '.jpg'
    sec_qr.save(file)
    if request.method == 'POST':
        code = request.POST['data']
        data = qrcode.make(code)
        v = code+'.jpg'
        f = 'static/'+code+'.jpg'
        s_data = data.save(f)
        context = {'v':v}
        return render(request, 'qr..html', context)

    return render(request, 'qr..html', {'file':file1})
def cart(request):
    if request.method == 'POST':
        name = request.user.first_name + request.user.last_name
        cart_product = request.POST['cart']
        data = cart.objects.create(User=name,product=cart_product)



class EcommerceList(APIView):
    def get(self,request):
        Ecom1 = Ecommerce.objects.all()
        serializer = EcommerceSerializer(Ecom1,many=True)
        return Response(serializer.data)

if __name__ == '__main__':
    a = '__all__'



















