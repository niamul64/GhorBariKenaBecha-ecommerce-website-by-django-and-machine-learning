
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('activation',views.activation, name='activation'),
    path('confirmActivation',views.confirmActivation, name='confirmActivation'),
    path('', views.home, name='home'),

    path('postAd', views.postAd, name='postAd'),
    path('<int:pId>/', views.detail, name='detail'),
    # path('myCollection', views.myCollection, name='myCollection'),
    # path('delete/myCollection/', views.myCollection, name='delete/myCollection'),
    # path('newsBee', views.newsBee, name='newsBee'),
    # path('delete/<int:pk>',views.delete.as_view(), name='delete'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
