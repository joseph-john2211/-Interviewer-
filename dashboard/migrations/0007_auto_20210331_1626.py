# Generated by Django 3.1.7 on 2021-03-31 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210331_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={},
        ),
        migrations.AlterField(
            model_name='interview',
            name='question',
            field=models.CharField(choices=[('What is an operating system?', 'What is an operating system?'), ('What is the use of paging in operating system?', 'What is the use of paging in operating system?'), ('What is DBMS?', 'What is DBMS?'), ('What are the basic concepts of OOPS?', 'What are the basic concepts of OOPS?'), ('List the area of applications where stack data structure can be used?', 'List the area of applications where stack data structure can be used?'), ('What is a Stack?', 'What is a Stack?'), ('What is OOPS?', 'What is OOPS?'), ('What is a checkpoint in DBMS?', 'What is a checkpoint in DBMS?'), ('Define overloading and overriding in OOPS?', 'Define overloading and overriding in OOPS?'), ('Explain what is Computer Architecture?', 'Explain what is Computer Architecture?'), ('What are the advantages of DBMS?', 'What are the advantages of DBMS?'), ("What is Banker's algorithm?", "What is Banker's algorithm?")], default='', max_length=255),
        ),
    ]