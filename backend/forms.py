from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    
    #     fields = ['nombre', 'pregunta_1', 'pregunta_2', 'pregunta_3', 'pregunta_4', 'pregunta_5', 'pregunta_6', 'pregunta_7', 'pregunta_8', 'pregunta_7', 'pregunta_10', 'pregunta_11', 'pregunta_12', 'pregunta_13', 'pregunta_14', 'pregunta_15']

    pregunta_9 = [
        ('limitada', 'limitada'),
        ('versatil', 'versatil'),
    ]

    pregunta_10 = [
        ('inutil' , 'inutil'),
        ('util' , 'util'),
    ]

    pregunta_11 = [
        ('pesada' , 'pesada'),
        ('ligero' , 'ligero'),
    ]

    pregunta_12 = [
        ('debil' , 'debil'),
        ('resistente' , 'resistente'),
    ]

    pregunta_13 = [
        ('debil', 'debil'),
        ('intenso' , 'intenso'),
    ]

    pregunta_14 = [
        ('complicado' , 'complicado'),
        ('sencillo' , 'sencillo'),
    ]

    pregunta_15 = [
        ('poco atractiva', 'poco atractiva'),
        ('muy atractiva', 'muy atractiva'),
    ]

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'nombre-input'}))
    
    OPCIONES = [(str(i), str(i)) for i in range(1, 6)]
    
    pregunta_1 = forms.ChoiceField(
        choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿La lámpara permite ajustar fácilmente las tonalidades de la luz (cálida, fría y neutra)?"
    )

    pregunta_2 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="Cree que los tonos verdes usados para el diseño de la lámpara sean los adecuados para esta y el ambiente donde sera utilizada?")

    pregunta_3 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿El tamaño de la lámpara se le hace adecuado para llevarla a camping?")

    pregunta_4 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿El aro facilita que la lámpara sea colocada en distintos lugares?")

    pregunta_5 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿El agarre se adapta adecuadamente a la mano y es cómodo?")

    pregunta_6 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿La lámpara es fácil de transportar?")

    pregunta_7 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿La lampara emite luz de manera uniforme y sin zonas oscuras?")

    pregunta_8 = forms.ChoiceField(choices=OPCIONES,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        label="¿La lampara cumple con sus expectativas para usarla en camping?")

    pregunta_9 = forms.ChoiceField(
        choices=pregunta_9, 
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}), 
        label="¿Como es la adpatabilidad de las tonalidades de la Luz?")

    pregunta_10 = forms.ChoiceField(choices=pregunta_10,
                                    widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}), 
                                    label="¿ que tan útil le parece el cambio de las tonalidades de la luz ( neutra, calida y fría)?")

    pregunta_11 = forms.ChoiceField(choices= pregunta_11, 
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}),
        label='¿como considera el peso de la lampara?')

    pregunta_12 = forms.ChoiceField(choices= pregunta_12, 
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}),
        label='¿que tan resistente considera que sera la lampara?')

    pregunta_13 = forms.ChoiceField(choices= pregunta_13, 
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}),
        label='¿Como le parece el brillo de la luz?')

    pregunta_14 = forms.ChoiceField(choices= pregunta_14, 
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}),
        label='¿Como le parece la facilidad de uso de la lampara?')

    pregunta_15 = forms.ChoiceField(
        choices=pregunta_15,
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}),
        label='¿Cómo le parece la estética del diseño?'
    )

    class Meta:
        model = Formulario

        fields = '__all__'
