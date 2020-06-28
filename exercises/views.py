
"""
    Exercise views:
    - exercise_description_view with the exercise description
    - exercise_view with the exercise
    - StorageGeoJson used to visualize points in the database
"""

import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.serializers import serialize
from django.forms.utils import ErrorList

from .forms import ExerciseForm
from .models import Exercises, Storage


logger = logging.getLogger(__name__)


def exercise_list_view(request):
    """Can be used if we want multiples exercises!"""
    queryset = Exercises.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "exercises/exercise_list.html", context)


def exercise_description_view(request, *args, **kwargs):
    my_context = {
        "title": "Exercise Description",
        "this_is_true": True,
    }

    return render(request, "exercises/exercise_description.html", my_context)


def exercise_view(request, *args, **kwargs):
    form = ExerciseForm(request.POST or None, error_class=DivErrorList)
    queryset = None
    coord_geojson = None

    # is the form valid?
    if form.is_valid():
        logger.debug("The form is valid ", form)
        # yes, let's get the distance between user location (inserted x,y values)
        # and our storage. This will get compute async using task (celery)
        queryset = form.get_distances_from_user_point()
        form.save()  # Save inserted in database

    my_context = {
        'form': form,
        'result': queryset,
        'geojson': coord_geojson
    }

    return render(request, "exercises/exercise.html", my_context)


class StorageGeoJson(View):
    """View to serialize initial points stored in the database (id, x, y) to GeoJson.
    Than, we can visualize the that points in the map!"""
    def get(self, request):
        geojson = serialize(
            'geojson',
            Storage.objects.all(),
            geometry_field='point',
            fields=('id', 'point')
        )
        return HttpResponse(geojson)


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        style = "color:red; font-size: 12px; font-style: italic;"
        if not self:
            return ''
        return '<div class="errorlist" style=' + style + '>%s</div>' % ''.join(
            ['<div class="error" style=' + style + '>%s</div>' % e for e in self]
        )
