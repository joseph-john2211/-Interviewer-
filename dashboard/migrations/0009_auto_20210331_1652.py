# Generated by Django 3.1.7 on 2021-03-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210331_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='question',
            field=models.CharField(choices=[('What is a checkpoint in DBMS?', 'What is a checkpoint in DBMS?'), ('What are the advantages of DBMS?', 'What are the advantages of DBMS?'), ("What is Banker's algorithm?", "What is Banker's algorithm?"), ('What is OOPS?', 'What is OOPS?'), ('What is the use of paging in operating system?', 'What is the use of paging in operating system?'), ('Explain what is Computer Architecture?', 'Explain what is Computer Architecture?'), ('What are the basic concepts of OOPS?', 'What are the basic concepts of OOPS?'), ('What is DBMS?', 'What is DBMS?'), ('Define overloading and overriding in OOPS?', 'Define overloading and overriding in OOPS?'), ('What is an operating system?', 'What is an operating system?'), ('What is a Stack?', 'What is a Stack?'), ('List the area of applications where stack data structure can be used?', 'List the area of applications where stack data structure can be used?')], default='', max_length=255),
        ),
    ]
