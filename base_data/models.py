from django.db import models
from django.contrib.auth.models import User
from django.db import models

class EmployeeDetails(models.Model):
    marital_status = models.CharField(max_length=50, verbose_name="وضعیت تاهل")
    cost_center = models.CharField(max_length=50, verbose_name="مرکز هزینه")
    employee_id = models.IntegerField(verbose_name="شماره پرسنلی")
    insurance_type = models.CharField(max_length=50, verbose_name="نوع بیمه")
    insurance_number = models.CharField(max_length=50, verbose_name="شماره بیمه")
    employment_date = models.CharField(max_length=10, verbose_name="تاریخ استخدام")
    date_of_birth = models.CharField(max_length=10, verbose_name="تاریخ تولد")
    place_of_birth = models.CharField(max_length=100, verbose_name="محل تولد")
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    national_id = models.CharField(max_length=20, verbose_name="شماره شناسنامه")
    father_name = models.CharField(max_length=100, verbose_name="نام پدر")
    national_code = models.CharField(max_length=20, verbose_name="کد ملی")
    postal_code = models.CharField(max_length=20, verbose_name="کد پستی")
    telephone = models.CharField(max_length=20, verbose_name="تلفن")
    mobile = models.CharField(max_length=20, verbose_name="تلفن همراه")
    education_degree = models.CharField(max_length=100, verbose_name="مدرک تحصیلی")
    field_of_study = models.CharField(max_length=100, verbose_name="رشته تحصیلی")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    gender = models.CharField(max_length=10, verbose_name="جنسیت")
    job_description = models.CharField(max_length=255, verbose_name="شرح شغل")
    job_code = models.CharField(max_length=50, verbose_name="کد شغل")
    contract_duration = models.IntegerField(verbose_name="مدت قرارداد(ماه)")
    monthly_base_salary = models.IntegerField(verbose_name="حقوق پایه ماهانه")
    daily_base_salary = models.IntegerField(verbose_name="حقوق پایه روزانه")
    hourly_base_salary = models.IntegerField(verbose_name="حقوق پایه هر ساعت")
    recruitment_bonus = models.IntegerField(verbose_name="حق جذب")
    housing_allowance = models.IntegerField(verbose_name="حق مسکن")
    child_allowance = models.IntegerField(verbose_name="حق اولاد")
    food_and_weather_allowance = models.IntegerField(verbose_name="بن و خواروبار")
    weather_disability = models.IntegerField(verbose_name="بدی آب و هوا")
    mission_allowance = models.IntegerField(verbose_name="حق ماموریت")
    bonus = models.IntegerField(verbose_name="پاداش")
    insured = models.BooleanField(verbose_name="مشمول بیمه")
    worker_share = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="سهم کارگر")
    employer_share = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="سهم کارفرما")
    two_thirds_exemption = models.IntegerField(verbose_name="معافیت دو هفتم")
    seniority = models.IntegerField(verbose_name="سنوات")
    supervisor_allowance = models.IntegerField(verbose_name="حق سرپرستی")
    supplementary_insurance = models.IntegerField(verbose_name="بیمه تکمیلی")
    unemployment_insurance = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="بیمه بیکار")
    termination_date = models.CharField(max_length=10, verbose_name="تاریخ ترک کار", null=True)
    child_number = models.IntegerField(verbose_name="تعداد فرزند")
    cstart = models.CharField(max_length=10, verbose_name="تاریخ شروع قرارداد")
    cend = models.CharField(max_length=10, verbose_name="تاریخ پایان قرارداد")
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Creator")

    class Meta:
        # Add a unique constraint for insurance_number and employee_id
        unique_together = ['insurance_number', 'employee_id','cstart']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"

