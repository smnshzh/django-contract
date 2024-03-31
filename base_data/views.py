from django.shortcuts import render ,redirect
import json
import pandas as pd
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import EmployeeDetails
from datetime import datetime
def custom_404_view(request, exeptions):
# snipped custom 404 view code
    return redirect('dashboard')
#
# def custom_500_view(request, exeptions):
# # snipped custom 500 view code
#     return redirect('dashboard')

@login_required
def dashboard(request):
    # Assuming you have some data to pass to the template
    context = {
        'welcome_message': 'Welcome to our website!',
        'latest_news': ['News item 1', 'News item 2', 'News item 3'],
        # Add more context data as needed
    }
    return render(request, 'home.html', context)
@login_required
def setting_view(request):
    persons = EmployeeDetails.objects.filter(user_creator= request.user)

    return render(request, 'setting.html')



@login_required
def insert_data(request):
    if request.method == 'POST':
        # Decode the JSON data from request body
        user_name = request.user
        json_data = json.loads(request.body)

        # Check if JSON data is a list
        if not isinstance(json_data, list):
            return JsonResponse({'error': 'Input data must be a list'}, status=400)

        # Check if JSON data contains at least two rows (header and data)
        if len(json_data) < 2:
            return JsonResponse({'error': 'Input data must contain header and data'}, status=400)

        header = json_data[0]
        data = json_data[1:]

        # Check if the header contains all required columns
        required_columns = ['مرکز هزینه', 'شماره پرسنلی', 'نوع بیمه', 'شماره بیمه', 'تاریخ استخدام', 'تاریخ تولد', 'محل تولد', 'نام', 'نام خانوادگی', 'شماره شناسنامه', 'نام پدر', 'کد ملی', 'کد پستی', 'تلفن', 'تلفن همراه', 'مدرک تحصیلی', 'رشته تحصیلی', 'آدرس', 'جنسیت', 'شرح شغل', 'کد شغل', 'مدت قرارداد(ماه)', 'حقوق پایه ماهانه', 'حقوق پایه روزانه', 'حقوق پایه هر ساعت', 'حق جذب', 'حق مسکن', 'حق اولاد', 'بن و خواروبار', 'بدی آب و هوا', 'حق ماموریت', 'پاداش', 'مشمول بیمه', 'سهم کارگر', 'سهم کارفرما', 'معافیت دو هفتم', 'سنوات', 'حق سرپرستی', 'بیمه تکمیلی', 'بیمه بیکاری', 'تاریخ ترک کار', 'وضعیت تاهل', 'تعداد فرزند', 'تاریخ شروع قرارداد', 'تاریخ پایان قرارداد']
         # Add all required columns here
        if not all(col in header for col in required_columns):
            return JsonResponse({'error': 'Header is missing required columns'}, status=400)

        # Check if data rows have the same number of columns as the header
        if any(len(row) != len(header) for row in data):
            return JsonResponse({'error': 'Data rows have inconsistent number of columns'}, status=400)

        # Create DataFrame
        df = pd.DataFrame(data, columns=header)

        # Additional data validation checks if needed

        # Assign user to DataFrame
        df['user'] = user_name

        # Save data to the database
        try:
            for _, row in df.iterrows():
                employee_details = EmployeeDetails.objects.create(
                    marital_status=row['وضعیت تاهل'],
                    cost_center=row['مرکز هزینه'],
                    employee_id=int(float(row['شماره پرسنلی'])),
                    insurance_type=row['نوع بیمه'],
                    insurance_number=row['شماره بیمه'],
                    employment_date=row['تاریخ استخدام'],
                    date_of_birth=row['تاریخ تولد'],
                    place_of_birth=row['محل تولد'],
                    first_name=row['نام'],
                    last_name=row['نام خانوادگی'],
                    national_id=row['شماره شناسنامه'],
                    father_name=row['نام پدر'],
                    national_code=row['کد ملی'],
                    postal_code=row['کد پستی'],
                    telephone=row['تلفن'],
                    mobile=row['تلفن همراه'],
                    education_degree=row['مدرک تحصیلی'],
                    field_of_study=row['رشته تحصیلی'],
                    address=row['آدرس'],
                    gender=row['جنسیت'],
                    job_description=row['شرح شغل'],
                    job_code=row['کد شغل'],
                    contract_duration=int(float(row['مدت قرارداد(ماه)'])),
                    monthly_base_salary=int(float(row['حقوق پایه ماهانه'])),
                    daily_base_salary=int(float(row['حقوق پایه روزانه'])),
                    hourly_base_salary=int(float(row['حقوق پایه هر ساعت'])),
                    recruitment_bonus=int(float(row['حق جذب'])),
                    housing_allowance=int(float(row['حق مسکن'])),
                    child_allowance=int(float(row['حق اولاد'])),
                    food_and_weather_allowance=int(float(row['بن و خواروبار'])),
                    weather_disability=int(float(row['بدی آب و هوا'])),
                    mission_allowance=int(float(row['حق ماموریت'])),
                    bonus=int(float(row['پاداش'])),
                    insured=row['مشمول بیمه'],
                    worker_share=row['سهم کارگر'],
                    employer_share=row['سهم کارفرما'],
                    two_thirds_exemption=int(float(row['معافیت دو هفتم'])),
                    seniority=int(float(row['سنوات'])),
                    supervisor_allowance=int(float(row['حق سرپرستی'])),
                    supplementary_insurance=int(float(row['بیمه تکمیلی'])),
                    unemployment_insurance=row['بیمه بیکاری'],
                    termination_date=row['تاریخ ترک کار'],
                    child_number=int(float(row['تعداد فرزند'])),
                    cstart=row['تاریخ شروع قرارداد'],
                    cend=row['تاریخ پایان قرارداد'],
                    user_creator=user_name
                )

                employee_details.save()
        except Exception as e:

                return JsonResponse({'error': str(e)}, status=400)

        return redirect('setting')

    # Handle GET request or other cases
    # You can render an upload template here
