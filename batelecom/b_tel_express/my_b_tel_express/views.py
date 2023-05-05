#from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import requires_csrf_token
#from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token
#from django.template import RequestContext

import logging
import requests, json

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
#---------------------------------------------------------
#---------------------------------------------------------
class View_manage_accounts_list(LoginRequiredMixin, View):
    template_name = 'my_services/manage_accounts_list.html'

    def get(self, request): 
    #def get(): #self, request
        return render(request, self.template_name, )
#---------------------------------------------------------
class View_sabafon_list(LoginRequiredMixin, View):
    template_name = 'my_services/sabafon_list.html'

    def get(self, request): 
    #def get(): #self, request
        return render(request, self.template_name, )
#---------------------------------------------------------


#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
class View_b_tel_express_index(LoginRequiredMixin, View):
    template_name = 'b_tel_express_index.html'

    def get(self, request): 
    #def get(): #self, request
        return render(request, self.template_name, )
#---------------------------------------------------------

class b_tel_index_xxxxx(LoginRequiredMixin, View):
    template_name = 'b_tel_index.html'


    def get(self, request):

        t = loader.get_template(self.template_name)
        c = {"foo": "bar"}



        '''
        return render(
        request,
        self.template_name,
        {
            "foo": "bar",
        },
        content_type="JSON",
        )
        '''

        return HttpResponse(t.render(c, request), content_type="application/json")
    
    
    #def get(): #self, request
        #return render(request, self.template_name, )

#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------

class View_get_packages_list_SOURCE(LoginRequiredMixin, View):
    template_name = 'get_packages_list.html'
    #template_name = 'b_tel_index.html'

    def get(self, request): 
    #def get(): #self, request
        return render(request, self.template_name, )

    #path('get_packages_list', View_get_packages_list.as_view(), name = "get_packages_list"),
    #http://185.240.65.38:8014/API/Packages/List/
#---------------------------------------------------------

class View_packages_list_OK(LoginRequiredMixin, View):
    template_name = 'my_services/get_packages_list.html'

    def get(self, request): 

        #return HttpResponseRedirect("http://185.240.65.38:8014/API/Packages/List/")
        #return render_to_response('my_services\test.html', { 'foo': 123, 'bar': 456 })
        
        #context = {'foo': 'bar'}
        #return render(request, 'index.html', context)


        #return redirect_to(request, "http://185.240.65.38:8014/API/Packages/List/", **kwargs)

        #return render(request, 'my_services\test.html', { 'foo': 123, 'bar': 456 })
    


        return render(request, self.template_name, )
#---------------------------------------------------------
class View_packages_list_OK_2(LoginRequiredMixin, View):
    #template_name = 'my_services/get_packages_list.html'
    template_name = 'my_services/test.html'

    def get(self, request): 

        #return HttpResponseRedirect("http://185.240.65.38:8014/API/Packages/List/")
        return render(request, self.template_name, )
#---------------------------------------------------------
class View_packages_list_Z1(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'

    def get(self, request): 
        response=requests.get('http://185.240.65.38:8014/API/Packages/List/').json()
        return render(request, self.template_name,{'response':response})

#---------------------------------------------------------
class View_packages_list_z2(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'
    
    def get(self, request):
        response = requests.get(self.url)
        response.raise_for_status()  # raises exception when not a 2xx response
        if response.status_code != 204:
            return response.json()

#---------------------------------------------------------
class View_packages_list_zz_1(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'

    def get(self, request): 
        #response=requests.get('http://185.240.65.38:8014/API/Packages/List/')#.json()
        #response=requests.get('https://api.covid19api.com/countries').json()

        response=requests.get('http://185.240.65.38:8014/API/Packages/List').text
        return render(request, self.template_name,{'response':response})

#---------------------------------------------------------
class View_packages_list_ok_ok(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'

    def get(self, request):
        #response = requests.get('https://jsonplaceholder.typicode.com/users')
        response = requests.get(self.url)

        #jsonResponse = json.loads(response.content)
        my_packages_list = json.loads(response.content)

        #convert reponse data into json
        #users = response.json()
        #users = response.text
        
        #print(jsonResponse)
        #print(users)

        
        #return HttpResponse("Users")
        #return render(request, self.template_name)
        return render(request, self.template_name, {'my_packages_list': my_packages_list})
        #pass

        

#---------------------------------------------------------
class View_packages_list_ok_ok_2(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'

    def get(self, request):
        response = requests.get(self.url)
        response.raise_for_status()  # raises exception when not a 2xx response
        if response.status_code != 204:
            my_packages_list = response.json()
            #return response.json()



        #response = requests.get(self.url)
         #my_packages_list = json.loads(response.content)

        return render(request, self.template_name, {'my_packages_list': my_packages_list})
        #pass

#---------------------------------------------------------
class View_packages_list_xx_1(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'

    #req = urllib.request.Request('https://v2.gcchmc.org/book-appointment/')
    #response = requests.get('https://v2.gcchmc.org/book-appointment/', headers=headers)
    #response = requests.get(self.url)

    
    def get(self, request):
        #response = urllib.request.Request(self.url)
        response = requests.get(self.url)

        
        #response.raise_for_status()  # raises exception when not a 2xx response
        #if response.status_code != 204:
        #my_packages_list = response.json()
        #return response.json()



        #response = requests.get(self.url)
        #my_packages_list = json.loads(response.content)
        my_packages_list = json.loads(response.content)
        
        return render(request, self.template_name, {'my_packages_list': my_packages_list})
    
        #return render(request, self.template_name, {"csrf_token": get_token(request), 'my_packages_list': my_packages_list}, context_instance=RequestContext(request))
        #return render(request, self.template_name, {"csrf_token": get_token(request), 'my_packages_list': my_packages_list}, )
        #pass

#---------------------------------------------------------
class View_packages_list(LoginRequiredMixin, View):
    template_name = 'my_services/packages_list.html'
    url = 'http://185.240.65.38:8014/API/Packages/List/'
    http = 'http://185.240.65.38:8014/API/Packages/List/'
    https = 'https://185.240.65.38:8014/API/Packages/List/'
    

    def get(self, request):
        proxy = { 
                "http"  : self.http, 
                "https" : self.https, 
            }

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}
        #response = requests.get(self.url, proxies=proxy)
        response = requests.get(self.url, headers=headers)
        

        #response.raise_for_status()  # raises exception when not a 2xx response
        #if response.status_code != 204:

        #my_packages_list = response.text
        my_packages_list = json.loads(response.text)
        #my_packages_list = response.json()

        #response.raise_for_status()  # raises exception when not a 2xx response
        #if response.status_code != 204:
            #my_packages_list = response.json()
            #return response.json()



        #response = requests.get(self.url)
         #my_packages_list = json.loads(response.content)

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
    
