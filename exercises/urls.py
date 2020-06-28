
from django.urls import path

from .views import exercise_description_view, exercise_view, StorageGeoJson


urlpatterns = [
    path('exercise_description/', exercise_description_view, name='exercise_description_view'),
    path('exercise/', exercise_view, name='exercise'),
    path("StorageGeoJson/", StorageGeoJson.as_view(), name="StorageGeoJson"),
]
