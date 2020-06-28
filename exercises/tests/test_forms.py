
from exercises.models import OperationExercise
from exercises.forms import ExerciseForm
from django.test import TestCase


class ExerciseFormTest(TestCase):
    """Simple positive test case to test Model: OperationExercise!"""
    databases = {'default'}

    def create_model(self, x, y, num_points, operation_type):
        """Auxiliary to create model!"""
        return OperationExercise.objects.create(x=x, y=y, num_points=num_points, operation_types=operation_type)

    def test_valid_nearest_form(self):
        m = self.create_model(12.4, 12.5, 4, "nearest")
        data = {'x': m.x, 'y': m.y, 'num_points': m.num_points, 'operation_types': m.operation_types}
        form = ExerciseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_furthest_form(self):
        m = self.create_model(12.4, 12.5, 4, "furthest")
        data = {'x': m.x, 'y': m.y, 'num_points': m.num_points, 'operation_types': m.operation_types}
        form = ExerciseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_gt_max_x_form(self):
        """Test with invalid - > max limit x!"""
        data = {'x': 184, 'y': 12.5, 'num_points': 4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_gt_max_y_form(self):
        """Test with invalid - > max limit y!"""
        data = {'x': 12, 'y': 94, 'num_points': 4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_lt_min_x_form(self):
        """Test with invalid - < min limit x!"""
        data = {'x': -184, 'y': 12.5, 'num_points': 4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_lt_min_y_form(self):
        """Test with invalid - < min limit y!"""
        data = {'x': 12, 'y': -94, 'num_points': 4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_negative_num_points_form(self):
        """Test with invalid - -num_points!"""
        data = {'x': 12, 'y': 12.5, 'num_points': -4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_wrong_chars_form(self):
        """Test with invalid - wrong chars!"""
        data = {'x': "#!ola", 'y': 12.5, 'num_points': -4, 'operation_types': 'nearest'}
        form = ExerciseForm(data=data)
        self.assertFalse(form.is_valid())
