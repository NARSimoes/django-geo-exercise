
"""
    Exercise Forms:
    - ExerciseForm: filled by user in frontend
    - Storage: model is populated by management command
"""

import json

from django import forms

from .models import OperationExercise
from .tasks import get_distances_from_user_point_task


class ExerciseForm(forms.ModelForm):
    x = forms.DecimalField(
        max_digits=9,
        decimal_places=6,
        min_value=-180,
        max_value=180,
        required=True,
        label="X",
        widget=forms.TextInput(attrs={"placeholder": "Insert X value!"}))

    y = forms.DecimalField(
        max_digits=9,
        decimal_places=6,
        min_value=-90,
        max_value=90,
        required=True,
        label="Y",
        widget=forms.TextInput(attrs={"placeholder": "Insert Y value!"}))

    num_points = forms.IntegerField(
        required=True,
        label="Number of points to be returned!",
        widget=forms.TextInput(attrs={"placeholder": "Insert number of points!"}))

    class Meta:
        model = OperationExercise
        fields = [
            'x',
            'y',
            'num_points',
            'operation_types'
        ]

    def get_distances_from_user_point(self):
        """Calling task from celery.delay in order to run queryset asynchronously."""
        return get_distances_from_user_point_task(
            float(self.cleaned_data["x"]),
            float(self.cleaned_data["y"]),
            self.cleaned_data["operation_types"],
            0,
            self.cleaned_data["num_points"]
        )
