import mysql.connector
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students
from .models import goods
import logging
from django.db.utils import IntegrityError



# Create your views here.
# def index(request):
#     return render(request,'sports_goods/index.html')

# def my_view(request):
#     data = Ptudents.objects.all()
#     return render(request, 'index.html', {'data': data})

# def register(request):
#     return render(request,"sports_goods/register.html", {})


# def insertuser(request):
#     # left side pe temporary variables bnane hai and right brackets mein exact names used in template
#     tnumber= request.POST['EnrollmentNumber'];
#     tname= request.POST['UName'];
#     tbranch= request.POST['branches'];
#     tphone=request.POST['phone'];
#     # Ab yaha pe left pe database wale names and right pe temporary variables.
#     Regis=Students(Enrollment_number=tnumber, Name=tname, Branch=tbranch, Phone_number=tphone);
#     Regis.save();
#     # Ab yeh wo page hoga jaha pe entry hone ke baad we will go
#     return render(request,'sports_goods/index.html',{})

# def index(request):
#     if request.method == 'POST':
#         print("Form submitted")
#         return HttpResponse("Form submitted")
#     else:
#         return render(request, 'sports_goods/index.html', {})

def register(request):
    return render(request, 'sports_goods/register.html', {})


def insertusers(request):
    if request.method == 'POST':
        tnumber = request.POST.get('EnrollmentNumber')
        tname = request.POST.get('UName')
        tbranch = request.POST.get('branches')
        tphone = request.POST.get('phone')
        try:
            Regis = Students(Enrollment_number=tnumber, Name=tname, Branch=tbranch, Phone_number=tphone)
            Regis.full_clean()
            Regis.save()
            return render(request, 'sports_goods/index.html', {})
        except IntegrityError:
            error_msg = "Enrollment number already exists"
            return render(request, 'sports_goods/index.html', {'error_msg': error_msg})
        except Exception as e:
            error_msg = "An error occurred: {}".format(str(e))
            return render(request, 'sports_goods/index.html', {'error_msg': error_msg})
    else:
        return render(request, 'sports_goods/index.html', {})
    
def show_students(request):
    students = Students.objects.all()
    context = {'students': students}
    return render(request, 'sports_goods/showall.html', context)


# def particular(request):
#     conne = mysql.connector.connect(user='root', password='nikhil2002',
#                                   host='localhost', database='newsport')
#     cursor = conne.cursor()
#     query = "SELECT * FROM user"
#     cursor.execute(query)
#     results = cursor.fetchall()
#     conne.close()
#     return render(request, 'sports_goods/particular.html', {'results': results})

def loginpage(request):
    return render(request, 'sports_goods/login_page.html')

def login_view(request):
    if request.method == 'POST':
        enrollment_number = request.POST.get('uname')
        password = request.POST.get('psw')

        # connect to the MySQL database
        conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
        cursor = conne.cursor()

        # execute the SQL query to check the credentials
        query = f"SELECT * FROM user WHERE enrollment_number = {enrollment_number} AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        # if user exists, set a session variable and show the dashboard
        if user:
            request.session['Enrollment_number'] = user[0] # assuming user_id is the first column in the table
            query = F"SELECT * FROM user WHERE enrollment_number = {enrollment_number}"
            cursor.execute(query)
            results = cursor.fetchall()
            
            # close the database connection
            conne.close()
            
            return render(request, 'sports_goods/particular.html', {'results': results})
        else:
            # close the database connection
            conne.close()

            # if user does not exist, show an error message
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'sports_goods/login_page.html', {'error_message': error_message})
    else:
        # if request method is GET, show the login page
        return render(request, 'sports_goods/login_page.html')


