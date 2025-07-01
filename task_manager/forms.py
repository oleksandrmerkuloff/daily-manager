from django import forms


class GoalForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        initial='Goal Title'
    )
    content = forms.TextInput()
    is_done = forms.BooleanField()


class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        initial='Task Title'
    )
    content = forms.TextInput()
    deadline = forms.DateTimeField()
    status = None #? Choices
    goal = None #! Foreing KEy


class NoteForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        initial='Note Title'
    )
    text = forms.TextInput()
    task = None #! Here will be foreign key
