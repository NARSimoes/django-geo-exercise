
"""
    Register the celery tasks!
"""

from celery.task import task
from celery.utils.log import get_task_logger

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from .models import Storage

logger = get_task_logger(__name__)


@task(name="get_distances_from_user_point_task")
def get_distances_from_user_point_task(x, y, operation_type, initial_filter, last_filter):
    """Task to compute distance between user location and our storage data.
    We are returning json because celery is using serializer=json."""
    user_location = Point(x, y, srid=4326)
    if operation_type == "nearest":
        queryset = Storage.objects.annotate(distance=Distance('point', user_location)).order_by(
                                            'distance')[initial_filter:last_filter]
    else:
        queryset = Storage.objects.annotate(distance=Distance('point', user_location)).order_by(
                                            'distance').reverse()[initial_filter:last_filter]

    distances = []
    for i in queryset:
        distances.append({"id": i.id, "distance": round(i.distance.m/1000., 4)})  # m to km

    return distances

