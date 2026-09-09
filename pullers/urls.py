from django.urls import path
from . import views


urlpatterns = [


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



    path('', views.home, name='home'),

    path('puller_list', views.puller_list, name='puller_list'),
    path('puller/<int:pk>/', views.puller_detail, name='puller_detail'),

    path('puller_page_menu', views.puller_page_menu, name='puller_page_menu'),

    # Special Puller -> সরাসরি filtered list
    path('special-puller/', views.special_puller_page, name='special_puller_page'),

    # Regular Puller -> DA/DALH বাছাই করার menu
    path('regular-puller/', views.regular_puller_menu, name='regular_puller_page'),
    path('regular-puller/da/', views.da_puller_page, name='da_puller_page'),
    path('regular-puller/dalh/', views.dalh_puller_page, name='dalh_puller_page'),

    path('dashboard', views.dashboard, name='dashboard'),
]