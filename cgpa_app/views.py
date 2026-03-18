from django.shortcuts import redirect, render

from .forms import CGPAForm


def cgpa_input_view(request):
	if request.method == 'POST':
		form = CGPAForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			total_marks = form.cleaned_data['total_marks']
			cgpa = total_marks / 50

			request.session['cgpa_result'] = {
				'name': name,
				'total_marks': total_marks,
				'cgpa': round(cgpa, 2),
			}
			return redirect('cgpa-result')
	else:
		form = CGPAForm()

	return render(request, 'cgpa_app/page1.html', {'form': form})


def cgpa_result_view(request):
	result = request.session.get('cgpa_result')
	if not result:
		return redirect('cgpa-input')
	return render(request, 'cgpa_app/page2.html', {'result': result})

# Create your views here.
