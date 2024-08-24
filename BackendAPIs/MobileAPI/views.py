# from django.shortcuts import render

# # Create your views here.

# def Peripherals(request):
#     return render(request, 'Peripherals.html')

# def ReviewApplications(request):
#     return render(request, 'ReviewApplications.html')

# def Dashboard(request):
#     return render(request, 'Login.html')

# def Consultants(request):
#     return render(request, 'Consultants.html')

# def Aboutus(request):
#     return render(request, 'Aboutus.html')

import random
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view
from .serializers import PeripheralRequestSerializer
from BackendAPIs import settings
from .serializers import EmployeeSerializer
import requests
from .models import Employeetable as Employee
from twilio.rest import Client
from rest_framework.response import Response

class EmployeeGET(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from django.core.cache import cache
from django.conf import settings
from twilio.rest import Client
from django.http import JsonResponse
from .models import Employeetable as Employee
import random

def Login(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        otp = request.POST.get('otp')
        request.session['empid'] = empid

        if empid and not otp:  # Stage 1: Generate and send OTP
            try:
                employee = Employee.objects.get(empid=empid)
                mobile_number = employee.mobileno

                # Generate a 6-digit OTP
                generated_otp = random.randint(100000, 999999)

                # Send OTP via Twilio
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(
                    body=f'Your RMS OTP verification code is {generated_otp}. Please do not share it with others',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to='+91' + employee.mobileno
                )

                # Store the OTP in the Django cache
                cache.set(f'otp_{empid}', generated_otp, timeout=300)  # 300 seconds (5 minutes) timeout

                return JsonResponse({'status': 'OTP sent', 'empid': empid})
            except Employee.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Invalid Employee ID'})

        elif empid and otp:  # Stage 2: Verify OTP
            stored_otp = cache.get(f'otp_{empid}')
            if stored_otp == int(otp):
                # OTP is correct, proceed with login
                return JsonResponse({'status': 'OTP verified', 'empid': empid})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid OTP'})

    return render(request, 'Login.html')



def dashboard(request):
    response = requests.get("http://127.0.0.1:8000/apiget").json()  # Add the API key hosted (CHANGE IT)
    empid = request.session.get('empid')

    # Filter the response to get the data for the specific empid
    employee_data = next((i for i in response if str(i['empid']) == empid), None)
    context = { 'employee_data': employee_data }
    return render(request, 'dashboard.html', context)

def request(request):
    response = requests.get("http://127.0.0.1:8000/apiget").json()  # Add the API key hosted (CHANGE IT)
    empid = request.session.get('empid')
    employee_data = next((i for i in response if str(i['empid']) == empid), None)
    context = { 'employee_data': employee_data }
    return render(request, 'Requestform.html', context)

@api_view(['POST'])
def submit_peripheral_request(request):
    serializer = PeripheralRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'Request submitted'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)