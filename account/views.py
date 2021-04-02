from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from account.forms import UserRegistrationForm, UserModifyForm
from account.utils import send_activation_email


class RegisterView(FormView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'account/registration.html'

    def form_valid(self, form):
        user = form.save()
        send_activation_email(user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ActivationView(View):
    def get(self, request, activation_code):
        user = get_object_or_404(get_user_model(), activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html')


def user_modify(request, pk):
    if request.method == 'POST':
        form = UserModifyForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.cleaned_data.get('first_name')
            form.cleaned_data.get('last_name')
            form.cleaned_data.get('bio')
            form.save()
            return redirect('product_list')
    else:
        form = UserModifyForm()
    return render(request, 'account/user_modify.html', {'form': form})
