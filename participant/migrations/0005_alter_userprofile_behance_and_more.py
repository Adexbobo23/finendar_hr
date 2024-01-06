# Generated by Django 4.2.4 on 2024-01-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0004_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='behance',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='career_objective',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_job_place',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='designation',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='designation_employment',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dribbble',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education_level',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ending_period_education',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ending_period_employment',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='father_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='institute',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='major',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marital_status',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mother_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='permanent_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pinterest',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='present_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='religion',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='responsibility',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='result_gpa',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='starting_period_education',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='starting_period_employment',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website_link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_of_experience',
            field=models.CharField(default='', max_length=10),
        ),
    ]