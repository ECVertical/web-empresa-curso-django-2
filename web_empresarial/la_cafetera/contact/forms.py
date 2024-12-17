from django import forms

class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
        ), min_length=5, max_length=50)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
        ), min_length=6, max_length=50) 
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje' }
        ), min_length=10, max_length=700)  

