from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from .forms import PickupForm
from .models import Item, Facility
import threading


# Create your views here.
base_template = 'base.html'


class EmailThread(threading.Thread):  # TODO look into celery
    def __init__(self, subject, text_content, html_content, to):
        self.subject = subject
        self.text_content = text_content
        self.html_content = html_content
        self.to = to
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(subject=self.subject, body=self.text_content, to=self.to)
        msg.attach_alternative(self.html_content, "text/html")
        msg.send()


def homepage(request):
    context = {'base_template': base_template,
               'active_navbar': 'homepage'}
    return render(request, 'homepage.html', context)


def lost_item(request):
    context = {'base_template': base_template,
               'active_navbar': 'lost_item'}
    return render(request, 'lost_item.html', context)


def found_item(request):
    if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
            facility_id = request.POST['facility']
            facility = Facility.objects.get(pk=facility_id)
            item_description = request.POST['item_description']
            additional_information = request.POST['additional_information']

            new_item = Item(facility=facility,
                            item_description=item_description,
                            additional_information=additional_information)
            new_item.save()

            email_subject = facility.name
            email_text_template = get_template('email.txt')
            email_html_template = get_template('email.html')
            email_context = Context({'item': new_item})
            email_text_content = email_text_template.render(email_context)
            email_html_content = email_html_template.render(email_context)
            email_send_to = ['colonial.carriers@gmail.com']
            
            email_thread = EmailThread(email_subject, email_text_content, email_html_content, email_send_to)
            email_thread.start()

            request.session["item_pk"] = new_item.pk
            return HttpResponseRedirect(reverse('found_item_confirmed'))
    else:
        form = PickupForm()
    context = {'base_template': base_template,
               'active_navbar': 'found_item',
               'form': form}
    return render(request, 'found_item.html', context)


def found_item_confirmed(request):
    try:
        item_pk = request.session["item_pk"]
        del request.session["item_pk"]
        item = Item.objects.get(pk=item_pk)
        context = {'base_template': base_template,
                   'active_navbar': 'found_item',
                   'item': item}
        return render(request, 'found_item_confirmed.html', context)
    except KeyError:
        return HttpResponseRedirect(reverse('found_item'))


def partners(request):
    facility_list = Facility.objects.all()
    context = {'base_template': base_template,
               'active_navbar': 'partners',
               'facilityList': facility_list}
    return render(request, 'partners.html', context)


def terms(request):
    context = {'base_template': base_template}
    return render(request, 'terms.html', context)


def privacy(request):
    context = {'base_template': base_template}
    return render(request, 'privacy_policy.html', context)
