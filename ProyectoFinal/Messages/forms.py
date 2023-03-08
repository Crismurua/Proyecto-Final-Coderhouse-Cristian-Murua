from django import forms

class MessageForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea(attrs = {

			"class": "form_ms",
			"placeholder":"Message..."

		}))