from django import forms
from .models import CropData

# Define the choices for soil types and crops
SOIL_CHOICES = [
    ('soil1', 'Soil 1'),
    ('soil2', 'Soil 2'),
    # Add more soil types as needed
]

CROP_CHOICES = [
    ('crop1', 'Crop 1'),
    ('crop2', 'Crop 2'),
    # Add more crop types as needed
]

class CropSoilForm(forms.ModelForm):
    class Meta:
        model = CropData
        fields = ['region', 'soil', 'previous']
        

class QuestionnaireForm(forms.Form):
    area = forms.CharField(label='Area/Region', max_length=100)
    soil_type = forms.ChoiceField(label='Soil Type', choices=SOIL_CHOICES)
    soil_test_conducted = forms.BooleanField(label='Have you conducted a soil test?', required=False)
    primary_crop = forms.ChoiceField(label='Primary Crop', choices=CROP_CHOICES)
    secondary_crop = forms.ChoiceField(label='Secondary Crop', choices=CROP_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        primary_crop = cleaned_data.get('primary_crop')
        secondary_crop = cleaned_data.get('secondary_crop')

        if not primary_crop or not secondary_crop:
            raise forms.ValidationError('Please select both a primary and secondary crop.')
        return cleaned_data