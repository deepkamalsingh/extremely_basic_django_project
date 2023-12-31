from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data 
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title',f"{title} is already taken.")
        return data 

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        data = self.cleaned_data 
        if data.get('title') == "erwr":
            # this can be interpreted as field error.
            self.add_error('title','this is not a valid title.')
            # this can be interpreted as form error.
            raise forms.ValidationError("no erwr god damn.")
