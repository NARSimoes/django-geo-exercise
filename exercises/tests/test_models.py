
from django.test import TestCase
from exercises.models import OperationExercise


class OperationExerciseTest(TestCase):
    """Simple positive test case to test Model: OperationExercise!"""
    databases = {'default'}

    def create_model(self, operation_id, x, y, num_points, operation_type):
        return OperationExercise.objects.create(id=operation_id, x=x, y=y, num_points=num_points, operation_types=operation_type)

    def test_operation_exercise_creation(self):
        m = self.create_model(1, 12.4, 12.5, 4, "nearest")
        obj = OperationExercise.objects.first()
        self.assertTrue(isinstance(m, OperationExercise))
        self.assertEqual(m.id, obj.id)
        self.assertEqual(m.x, obj.get_x())
        self.assertEqual(m.y, obj.get_y())
        self.assertEqual(m.num_points, obj.num_points)
        self.assertEqual(m.operation_types, obj.operation_types)
