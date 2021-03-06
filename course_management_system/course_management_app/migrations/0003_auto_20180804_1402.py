# Generated by Django 2.0.5 on 2018-08-04 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_management_app', '0002_auto_20180731_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_assignment', models.FileField(blank=True, upload_to='')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_management_app.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='userprofileinfo_ptr',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='course',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
