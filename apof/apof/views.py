from django.views.generic import TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


class Index(TemplateView):
    """
    View for main page.
    """
    template_name = 'apof/index.html'


class LoginView(View):
    """
    View for logging in to our app.
    """
    form_class = AuthenticationForm
    template_name = 'apof/login.html'

    def get(self, request):
        """
        Displays clear AuthenticationForm on page.
        """
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Log an user into app.
        """
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        return render(request, self.template_name, {'form': form})
