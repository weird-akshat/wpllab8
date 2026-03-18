from django import forms


class VoteForm(forms.Form):
    CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad'),
    ]
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
