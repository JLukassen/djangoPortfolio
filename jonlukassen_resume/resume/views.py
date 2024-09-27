from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactFormModelForm
from .models import ContactInfo
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
            message = f"""
            Name: {form_data.name}
            Email: {form_data.email}
            Phone: {form_data.phone}
            Job Description: {form_data.job_description}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['your-email@outlook.com']  # Replace with your email

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('resume_contact')  # Redirect after form submission

    return render(request, 'resume/resume_contact.html', {'contact': contact, 'form': form})

def contact_form(request):
    return render(request, 'resume/contact_info.html')  # Make sure the template exists