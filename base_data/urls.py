from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', dashboard, name='home'),
    path('setting',setting_view,name="setting"),
    path('insertdata',insert_data,name="insertdata")
]