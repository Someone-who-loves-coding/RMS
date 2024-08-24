# Generated by Django 5.0.8 on 2024-08-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeetable',
            fields=[
                ('empid', models.IntegerField(db_column='EMPID', primary_key=True, serialize=False)),
                ('empname', models.CharField(blank=True, db_column='EmpName', max_length=100, null=True)),
                ('empnamehindi', models.CharField(blank=True, db_column='EmpNameHindi', max_length=100, null=True)),
                ('maritalstatus', models.CharField(blank=True, db_column='MaritalStatus', max_length=20, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=10, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('dateofbirth', models.DateField(blank=True, db_column='DateOfBirth', null=True)),
                ('doj', models.DateField(blank=True, db_column='DOJ', null=True)),
                ('dateofjoining', models.DateField(blank=True, db_column='DateOfJoining', null=True)),
                ('dor', models.DateField(blank=True, db_column='DOR', null=True)),
                ('dateofretirement', models.DateField(blank=True, db_column='DateOfRetirement', null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=50, null=True)),
                ('specialcategory', models.CharField(blank=True, db_column='SpecialCategory', max_length=50, null=True)),
                ('ispwd', models.BooleanField(blank=True, db_column='isPwD', null=True)),
                ('socialcategory', models.CharField(blank=True, db_column='SocialCategory', max_length=50, null=True)),
                ('officialemail', models.CharField(blank=True, db_column='OfficialEmail', max_length=100, null=True)),
                ('mobileno', models.CharField(blank=True, db_column='MobileNo', max_length=15, null=True)),
                ('isshowmobile', models.BooleanField(blank=True, db_column='IsShowMobile', null=True)),
                ('pan', models.CharField(blank=True, db_column='PAN', max_length=10, null=True)),
                ('epfno', models.CharField(blank=True, db_column='EPFNo', max_length=20, null=True)),
                ('jobstatusid', models.IntegerField(blank=True, db_column='JobStatusID', null=True)),
                ('jobstatus', models.CharField(blank=True, db_column='JobStatus', max_length=50, null=True)),
                ('jobtypeid', models.IntegerField(blank=True, db_column='JobTypeID', null=True)),
                ('jobtype', models.CharField(blank=True, db_column='JobType', max_length=50, null=True)),
                ('imgfile', models.CharField(blank=True, db_column='imgFile', max_length=255, null=True)),
                ('designationid', models.IntegerField(blank=True, db_column='DesignationID', null=True)),
                ('designation', models.CharField(blank=True, db_column='Designation', max_length=100, null=True)),
                ('department', models.CharField(blank=True, db_column='Department', max_length=100, null=True)),
                ('designationhindi', models.CharField(blank=True, db_column='DesignationHindi', max_length=100, null=True)),
                ('designationshortname', models.CharField(blank=True, db_column='DesignationShortName', max_length=50, null=True)),
                ('designationorderid', models.IntegerField(blank=True, db_column='DesignationOrderID', null=True)),
                ('empgroup', models.CharField(blank=True, db_column='EmpGroup', max_length=50, null=True)),
                ('officeid', models.IntegerField(blank=True, db_column='OfficeID', null=True)),
                ('officetype', models.CharField(blank=True, db_column='OfficeType', max_length=50, null=True)),
                ('officetypename', models.CharField(blank=True, db_column='OfficeTypeName', max_length=100, null=True)),
                ('office', models.CharField(blank=True, db_column='Office', max_length=100, null=True)),
                ('zoneid', models.IntegerField(blank=True, db_column='ZoneID', null=True)),
                ('zonename', models.CharField(blank=True, db_column='ZoneName', max_length=100, null=True)),
                ('reportingofficerid', models.IntegerField(blank=True, db_column='ReportingOfficerID', null=True)),
                ('reportingofficer', models.CharField(blank=True, db_column='ReportingOfficer', max_length=100, null=True)),
                ('reportingofficer2id', models.IntegerField(blank=True, db_column='ReportingOfficer2ID', null=True)),
                ('reportingofficer2', models.CharField(blank=True, db_column='ReportingOfficer2', max_length=100, null=True)),
                ('isro1primary', models.BooleanField(blank=True, db_column='IsRO1Primary', null=True)),
                ('dateofcurrentposting', models.DateField(blank=True, db_column='DateOfCurrentPosting', null=True)),
                ('currentpostingdatefull', models.DateField(blank=True, db_column='CurrentPostingDateFull', null=True)),
                ('enddateofcurrentposting', models.DateField(blank=True, db_column='EndDateOfCurrentPosting', null=True)),
                ('enddateofcurrentpostingfull', models.DateField(blank=True, db_column='EndDateOfCurrentPostingFull', null=True)),
            ],
            options={
                'db_table': 'EmployeeTable',
            },
        ),
    ]
