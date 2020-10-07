from django import forms
from .models import FormularioIncripcion

 
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = FormularioIncripcion
        fields = ['curso',
         'cedula',
         'archivo_cedula', 
         'nombres',
         'apellidos',
         'profesion',
         'nivel_academico',
         'estado',
         'municipio',
         'direccion',
         'telefono',
         'telefono_local',
         'correo_electronico',
         'curriculum']
        widgets = {
            'curso': forms.Select(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Cedula'
					}
				),

            'cedula': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Cedula'
					}
				),

            'archivo_cedula': forms.FileInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Cedula'
					}
				), 

           'nombres': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar nombres'
					}
				),



           'apellidos': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar apellidos'
					}
				),  

           'profesion': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar profesion'
					}
				),


           'nivel_academico': forms.Select(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Nivel Academico'
					}
				), 



           'estado': forms.Select(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Estado'
					}
				), 



           'municipio': forms.Select(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Municipio'
					}
				), 


           'direccion': forms.Textarea(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Dirección'
					}
				),


            'telefono': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar telefono celular'
					}
				),

            'telefono_local': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar telefono local'
					}
				),   

            'correo_electronico': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Ingresar Correo Electronico'
					}
				),

             'curriculum': forms.FileInput(
				attrs={
					'class': 'form-control',
                    'placeholder': ' Curriculum'
					}
				),                                         


			}


