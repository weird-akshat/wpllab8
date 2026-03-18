from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			request.session['register_data'] = {
				'username': form.cleaned_data['username'],
				'email': form.cleaned_data.get('email', ''),
				'contact_number': form.cleaned_data.get('contact_number', ''),
			}
			return redirect('register-success')
	else:
		form = RegisterForm()

	return render(request, 'register_app/register.html', {'form': form})


def success_view(request):
	data = request.session.get('register_data')
	if not data:
		return redirect('register')

	return render(request, 'register_app/success.html', {'data': data})

# Create your views here.
