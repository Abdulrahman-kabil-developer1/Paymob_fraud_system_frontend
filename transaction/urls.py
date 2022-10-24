#import path
from django.urls import path
from . import views
app_name='transaction'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('list/transactions/',views.list_transactions,name='transactions'),
    path('send/transaction/',views.send_transaction,name='send_transaction'),
    path("list/reviews/",views.list_review_transactions,name='review'),
    path('add/blacklist/',views.add_to_BL,name='blacklist'),
    path('add/globalblacklist/',views.add_to_GBL,name='globalblacklist'),
    path('add/whitelist/',views.add_to_WL,name='whitelist'),
    path('add/globalwhitelist/',views.add_to_GWL,name='globalwhitelist'),
    path('list/blacklist/',views.list_BL,name='list_BL'),
    path('list/globalwhitelist/',views.list_GWL,name='list_GWL'),
    path('list/whitelist/',views.list_WL,name='list_WL'),
    path('change/password/',views.change_password,name='change_password'),
    path('list/globalblacklist/',views.list_GBL,name='list_GBL'),
    path('reset/password/',views.reset_password,name='reset_password'),
]