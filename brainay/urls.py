from django.urls import path
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('Contact/', views.Contact, name='Contact'),
   path('about_us/', views.about_us, name='about_us'),
   path('Blog/', views.Blog, name='Blog'),
   path('product/', views.product, name='product'),
   path('playgroup/', views.playgroup, name='playgroup'),
   
   path('KG1/', views.KG1, name='KG1'),
   path('KG2/', views.KG2, name='KG2'),
   path('nursery/', views.nursery, name='nursery'),
   path('phonics/', views.phonics, name='phonics'),
   path('login/', views.login, name='login'),
   path('signup/', views.signup, name='signup'),
   path('register/', views.register, name='register'),
   path('verify/<str:token>', views.varify, name='success'),
   path('login_user/', views.login_user, name='login_user'),
   path('trackorder/', views.trackorder, name='trackorder'),
   path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
   path('cart/', views.cart, name='cart'),
   path('checkout/', views.checkout, name='checkout'),
   path('singleblog/', views.singleblog, name='singleblog'),



]