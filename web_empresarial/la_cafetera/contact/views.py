from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    contact_form = ContactoForm()

    if request.method == 'POST':
        contact_form = ContactoForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            contenido = request.POST.get('contenido', '')
            # Enviando email de confirmacion

            email = EmailMessage(
                "La cafetera: confirmacion de registro",
                "De {} <{}>\n\n{}".format(name, email, contenido),
                "no-contestar@inbox.mailtrap.io",
                ["info@ecuadorvertical.com"],
                reply_to=[email],
            )

            try:
                email.send()
                # Todo ha ido bien redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            


    return render(request, "contact/contacto.html", {'form':contact_form})
