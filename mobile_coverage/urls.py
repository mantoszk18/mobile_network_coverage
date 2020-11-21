from django.urls import path, include

from . import views


urlpatterns = [
    path('api/find', views.FindNetworkCoverageView.as_view()),
]