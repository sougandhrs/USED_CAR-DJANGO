from django.urls import path
from users import views
from vehimarket import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('nav',views.nav,name='nav'),
    path('checkemailexist',views.checkemailavailable,name='checkemailexist'),
    path('home',views.home,name='home'),
    path('logout/',views.logout_view,name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('admin_userview/',views.admin_userview,name='admin_userview'),
    path('sellcar/',views.sellcar,name='sellcar'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout_view,name='admin_logout'),
    path('viewcar/',views.viewcar,name='viewcar'),
    path('admin_carview/',views.admin_carview,name='admin_carview'),
    path('cardetail/<int:car_id>/',views.cardetail,name='cardetail'),
    path('car_booking/<int:car_id>/',views.car_booking,name='car_booking'),
]