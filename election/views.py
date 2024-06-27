from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import requests


def project1(request):
    if request.method == "POST":
        index_number = request.POST.get('indexNumber', '').strip()
        token = request.POST.get('token', '').strip()

        try:
            voter = voters.objects.get(Index_Number=index_number, Token=token)
            if voter.is_token_used:
                return redirect('Exit Page')  
            else:
                voter.is_token_used = True
                voter.save()
                request.session.flush()
                request.session['current_page'] = 1

                return redirect('Voting page 1')  
        except voters.DoesNotExist:
            messages.error(request, 'Invalid index number or token')

    return render(request, 'project1.html')

def project2(request):
    return render(request, 'project2.html')

def project30(request):
    return render(request, 'project30.html')

def project3(request):
    return render(request, 'project3.html')

def project4(request):
    return render(request, 'project4.html')

def project5(request):
    return render(request, 'project5.html')

def project6(request):
    return render(request, 'project6.html')

def project7(request):
    return render(request, 'project7.html')

def project8(request):
    return render(request, 'project8.html')

def project9(request):
    return render(request, 'project9.html')

def project10(request):
    return render(request, 'project10.html')

def project11(request):
    return render(request, 'project11.html')

def project12(request):
    return render(request, 'project12.html')

def project13(request):
    return render(request, 'project13.html')

def project14(request):
    return render(request, 'project14.html')

def project15(request):
    return render(request, 'project15.html')

def project16(request):
    return render(request, 'project16.html')

def project17(request):
    return render(request, 'project17.html')

def project18(request):
    return render(request, 'project18.html')

def project19(request):
    return render(request, 'project19.html')

def project20(request):
    return render(request, 'project20.html')

def project21(request):
    return render(request, 'project21.html')

def my_view(request):
    # Establish a cursor to interact with the database
    with connection.cursor() as cursor:
        # Execute a SQL query to select all records from the 'voters' table
        cursor.execute("SELECT * FROM voters")
        # Fetch all the rows returned by the query
        rows = cursor.fetchall()
    # Render the template with the data
    return render(request, 'my-view.html', {'rows': rows})
    
    
def cast_vote(request):
    if request.method == "POST":
        candidate_id = request.POST.get('candidate_id')
        candidate = get_object_or_404(candidates, id=candidate_id)
        candidate.Votes += 1
        candidate.save()

        current_page = request.session.get('current_page', 1)
        next_page_number = current_page + 1
        request.session['current_page'] = next_page_number

        if current_page == 1:
            next_page_url = reverse('Voting page 2')
        elif current_page == 2:
            next_page_url = reverse('Voting page 3')
        elif current_page == 3:
            next_page_url = reverse('Voting page 4')
        elif current_page == 4:
            next_page_url = reverse('Voting page 5')
        elif current_page == 5:
            next_page_url = reverse('Voting page 6')
        elif current_page == 6:
            next_page_url = reverse('Voting page 7')
        elif current_page == 7:
            next_page_url = reverse('Voting page 8')
        elif current_page == 8:
            next_page_url = reverse('Voting page 9')
        elif current_page == 9:
            next_page_url = reverse('Voting page 10')
        elif current_page == 10:
            next_page_url = reverse('Voting page 11')
        elif current_page == 11:
            next_page_url = reverse('Voting page 12')
        elif current_page == 12:
            next_page_url = reverse('Voting page 13')
        elif current_page == 13:
            next_page_url = reverse('Voting page 14')
        elif current_page == 14:
            next_page_url = reverse('Voting page 15')
        elif current_page == 15:
            next_page_url = reverse('Voting page 16')
        elif current_page == 16:
            next_page_url = reverse('Voting page 17')
        elif current_page == 17:
            next_page_url = reverse('Voting page 18')
        elif current_page == 18:
            next_page_url = reverse('Voting page 19')
        elif current_page == 19:
            next_page_url = reverse('Voting page 20')
        else:
            next_page_url = reverse('Exit Page')

        return redirect(next_page_url)
    else:
        return redirect('Login Page')
