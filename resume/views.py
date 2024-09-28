from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactFormModelForm
from .models import ContactInfo
from django.conf import settings
from django.contrib import messages

def resume_contact(request):
    contact = ContactInfo.objects.first()  # Assuming there's only one contact info record
    form = ContactFormModelForm()

    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form_data = form.save()  # Save the form data to the database

            # Prepare email details
            mail_to_send_to = "jonlukassen@gmail.com"  # The email address to send to
            from_email = settings.DEFAULT_FROM_EMAIL  # Email address to send from
            subject = "New Contact Form Submission"  # Email subject

            # Build the email message body
            message = f"""
            Name: {form_data.name}
            Email: {form_data.email}
            Phone: {form_data.phone}
            Job Description: {form_data.job_description}
            Message: {form_data.message}
            """

            # Reply-To header for the recipient to reply to the sender
            headers = {
                'Reply-To': form_data.email,
            }

            try:
                # Send email
                send_mail(
                    subject,        # Email subject
                    message,        # Message body
                    from_email,     # Sender email
                    [mail_to_send_to],  # Recipient email
                    fail_silently=False,
                    headers=headers  # Reply-to address
                )
                messages.success(request, 'Message was sent, you can send another one.')
            except Exception as e:
                messages.error(request, 'Message wasn’t sent, please try again later.')
                print(f"Error sending email: {e}")

            return redirect('resume_contact')  # Redirect after form submission to clear the form

    return render(request, 'resume/resume_contact.html', {'contact': contact, 'form': form})
