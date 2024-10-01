from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactFormModelForm
from .models import ContactInfo
from django.conf import settings
from django.contrib import messages
from django.http import FileResponse
import os
from django.core.mail import send_mail

def resume_contact(request):
    contact = ContactInfo.objects.first()  # Assuming there's only one contact info record
    form = ContactFormModelForm()

    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form_data = form.save()  # Save the form data to the database

            if send_contact_email(form_data):
                messages.success(request, 'Message was sent, you can send another one.')
            else:
                messages.error(request, 'Message wasn’t sent, please try again later.')
            
            return redirect('resume_contact')  # Redirect after form submission to clear the form

    return render(request, 'resume/resume_contact.html', {'contact': contact, 'form': form})
    
def send_contact_email(form_data):
    mail_to_send_to = "jlukassen@jonlukassen.com"
    subject = "New Contact Form Submission"

    # Build the email message body
    message = f"""
    Name: {form_data.name}
    Email: {form_data.email}
    Phone: {form_data.phone}
    Message: {form_data.message}
    """

    # Create an EmailMessage object
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['recipient@example.com'],  # Recipient email
        reply_to=[form_data.email],  # Reply-To header
    )
    try:
        email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    
    if form.is_valid():
        form_data = form.save()
        if send_contact_email(form_data):
            messages.success(request, 'Message was sent, you can send another one.')
        else:
            messages.error(request, 'Message wasn’t sent, please try again later.')
        return redirect('resume_contact')
        
def download_resume(request):
        # Define the file path
    file_path = os.path.join(settings.STATIC_ROOT, 'resume/LukassenJonathanResume.pdf')

        # Serve the file
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='LukassenJonathanResume.pdf')
