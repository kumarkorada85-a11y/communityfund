from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from .models import Donation

import razorpay


client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)


def home(request):

    if request.method == "POST":

        name = request.POST.get('name')
        amount = request.POST.get('amount')

        Donation.objects.create(
            name=name,
            amount=amount
        )

        return redirect('/')

    return render(request, 'index.html')


def donations(request):

    donations = Donation.objects.all()

    return render(request, 'donations.html', {
        'donations': donations
    })


def collection(request):

    donations = Donation.objects.all()

    total = 0

    for donation in donations:
        total += donation.amount

    return render(request, 'collection.html', {
        'total': total
    })


def create_order(request):

    if request.method == "POST":

        amount = int(request.POST.get("amount")) * 100

        payment = client.order.create({

            "amount": amount,

            "currency": "INR",

            "payment_capture": "1"

        })

        return JsonResponse(payment)