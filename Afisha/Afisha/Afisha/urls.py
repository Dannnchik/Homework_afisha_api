from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to the Afisha Movie API!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/v1/', include('movie_app.urls')),

]
