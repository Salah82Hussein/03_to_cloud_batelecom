from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


import logging
import requests, json

from django.contrib.auth.decorators import login_required
from .acc_forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response


from django.http import HttpResponse
#from django.template import loader

from django.shortcuts import render

# Create your views here.

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#---------------------------------------------------------
#@login_required
def profilex(request):
    return render(request, 'my_acc/profile.html', {'title': _('Profile'), 'pretitle': _('Manage your profile')})


#---------------------------------------------------------
class View_profile(LoginRequiredMixin, View):
    template_name = 'my_acc\profile.html'
    initial = {'key': 'value'}
    
    def get(self, request):
        #def get(self, request):
        #template_name = 'my_acc\profile.html'
        #form = self.form_class(self.request.GET or None, instance=my_obj)
        #form = self.form_class(self.request.GET)#, instance=self.request.GET)
        
        return render(request, self.template_name )
        #return render(request, self.template_name, {'title': _('Profile'), 'pretitle': _('Manage your profile')})

#---------------------------------------------------------
class View_password_change_ss(LoginRequiredMixin, View):
    template_name = 'my_acc\password_change_form.html'
    form_class = PasswordChangeForm
    

    def get(self, request):
        #form = self.form_class(self.request.GET or None, instance=my_obj)
        form = self.form_class(self.request.GET)#, instance=self.request.GET)
        
        return render(request, self.template_name, {'form': form} )
        #return PasswordChangeView.as_view(template_name=self.template_name, form_class=self.form_class)
    
#---------------------------------------------------------
#class View_password_change(LoginRequiredMixin, View):
def View_password_change():
    
    template_name = 'my_acc\password_change_form.html'
    form_class = PasswordChangeForm
    #return PasswordChangeView.as_view(template_name=self.template_name, form_class=self.form_class)
    return PasswordChangeView.as_view(template_name=template_name, form_class=form_class)


#---------------------------------------------------------
    #path('password_change/', PasswordChangeView.as_view(template_name='accounts/accounts/password_change_form.html',
    #                                                    form_class=PasswordChangeForm), name='password_change'),
    
    
#---------------------------------------------------------
class View_password_change_done(LoginRequiredMixin, View):
    template_name = 'my_acc\password_change_done.html'

    def get(self, request):
       
        return render(request, self.template_name, )

#---------------------------------------------------------

class View_packages_list(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'

    def get(self, request):
        #response = requests.get('https://jsonplaceholder.typicode.com/users')
        response = requests.get(self.url)

        #jsonResponse = json.loads(response.content)
        my_packages_list = json.loads(response.content)

        return render(request, self.template_name, {'my_packages_list': my_packages_list})
        #pass

#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
class View_package_info(LoginRequiredMixin, View):
    template_name = 'my_services/package_info.html'
    
    #initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        pk_package_code = self.kwargs.get('pk_package_code')

        url = 'http://185.240.65.38:8014/API/Packages/Information/Code=%s' % (pk_package_code)
        
        
        response = requests.get(url)
        my_package_info = json.loads(response.content)

        return render(request, self.template_name, {'my_package_info': my_package_info, 'Code': pk_package_code})
        #pass


#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
    
