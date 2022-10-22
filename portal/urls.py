from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings
# app_name = 'waste'
from django.contrib.auth.views import LogoutView

urlpatterns = [
# path('admin/', admin.site.urls),
path("dashboard/", views.dashboard, name="dashboard"),
path("chartsPlot/", views.chartsPlot, name="charts"),
path("getDistricts/<str:region>/", views.getDistricts, name="getDistricts"),

path("", views.landingPage, name="landing_page"),



]


# handler502 = 'portal.views.error502'
# handler404 = 'portal.views.error404'