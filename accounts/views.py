from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import LoginForm, RegisterForm
from .models import User

def index(request):
    user_id = request.session.get('user')
    user = User.objects.get(id=user_id)
    return render(request,'index.html',{'email':user.email})

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