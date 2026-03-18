from django.shortcuts import render

from .forms import VoteForm
from .models import VoteCount


def _ensure_options_exist():
	for option in ['good', 'satisfactory', 'bad']:
		VoteCount.objects.get_or_create(option=option)


def _result_rows():
	records = {item.option: item.votes for item in VoteCount.objects.all()}
	total = sum(records.values())
	rows = []
	for key, label in [('good', 'Good'), ('satisfactory', 'Satisfactory'), ('bad', 'Bad')]:
		count = records.get(key, 0)
		percentage = (count * 100 / total) if total else 0
		rows.append({'label': label, 'count': count, 'percentage': percentage})
	return rows


def vote_view(request):
	_ensure_options_exist()
	if request.method == 'POST':
		form = VoteForm(request.POST)
		if form.is_valid():
			choice = form.cleaned_data['choice']
			vote = VoteCount.objects.get(option=choice)
			vote.votes += 1
			vote.save(update_fields=['votes'])
			return render(
				request,
				'voting_app/vote.html',
				{'form': VoteForm(), 'results': _result_rows(), 'voted': True},
			)
	else:
		form = VoteForm()

	return render(request, 'voting_app/vote.html', {'form': form, 'results': _result_rows()})

# Create your views here.
