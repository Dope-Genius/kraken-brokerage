from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('deposit', views.deposit, name='deposit'),
  path('forgot', views.forgot, name='forgot'),
  path('signin', views.signin, name='signin'),
  path('signup', views.signup, name='signup'),
  path('withdraw', views.withdraw, name='withdraw'),
  path('transaction', views.transaction, name='transaction'),
  path('investment', views.investment, name='investment'),
  path('notification', views.notification, name='notification'),
  path("delete/<int:pk>/", views.delete_notify, name="delete_notify"),
  path('support-ticket', views.support, name='support-ticket'),
  path('referrals', views.referrals, name='referrals'),
  path('profile', views.profile, name='profile'),
  path('logout', views.logout, name='logout'),
]
