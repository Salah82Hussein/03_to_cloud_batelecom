#from django.http import HttpResponse
#from django.http import Http404, HttpResponseRedirect

#--------------------------------------------------
#--------------------------------------------------

#from stock.my_stock.a_00_test_00.mdl_test_users import *
#from stock.my_stock.a_00_test_00.vw_test_users import * #View_open_sub_period

'''
from stock.my_stock.page_users.view_users import AuthorCreate
from stock.my_stock.page_users.view_users import AuthorUpdate
from stock.my_stock.page_users.view_users import AuthorDelete
'''

from django.contrib import admin
from django.conf.urls import url

from django.urls import path
#--------------------------------------------------
#--------------------------------------------------
# TO CALL LOGIN, LOGOUT, CHANGE PASSWORD and OTHERS USERS AUTH :

from django.contrib.auth import views as auth_views
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

from b_tel_express.my_b_tel_express.views import View_b_tel_express_index
from b_tel_express.my_b_tel_express.views import View_manage_accounts_list
from b_tel_express.my_b_tel_express.views import View_sabafon_list

from b_tel_express.my_b_tel_express.views import View_packages_list
from b_tel_express.my_b_tel_express.views import View_package_info

#--------------------------------------------------
#--------------------------------------------------
from b_tel_express.my_b_tel_express.acc_views import View_password_change
from b_tel_express.my_b_tel_express.acc_views import View_password_change_done

#from . import acc_views as views
from b_tel_express.my_b_tel_express.acc_views import View_profile
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

urlpatterns = [
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #--------------------------------------------------

    path('manage_accounts_list/', View_manage_accounts_list.as_view(), name='manage_accounts_list'),
    path('sabafon_list/', View_sabafon_list.as_view(), name='sabafon_list'),
    
    
    #path('password_change/', View_password_change.as_view(), name='password_change'),
    path('password_change/', View_password_change(), name='password_change'),
    
    path('password_change/done/', View_password_change_done.as_view(), name='password_change_done'),

    path('profile/', View_profile.as_view(), name='profile'),
    #--------------------------------------------------
    #--------------------------------------------------
    path('', View_b_tel_express_index.as_view(), name='b_tel_express_index'),
    
    path('packages_list/', View_packages_list.as_view(), name='packages_list'),

    path('package_info/<pk_package_code>/', View_package_info.as_view(), name='package_info'),
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
    
]
