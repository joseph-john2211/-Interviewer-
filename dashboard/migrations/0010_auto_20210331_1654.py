# Generated by Django 3.1.7 on 2021-03-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210331_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='question',
            field=models.CharField(choices=[('What is a checkpoint in DBMS?', 'What is a checkpoint in DBMS?'), ("What is Banker's algorithm?", "What is Banker's algorithm?"), ('Define overloading and overriding in OOPS?', 'Define overloading and overriding in OOPS?'), ('What is an operating system?', 'What is an operating system?'), ('What is a Stack?', 'What is a Stack?'), ('What is the use of paging in operating system?', 'What is the use of paging in operating system?'), ('What is OOPS?', 'What is OOPS?'), ('What are the basic concepts of OOPS?', 'What are the basic concepts of OOPS?'), ('List the area of applications where stack data structure can be used?', 'List the area of applications where stack data structure can be used?'), ('Explain what is Computer Architecture?', 'Explain what is Computer Architecture?'), ('What is DBMS?', 'What is DBMS?'), ('What are the advantages of DBMS?', 'What are the advantages of DBMS?')], default='', max_length=255),
        ),
    ]
