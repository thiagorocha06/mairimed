class AnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        exclude = ['']
        widgets = {
            'field1': RadioSelect(choices=CHOICES, attrs={'required': 'True'}),
            'field2': HiddenInput,
            }
