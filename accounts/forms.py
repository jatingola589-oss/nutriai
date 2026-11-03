from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            'full_name',
            'gender',
            'date_of_birth',
            'height',
            'weight',
            'activity_level',
            'disability',
            'accessibility_needs',
            'health_conditions',
            'food_allergies',
            'dietary_preference',
            'health_goal',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'accessibility_needs': forms.Textarea(
                attrs={'rows': 3}
            ),
            'health_conditions': forms.Textarea(
                attrs={'rows': 3}
            ),
            'food_allergies': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

