from django import forms


class BillingForm(forms.Form):
    BRANDS = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]

    ITEMS = [
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
    ]

    brand = forms.ChoiceField(choices=BRANDS, widget=forms.RadioSelect, required=True)
    items = forms.MultipleChoiceField(
        choices=ITEMS, widget=forms.CheckboxSelectMultiple, required=True
    )
    quantity = forms.IntegerField(min_value=1, required=True)
