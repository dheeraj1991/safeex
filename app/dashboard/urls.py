from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("api/lunarphase/", views.moon_data, name="moon_data"),
]
