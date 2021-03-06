from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import get_template


from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
                messages.success(
                    request, "Thank you for your email. Please expect a response from me as soon as possible.")
                contact_name = request.POST.get(
                    'contact_name', '')
                contact_email = request.POST.get(
                    'contact_email', '')
                form_content = request.POST.get('content', '')
                # Email the profile with the
                # contact information
                template = get_template('contact/confirmation_sent_email/contact_template.txt')
                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                }
                content = template.render(context)

                email = EmailMessage(
                    "New contact form submission",
                    content, "Your website" + '',
                    ['youremail@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                email.send()
                return redirect('contact')

    return render(request, 'contact/email.html', {
        'form': form_class,
    })
