
"""
    Exercise models:
    - OperationExercise: model to be filled by user in frontend
    - Storage: model populated by management command
"""

import logging

from django.contrib.gis.db import models


logger = logging.getLogger(__name__)


class Exercises(models.Model):
    """Can be used if we want more exercises in furthers devs!"""
    name = models.CharField(max_length=120)


class OperationExercise(models.Model):
    id = models.IntegerField(primary_key=True),
    x = models.DecimalField(max_digits=9, decimal_places=6)
    y = models.DecimalField(max_digits=9, decimal_places=6)
    num_points = models.PositiveIntegerField("Number of points to be returned")
    # operations
    operations = (
        ('nearest', 'Nearest'),
        ('furthest', 'Furthest')
    )
    operation_types = models.CharField(max_length=12, choices=operations, default='nearest')

    def get_x(self):
        return float(self.x)

    def get_y(self):
        return float(self.y)

    def __str__(self):
        return "{} id:{} x:'{}' y:'{}' NumPoints:'{}' OperationType:'{}'".format(
            self.__class__.__name__, self.id, self.x, self.y, self.num_points, self.operation_types)


class Storage(models.Model):
    id = models.IntegerField(primary_key=True)
    point = models.PointField()
