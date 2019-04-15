from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path('entry/<int:year>/', views.year_archive)
    path('entry/<int:year>/<int:month>/<int:pk>/', views.month_archive)
    path('entry/<int:year>/<int:month>/<int:pk>/', views.entry_archive)


]
