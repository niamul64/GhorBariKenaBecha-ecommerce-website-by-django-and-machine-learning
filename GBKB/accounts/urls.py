
from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('activation',views.activation, name='activation'),
    path('confirmActivation',views.confirmActivation, name='confirmActivation'),
    path('', views.home, name='home'),
    # path('share', views.share, name='share'),
    #
    # path('myCollection', views.myCollection, name='myCollection'),
    # path('delete/myCollection/', views.myCollection, name='delete/myCollection'),
    # path('newsBee', views.newsBee, name='newsBee'),
    # path('delete/<int:pk>',views.delete.as_view(), name='delete'),
]
