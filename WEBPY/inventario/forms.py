from django import forms
from .models import Usuario,Bien
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import UnidadOrganica,Sede,Estado,Rol,TipoBien


class RegistroForm(UserCreationForm):
    nombres = forms.CharField(label='Nombres')
    apellidos = forms.CharField(label='Apellidos')
    email = forms.EmailField(max_length=255)
    dni = forms.CharField(max_length=88)
    unidadOrganica = forms.ModelChoiceField(queryset=UnidadOrganica.objects.all(), required=False)
    sede = forms.ModelChoiceField(queryset=Sede.objects.all(), required=False)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=False)
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=False)
    
    
    class Meta:
        model = Usuario 
        fields = ['nombres','apellidos','dni','unidadOrganica','sede','estado','rol','username']  # Customize fields

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
    
    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.nombres = self.cleaned_data['nombres']
        user.apellidos = self.cleaned_data['apellidos']
        user.email = self.cleaned_data['email']
        user.dni = self.cleaned_data['dni']
        user.unidadOrganica = self.cleaned_data['unidadOrganica']
        user.sede = self.cleaned_data['sede']
        user.estado = self.cleaned_data['estado']
        user.rol = self.cleaned_data['rol']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Usuario o contraseña incorrectos.')
            elif not user.is_active:
                raise forms.ValidationError('Este usuario está inactivo.')
        
        return cleaned_data

class RegistroBienForm(forms.Form):
    tipoBien = forms.ModelChoiceField(queryset=TipoBien.objects.all(), required=False, label='Tipo de Bien')
    ordenCompra = forms.CharField(label='Orden de Compra')
    proveedor = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    serie = forms.CharField(max_length=20)
    fechaVenGarantia = forms.CharField(max_length=20,label='Fecha Vencimiento Garantia')
    componentes = forms.CharField(max_length=50)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=False)
    class Meta:
        model = Bien  # Use your custom user model if applicable
        fields = ['tipoBien','ordenCompra','proveedor','marca','modelo','serie','fechaVenGarantia',
                  'componentes','estado']  # Customize fields

    def __init__(self, *args, **kwargs):
        super(RegistroBienForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
    
    def save(self, commit=True):
        user = super(RegistroBienForm, self).save(commit=False)
        user.tipoBien = self.cleaned_data['tipoBien']
        user.ordenCompra = self.cleaned_data['ordenCompra']
        user.proveedor = self.cleaned_data['proveedor']
        user.marca = self.cleaned_data['marca']
        user.modelo = self.cleaned_data['modelo']
        user.serie = self.cleaned_data['serie']
        user.fechaVenGarantia = self.cleaned_data['fechaVenGarantia']
        user.componentes = self.cleaned_data['componentes']
        user.estado = self.cleaned_data['estado']
        if commit:
            user.save()
        return user
