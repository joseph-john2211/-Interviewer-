from django.db import models

# Create your models here.




class QuestionsTable(models.Model):
    topic = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    class Meta:
        db_table = 'QuestionsTable'

topic_set = set((QuestionsTable.objects.all().values_list('topic')))
topic_list = list(topic_set)

question_set = set((QuestionsTable.objects.all().values_list('question',flat=True)))
question_list = list(question_set)
possible_question = []

for question in question_list:
    sublist = []
    sublist.append(question)
    sublist.append(question)
    possible_question.append(sublist)


def convert(possible_question):
    return tuple( tuple(pair) for pair in possible_question)
CHOICE = convert(possible_question)


class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    interviewname = models.CharField(max_length=100)
    interviewid = models.IntegerField()
    candidateemail = models.CharField(max_length=100)
    candidatename = models.CharField(max_length=100)
    interviewerusername = models.CharField(max_length=100)
    question = models.CharField(max_length=255,choices=CHOICE, default='')
    answer = models.TextField()
    is_attended = models.BooleanField(default=False)

    class Meta:
        db_table = 'Interview'
        
    

class Student(models.Model):
    studentname = models.TextField()
    studentemail = models.TextField()
    class Meta:
        db_table = 'Student'





