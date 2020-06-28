
"""
    NOTE: This was used when I developed the exercise with two databases.
    Instead this is not used anymore, I left this is here just to explain
    how I to deal with database routers.

    dbrouters is a router for databases:
    - Storage or OperationExercise models save/write data in the "geo" Database
"""

from .models import Storage, OperationExercise


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading Storage or OperationExercise models from geo """
        if model == Storage or model == OperationExercise:
            return 'geo'
        return None

    def db_for_write(self, model, **hints):
        """ writing Storage or OperationExercise to geo """
        if model == Storage or model == OperationExercise:
            return 'geo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in "exercises" or \
                obj2._meta.app_label in "exercises":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in "exercises":
            return db == 'geo'
        return None
