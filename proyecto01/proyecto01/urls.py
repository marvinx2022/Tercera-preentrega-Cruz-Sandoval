
from proyecto01.views import saludo, mejor_saludo, saludar_por_nombre, load_about
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('mejor_saludo', mejor_saludo),
    path('saludar_nombre/<nombre>', saludar_por_nombre),
    path('info/', load_about),
    path('AppCoder/', include('AppCoder.urls'))
    
]
