from django import forms

class NameForm(forms.Form):
    search = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
        'class':'search',
        'placeholder':'Search..'
        }))

class NewPageForm(forms.Form):
    page_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
        'class':'title',
        'placeholder':'Title..'
        }))
    page_content = forms.CharField(label='', widget=forms.Textarea(
        attrs={
        'class':'description',
        'placeholder':'Description..'
        }))

class EditPageForm(forms.Form):
    page_edit_content = forms.CharField(label='', widget=forms.Textarea)
