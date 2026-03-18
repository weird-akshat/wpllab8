from django import forms


class FeedbackForm(forms.Form):
    COURSES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix', 'Unix'),
        ('C', 'C'),
        ('C++', 'C++'),
    ]

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15, required=True)
    course = forms.ChoiceField(choices=COURSES, required=True)
    comments = forms.CharField(widget=forms.Textarea, required=False)
