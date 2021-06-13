# Generated by Django 3.1.7 on 2021-03-29 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210327_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='interviewername',
            new_name='interviewerusername',
        ),
        migrations.AlterField(
            model_name='interview',
            name='question',
            field=models.CharField(choices=[("What is Banker's algorithm?", "What is Banker's algorithm?"), ('Define overloading and overriding in OOPS?', 'Define overloading and overriding in OOPS?'), ('What is a checkpoint in DBMS?', 'What is a checkpoint in DBMS?'), ('Explain what is Computer Architecture?', 'Explain what is Computer Architecture?'), ('What is an operating system?', 'What is an operating system?'), ('What is DBMS?', 'What is DBMS?'), ('What is a Stack?', 'What is a Stack?'), ('List the area of applications where stack data structure can be used?', 'List the area of applications where stack data structure can be used?'), ('What is OOPS?', 'What is OOPS?'), ('What are the advantages of DBMS?', 'What are the advantages of DBMS?'), ('What is the use of paging in operating system?', 'What is the use of paging in operating system?'), ('What are the basic concepts of OOPS?', 'What are the basic concepts of OOPS?')], default='', max_length=255),
        ),
    ]