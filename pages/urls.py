from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.HomePageViews.as_view(), name="home")
]
