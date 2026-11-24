from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail  
from .models import *
from random import randint
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

# 

def registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )
        user.save()
        code = str(randint(100000, 999999))
        Emailc.objects.update_or_create(
            user = user,
            code = code
        )
        send_mail(
            f"Confirm your email  {username}",
            f"Your code {code}",
            'norep1y@softc1ub.tj',
            [user.email]
        )
        return redirect('confirm_email')
    return render(request, "registration.html")





def confirm_email(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        code = request.POST.get("code")
        user = User.objects.filter(username = username).first()
        code_obj = Emailc.objects.filter(user = user).first()
        if code_obj.code == code:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect("confirm_email")
    return render(request, 'confirm_email.html')
    
    
    
    
@login_required        
def show_profile(request):
    return render(request, "profile.html")
        
        

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")
    return render(request, 'login.html')
        
        
        
        
        
        

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        Task.objects.create(
            title=title,
            caption=caption,
            user=request.user)
        return redirect('tasks')
    return render(request,'add_task.html')



@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request,'tasks.html',{'tasks': tasks})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task,pk=id,user=request.user )
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.caption = request.POST.get('caption')
        task.save()
        return redirect('tasks')
    return render(request,'edit_task.html',{'task': task})



@login_required
def delete_task(request, id):
    task = get_object_or_404(Task,id=id,user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('tasks')




@login_required
def send_hello(request):
    users = User.objects.all()
    for user in users:
        send_mail(
            'Hello',
            'Hello!',
            'your_email@gmail.com',
            [user.email],
            html_message = f"""
            <html>
            <body style="margin:0; padding:30px; background:#f1f5f9; font-family:Arial;">
                <div style="max-width:500px; margin:auto; background:white;
                            padding:30px; border-radius:15px; text-align:center;">

                    <h1 style="color:#667eea;">👋 Hello!</h1>

                    <h2 style="color:#333;">
                        Hi, {user.username}!
                    </h2>

                    <p style="color:#666; font-size:16px;">
                        How are you ? 😊
                    </p>

                    <hr style="border:1px solid #eee;">

                    <p style="color:#999; font-size:13px;">
                        Sent by {request.user.username}
                    </p>

                </div>
            </body>
            </html>
            """
        )
        return redirect('res')
        
@login_required        
def res(request):
    return render(request, "res.html")