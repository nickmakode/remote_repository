from django import forms

class FeedbackForm(forms.Form):

    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'forms-control',
                'placeholder':'your name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'forms-control',
                'placeholder': 'your rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'forms-control',
                'placeholder': 'your feedback'
            }
        )
    )
    date = forms.DateTimeField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'forms-control',
                'placeholder': 'your name'
            }
        )
    )
