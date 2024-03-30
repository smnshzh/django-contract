from django.shortcuts import render ,redirect
import json
import pandas as pd
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

        # Print DataFrame
        print(df)

        return redirect('setting')

    # Handle GET request or other cases
    # You can render an upload template here
