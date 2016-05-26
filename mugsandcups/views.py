from django.shortcuts import render
from .models import Testimonial, Catalog, Feature
from mugsandcups.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
# Create your views here.

def index(request):
    testimonials = Testimonial.objects.all
    Features = Feature.objects.all()[:6]
    context = {
        'testimonials': testimonials,
        'Features': Features,
    }
    return render(request, 'mugsandcups/index.html', context)

def catalog(request):
    catalogs = Catalog.objects.all
    return render(request, 'mugsandcups/catalog.html', {'catalogs': catalogs})

def about(request):
    return render(request, 'mugsandcups/about.html')

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('mugsandcups/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, 'mugsandcups/contact.html', {'form': form_class,})