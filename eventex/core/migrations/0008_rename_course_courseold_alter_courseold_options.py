# Generated by Django 4.2.5 on 2023-10-05 20:01

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]