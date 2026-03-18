from django.shortcuts import redirect, render

from .forms import BillingForm

PRICES = {
	'Mobile': 15000,
	'Laptop': 50000,
}


def order_view(request):
	if request.method == 'POST':
		form = BillingForm(request.POST)
		if form.is_valid():
			brand = form.cleaned_data['brand']
			items = form.cleaned_data['items']
			quantity = form.cleaned_data['quantity']

			rows = []
			total = 0
			for item in items:
				amount = PRICES[item] * quantity
				rows.append({'item': item, 'rate': PRICES[item], 'quantity': quantity, 'amount': amount})
				total += amount

			request.session['bill_data'] = {
				'brand': brand,
				'rows': rows,
				'total': total,
			}
			return redirect('billing-bill')
	else:
		form = BillingForm()

	return render(request, 'billing_app/order.html', {'form': form})


def bill_view(request):
	bill_data = request.session.get('bill_data')
	if not bill_data:
		return redirect('billing-order')

	return render(request, 'billing_app/bill.html', {'bill': bill_data})

# Create your views here.
