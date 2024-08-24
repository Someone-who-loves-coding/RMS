from django.db import models


class Employeetable(models.Model):
    empid = models.IntegerField(db_column='EMPID', primary_key=True)  # Field name made lowercase.
    empname = models.CharField(db_column='EmpName', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    empnamehindi = models.CharField(db_column='EmpNameHindi', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10,  blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    doj = models.DateField(db_column='DOJ', blank=True, null=True)  # Field name made lowercase.
    dateofjoining = models.DateField(db_column='DateOfJoining', blank=True, null=True)  # Field name made lowercase.
    dor = models.DateField(db_column='DOR', blank=True, null=True)  # Field name made lowercase.
    dateofretirement = models.DateField(db_column='DateOfRetirement', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    specialcategory = models.CharField(db_column='SpecialCategory', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    ispwd = models.BooleanField(db_column='isPwD', blank=True, null=True)  # Field name made lowercase.
    socialcategory = models.CharField(db_column='SocialCategory', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    officialemail = models.CharField(db_column='OfficialEmail', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='MobileNo', max_length=15,  blank=True, null=True)  # Field name made lowercase.
    isshowmobile = models.BooleanField(db_column='IsShowMobile', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10,  blank=True, null=True)  # Field name made lowercase.
    epfno = models.CharField(db_column='EPFNo', max_length=20,  blank=True, null=True)  # Field name made lowercase.
    jobstatusid = models.IntegerField(db_column='JobStatusID', blank=True, null=True)  # Field name made lowercase.
    jobstatus = models.CharField(db_column='JobStatus', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    jobtypeid = models.IntegerField(db_column='JobTypeID', blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='JobType', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    imgfile = models.CharField(db_column='imgFile', max_length=255,  blank=True, null=True)  # Field name made lowercase.
    designationid = models.IntegerField(db_column='DesignationID', blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    designationhindi = models.CharField(db_column='DesignationHindi', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    designationshortname = models.CharField(db_column='DesignationShortName', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    designationorderid = models.IntegerField(db_column='DesignationOrderID', blank=True, null=True)  # Field name made lowercase.
    empgroup = models.CharField(db_column='EmpGroup', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    officeid = models.IntegerField(db_column='OfficeID', blank=True, null=True)  # Field name made lowercase.
    officetype = models.CharField(db_column='OfficeType', max_length=50,  blank=True, null=True)  # Field name made lowercase.
    officetypename = models.CharField(db_column='OfficeTypeName', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneID', blank=True, null=True)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    reportingofficerid = models.IntegerField(db_column='ReportingOfficerID', blank=True, null=True)  # Field name made lowercase.
    reportingofficer = models.CharField(db_column='ReportingOfficer', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    reportingofficer2id = models.IntegerField(db_column='ReportingOfficer2ID', blank=True, null=True)  # Field name made lowercase.
    reportingofficer2 = models.CharField(db_column='ReportingOfficer2', max_length=100,  blank=True, null=True)  # Field name made lowercase.
    isro1primary = models.BooleanField(db_column='IsRO1Primary', blank=True, null=True)  # Field name made lowercase.
    dateofcurrentposting = models.DateField(db_column='DateOfCurrentPosting', blank=True, null=True)  # Field name made lowercase.
    currentpostingdatefull = models.DateField(db_column='CurrentPostingDateFull', blank=True, null=True)  # Field name made lowercase.
    enddateofcurrentposting = models.DateField(db_column='EndDateOfCurrentPosting', blank=True, null=True)  # Field name made lowercase.
    enddateofcurrentpostingfull = models.DateField(db_column='EndDateOfCurrentPostingFull', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'EmployeeTable'

class PeripheralRequest(models.Model):
    CATEGORY_CHOICES = [
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=100)
    reason = models.TextField(max_length=400)
    employee_id = models.CharField(max_length=10)  # Assuming empid is a string

    def __str__(self):
        return f"{self.employee_id} - {self.subject}"