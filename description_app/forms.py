from django import forms

from .models import Child, Skill, ChildSkill


class ChildForm(forms.ModelForm):

    GENDER_CHOICES = [
        ('chłopiec', 'Chłopiec'),
        ('dziewczynka', 'Dziewczynka'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        label="Płeć"
    )

    class Meta:
        model = Child
        fields = ["first_name", "last_name", "gender",]
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
        }

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)

        skills = Skill.objects.all()

        for skill in skills:
            self.fields[f"skill_{skill.id}"] = forms.ChoiceField(
                choices=ChildSkill.GRADE_CHOICES,
                label=skill.name,
                widget=forms.RadioSelect
            )



# class ChildForm(forms.Form):
#     MALE = 'chłopiec'
#     FEMALE = 'dziewczynka'
    
#     GENDER_CHOICES = [
#         (MALE, 'chłopiec'),
#         (FEMALE, 'dziewczynka'),
#     ]
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     gender = forms.ChoiceField(
#         widget=forms.RadioSelect,
#         # choices=GENDER_CHOICES,
#     )