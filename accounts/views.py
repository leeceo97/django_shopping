from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import LoginForm, RegisterForm
from .models import User

def index(request):
    if "user" in request.session :
        user_id = request.session.get('user')
        user = User.objects.get(id=user_id)
        return render(request,'index.html',{'email':user.email})
    else: 
        user = 'none'
        return render(request,'index.html',{'email':user})
        
        

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.user_id
        return super().form_valid(form)

def logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/')