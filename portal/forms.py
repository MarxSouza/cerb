from django import forms

class ContatoForm(forms.Form):
	nome = forms.CharField(widget=forms.TextInput(attrs={'id':'name', 'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email', 'class':'form-control'}))
	telefone = forms.IntegerField(widget=forms.TextInput(attrs={'id':'phone','class':'form-control'}))
	assunto = forms.CharField(widget=forms.TextInput(attrs={'id':'name', 'class':'form-control'}))
	mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'class':'form-control'}))