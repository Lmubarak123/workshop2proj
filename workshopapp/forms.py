from django import forms
from multiselectfield import MultiSelectFormField
class Feedbackform(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'YOur your name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'YOur rating'
                'required'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'YOur FeedBack'
            }
        )
    )
class Equairyform(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter your Email",
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your Moblie",
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Mobile'
            }
        )
    )

    Gender_choice=(
        ('M','Male'),
        ('F','Female')
    )

    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_choice
    )


    COURSE_CHOICES = (
        ('PY', 'python'),
        ('DJ', 'django'),
        ('RA', 'restapi'),
        ('FL', 'flask'),
        ('UI', 'ui')
    )

    courses = MultiSelectFormField(choices=COURSE_CHOICES)

    SHIFTS_CHOICES = (
        ('Morning', 'Morning shift'),
        ('Afternoon', 'Afternoon shift'),
        ('Evening', 'Evening shift'),
        ('Night', 'Night shift'))
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES)

    start_date=forms.DateField(
        widget=forms.SelectDateWidget())