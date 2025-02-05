

from django.shortcuts import render, redirect
from .forms import StudentForm

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to 'success' after successful form submission
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

# Landing page view
def landing_page(request):
    return render(request, 'students/landing.html')  # Make sure the template exists

# success page view
def success(request):
    return render(request, 'students/success.html')  # A success message after form submission





