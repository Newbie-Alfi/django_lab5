from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")
    age=forms.IntegerField()
    email=forms.EmailField(label="Электронный адрес")
    text=forms.URLField(label="Введите URL")
    file_path=forms.FilePathField(label="Выберите файл", path="/")
    ifile=forms.FileField(label="Файл")