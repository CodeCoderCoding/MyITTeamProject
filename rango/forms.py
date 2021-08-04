from django import forms
from django.contrib.auth.models import User
from rango.models import Scenery, City, UserLikedCity, UserLikedScenery, UserProfile


# We could add these forms to views.py, but it makes sense to split them off into their own file.

# have errors, need update
class UserLikedCityForm(forms.ModelForm):
    name = forms.CharField(max_length=City.NAME_MAX_LENGTH, help_text="Please enter the city name.")
    user = forms.CharField(widget=forms.HiddenInput(), initial=User.username)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    intro = forms.CharField(help_text="Please enter the city intro.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserLikedCity
        fields = ('name', 'intro', 'user')

# have errors, need update
class UserLikedSceneryForm(forms.ModelForm):
    title = forms.CharField(max_length=Scenery.TITLE_MAX_LENGTH, help_text="Please enter the title of the scenery.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the scenery.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = UserLikedScenery
        exclude = ('city',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)