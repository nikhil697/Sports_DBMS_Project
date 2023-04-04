import mysql.connector
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students
from .models import goods
import logging
from django.db.utils import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone



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



def loginpage(request):
    return render(request, 'sports_goods/login_page.html')

def login_view(request):
    if request.method == 'POST':
        enrollment_number = request.POST.get('uname')
        password = request.POST.get('psw')

        if enrollment_number == '000000000':
            conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
            cursor = conne.cursor()
            query = f"SELECT * FROM user WHERE enrollment_number = {enrollment_number} AND password = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                request.session['Enrollment_number'] = user[0] # assuming user_id is the first column in the table
                query1 = F"SELECT * FROM user WHERE enrollment_number = {enrollment_number}"
                query2 = f"SELECT * FROM user WHERE Item1 IS NOT NULL OR Item2 IS NOT NULL"
                cursor.execute(query1)
                results = cursor.fetchall()
                cursor.execute(query2)
                haveitems = cursor.fetchall()
            # close the database connection
                conne.close()
                return render(request, 'sports_goods/admin.html', {'results':results,'haveitems': haveitems})
            else:
            # close the database connection
                conne.close()

            # if user does not exist, show an error message
                error_message = 'Invalid login credentials. Please try again.'
                return render(request, 'sports_goods/login_page.html', {'error_message': error_message})
        else:
            conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
            cursor = conne.cursor()
            query = f"SELECT * FROM user WHERE enrollment_number = {enrollment_number} AND password = '{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                request.session['Enrollment_number'] = user[0] # assuming user_id is the first column in the table
                query = F"SELECT * FROM user WHERE enrollment_number = {enrollment_number}"
                cursor.execute(query)
                results = cursor.fetchall()
                items = goods.objects.filter(Possessed_by__isnull=True)
                # close the database connection
                conne.close()
            
                return render(request, 'sports_goods/particular.html', {'results': results,'items': items})
            else:
            # close the database connection
                conne.close()

            # if user does not exist, show an error message
                error_message = 'Invalid login credentials. Please try again.'
                return render(request, 'sports_goods/login_page.html', {'error_message': error_message})
    else:
        # if request method is GET, show the login page
        return render(request, 'sports_goods/login_page.html')
    
    
    
def resetpass(request):
    return render(request, 'sports_goods/resetpass.html', {})

def success(request):
    return render(request, 'sports_goods/resetsuccess.html', {'message': 'Password reset success'})

def resetpassfunc(request):
    if request.method == 'POST':
        enroll = request.POST.get('EnrollmentNumber1')
        prevpass = request.POST.get('prevpass')
        newpass = request.POST.get('newpass')
        conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
        cursor = conne.cursor()
        query = f"UPDATE user SET password = '{newpass}' WHERE Enrollment_number = '{enroll}' AND password = '{prevpass}'"
        cursor.execute(query)
        if cursor.rowcount > 0:
            # Password was successfully updated in the database
            conne.commit()
            conne.close()
            return redirect('success')
        # render(request, 'sports_goods/resetsuccess.html', {})
        else:
            # Password could not be updated in the database
            conne.rollback()
            conne.close()
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'sports_goods/resetpass.html', {'error_message': error_message})
    else:
        # if request method is GET, show the reset password page
        return render(request, 'sports_goods/resetpass.html', {})


def booked(request):
    if request.method == 'POST':
        item1 = request.POST.get('item1')
        item2 = request.POST.get('item2')
        enrollment_number = request.session.get('Enrollment_number')
        conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
        cursor = conne.cursor()
        query=f"update Items set Possessed_by='{enrollment_number}' where id='{item1}'"
        query1=f"update Items set Possessed_by='{enrollment_number}' where id='{item2}'"
        query2=f"update user set Item1='{item1}', Item2='{item2}' where Enrollment_number='{enrollment_number}'"
        cursor.execute(query)
        cursor.execute(query1)
        cursor.execute(query2)
        # student = Students.objects.get(Enrollment_number=enrollment_number)
        # student.book_time = timezone.now()
        # student.save()
        query4 = f"UPDATE User SET book_time = NOW() WHERE Enrollment_number = '{enrollment_number}'"
        cursor.execute(query4)
        conne.commit()
        conne.close()
        message='Successfully Booked'
        return render(request,'sports_goods/booksuccess.html',{'message':message})
    
def released(request):
    if request.method== 'POST':
        enrollment_number = request.POST.get('enrollment_number')
        conne=mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='newsport')
        cursor = conne.cursor()
        query1=f"update user set Item1=NULL ,Item2=NULL where Enrollment_number='{enrollment_number}'"
        query2=f"update Items set Possessed_by=NULL where Possessed_by='{enrollment_number}'"
        cursor.execute(query1)
        cursor.execute(query2)
        conne.commit()
        conne.close()
        message='Successfully Returned'
        return render(request,'sports_goods/admin.html',{'message':message})




    


