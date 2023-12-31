# app_auth/views.py
from django import forms

from django.contrib.auth import forms as auth_forms, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView, DeleteView

from e_commerce_shop.app_auth.forms import RegisterUserForm


def not_found_view(request):
    raise Http404("This page does not exist")


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # Static way of providing 'success_url'
    success_url = reverse_lazy('products_app:all_products')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    # Dynamic way of providing 'success_url'
    # def get_success_url(self):
    #     pass


class LoginUserView(auth_views.LoginView):
    """
       Display the login form and handle the login action.
       """
    template_name = 'app_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'app_auth/logout.html'


UserModel = get_user_model()


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'


class UserProfileDetailView(auth_mixins.LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'app_auth/account_details.html'
    context_object_name = 'user_profile'


class UserProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserModel
    template_name = 'app_auth/edit_profile.html'
    fields = ['email', 'first_name', 'last_name', ]

    def get_success_url(self):
        return reverse_lazy('details_user', kwargs={'pk': self.object.pk})


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'app_auth/delete_profile.html'
    success_url = reverse_lazy('register_user')
