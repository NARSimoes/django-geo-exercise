

from django.test import TestCase
from django.urls import reverse
from exercises.models import OperationExercise
from django.test import TestCase


class ExercisesViewTest(TestCase):
    """Simple positive test case to test Model: OperationExercise!"""
    databases = {'default'}

    def create_model(self, x, y, num_points, operation_type):
        return OperationExercise.objects.create(x=x, y=y, num_points=num_points, operation_types=operation_type)

    def test_exercise_view(self):
        m = self.create_model(12.4, 12.5, 4, "nearest")
        url = reverse("exercise_description_view")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


