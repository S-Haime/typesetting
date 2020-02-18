from django import forms

from plugins.typesetting import models
from utils.forms import HTMLDateInput


class AssignTypesetter(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        typesetters = kwargs.pop('typesetters')
        files = kwargs.pop('files')
        self.rounds = kwargs.pop('rounds')
        super(AssignTypesetter, self).__init__(*args, **kwargs)

        self.fields['typesetter'].queryset = typesetters
        self.fields['files_to_typeset'].queryset = files

    class Meta:
        model = models.TypesettingAssignment
        fields = (
            'typesetter',
            'due',
            'task',
            'files_to_typeset',
        )

        widgets = {
            'due': HTMLDateInput(),
        }

    def save(self, commit=True):
        assignment = super(AssignTypesetter, self).save(commit=False)
        assignment.round = self.rounds[0]

        if commit:
            assignment.save()

            for file in self.cleaned_data.get('files_to_typeset'):
                assignment.files_to_typeset.add(file)

        return assignment


def decision_choices():
    return (
        ('accept', 'Accept'),
        ('decline', 'Decline'),
    )


class TypesetterDecision(forms.Form):
    decision = forms.ChoiceField(choices=decision_choices(), required=True)
    note = forms.CharField(widget=forms.Textarea, required=False)