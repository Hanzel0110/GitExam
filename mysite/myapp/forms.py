from django import forms
from myapp.models import Course

class updateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"