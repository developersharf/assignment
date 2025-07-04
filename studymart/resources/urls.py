from django.urls import path
from . import views


urlpatterns = [
    path('django/', views.django),
    path('resources/', views.resources),
    path('blog/', views.blog),
   
   
    
]
