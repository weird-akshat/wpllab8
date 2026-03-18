from django.shortcuts import redirect, render

from .forms import FeedbackForm


def feedback_view(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			request.session['feedback_name'] = form.cleaned_data['name']
			return redirect('feedback-thanks')
	else:
		form = FeedbackForm()

	return render(request, 'feedback_app/feedback.html', {'form': form})


def thanks_view(request):
	name = request.session.get('feedback_name')
	if not name:
		return redirect('feedback-form')
	return render(request, 'feedback_app/thanks.html', {'name': name})

# Create your views here.
