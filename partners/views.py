from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from .forms import PickupForm
from .models import Item, Facility


# Create your views here.
base_template = 'base.html'


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

            notify_by_email(new_item)

            request.session["item_pk"] = new_item.pk
            return HttpResponseRedirect(reverse('found_item_confirmed'))
    else:
        form = PickupForm()
    context = {'base_template': base_template,
               'active_navbar': 'found_item',
               'form': form}
    return render(request, 'found_item.html', context)


def notify_by_email(item):
    text_template = get_template('email.txt')
    html_template = get_template('email.html')

    context = Context({'item': item})

    text_content = text_template.render(context)
    html_content = html_template.render(context)

    msg = EmailMultiAlternatives(subject=item.facility.name, body=text_content, to=['colonial.carriers@gmail.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return


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