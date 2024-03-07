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
    path('admin_assign_timeslots/',views.admin_assign_timeslots,name='admin_assign_timeslots'),
    path('payment/<int:car_id>/<int:booking_id>/', views.payment, name='payment'),
    path('chatwithadmin/',views.chatwithadmin,name='chatwithadmin'),
    path('admin_viewchat/',views.admin_viewchat,name='admin_viewchat'),
    path('adminaccessoriesadd/',views.adminaccessoriesadd,name='adminaccessoriesadd'),
    path('accessories_list/', views.accessories_list, name='accessories_list'),
    path('update_accessory/<int:accessory_id>/', views.update_accessory, name='update_accessory'),
    path('accessories/delete/<int:pk>/', views.delete_accessory, name='delete_accessory'),
    path('accessory_view/',views.accessory_view, name='accessory_view'),
    path('admin_addcategory/',views.admin_addcategory,name='admin_addcategory'),
    path('accessories_detail/<int:accessory_id>/',views.accessories_detail,name='accessories_detail'),
    path('accessories/<int:accessory_id>/add_to_wishlist/',views.add_to_wishlist, name='add_to_wishlist'),
    path('accessories_wishlist/',views.accessories_wishlist,name='accessories_wishlist'),
    
]