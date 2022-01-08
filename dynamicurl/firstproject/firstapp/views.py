from django.shortcuts import render

# Create your views here.
# def show_details(request, my_id):
#     student = {'id':my_id}
#     return render(request, 'firstapp/show.html',student)

def home(request):
    return render(request,'firstapp/home.html')

def show_details(request, my_id):
    if my_id == 1:
        student = {'id':my_id, 'name': 'Gaurav Yadav'}
    if my_id == 2:
        student = {'id':my_id, 'name': 'Mnaoj Dhillon'}
    if my_id == 3:
        student = {'id':my_id, 'name': 'Deepak Kumar'}
    if my_id == 4:
        student = {'id':my_id, 'name': 'Vivek Rai'}
    if my_id == 5:
        student = {'id':my_id, 'name': 'Deepak Saini'}
    return render(request, 'firstapp/show.html',student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 1:
        student = {'id':my_id, 'name': 'Gaurav Yadav', 'info': 'sub_details'}
    if my_id == 2 and my_subid == 2:
        student = {'id':my_id, 'name': 'Mnaoj Dhillon', 'info': 'sub_details'}
    if my_id == 3 and my_subid == 3:
        student = {'id':my_id, 'name': 'Deepak Kumar','info': 'sub_details'}
    if my_id == 4 and my_subid == 4:
        student = {'id':my_id, 'name': 'Vivek Rai', 'info': 'sub_details'}
    if my_id == 5 and my_subid == 5:
        student = {'id':my_id, 'name': 'Deepak Saini', 'info': 'sub_details'}
    return render(request, 'firstapp/show.html',student)