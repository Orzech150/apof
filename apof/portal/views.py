from django.views.generic import TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


class Index(TemplateView):
    """
    View for main page.
    """
    template_name = 'portal/index.html'


class LoginView(View):
    """
    View for logging in to our app.
    """
    form_class = AuthenticationForm
    template_name = 'portal/login.html'

    def get(self, request, form=None):
        """
        Displays clear AuthenticationForm on page.
        """
        if form is None:
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
        return self.get(request, form)
