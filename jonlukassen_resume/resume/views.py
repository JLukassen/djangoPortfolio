from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import ContactInfo
from .forms import ContactFormModelForm
from django.conf import settings


def resume_contact(request):
    contact = ContactInfo.objects.first()  # Assuming there's only one contact info record
    form = ContactFormModelForm()

    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form_data = form.save()  # Save the form data to the database

            # Send email notification
            subject = "New Contact Form Submission"
            message = f"Name: {form_data.name}\nEmail: {form_data.email}\nPhone: {form_data.phone}\nJob Description: {form_data.job_description}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['jonlukassen@outlook.com']  # Replace with your email

            send_mail(subject, message, from_email, recipient_list)

            return redirect('resume_contact')  # Redirect to avoid re-submission

    return render(request, 'resume/resume_contact.html', {'contact': contact, 'form': form})
