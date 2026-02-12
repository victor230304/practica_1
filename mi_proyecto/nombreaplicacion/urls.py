from django.urls import path
from .views import vista_uno, vista_dos, vista_tres

urlpatterns = [
    path("uno/", vista_uno, name="vista_uno"),
    path("dos/", vista_dos, name="vista_dos"),
    path("tres/", vista_tres, name="vista_tres"),
]