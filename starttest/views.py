from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from dashboard.models import Interview

# Create your views here.

def testregister(request):
    if request.method == 'POST':
        interview_id = request.POST['interviewid']
        candidate_name = request.POST['candidatename']
        candidate_email = request.POST['candidateemail']
        interview_name = request.POST['interviewname']
        
        obj = set(Interview.objects.values_list('question',flat=True).filter(interviewname=interview_name,interviewid=interview_id,candidateemail=candidate_email,candidatename=candidate_name))
        questions_list = list(obj)


        print(questions_list)
        if not questions_list:
            return HttpResponse("You are not authorized to take this Test")
        else:
            request.session.set_expiry(1500)
            request.session['interviewid'] = interview_id
            request.session['interviewname'] = interview_name
            request.session['candidatename'] = candidate_name
            request.session['candidateemail'] = candidate_email
            request.session['question_1'] = questions_list[0]
            request.session['question_2'] = questions_list[1]
            request.session['question_3'] = questions_list[2]
            request.session['question_4'] = questions_list[3]
            request.session['question_5'] = questions_list[4]
            request.session['question_6'] = questions_list[5]
            request.session['question_7'] = questions_list[6]
            request.session['question_8'] = questions_list[7]
            request.session['question_9'] = questions_list[8]
            request.session['question_10'] = questions_list[9]
            return render(request,'instructions_new.html',{'candidatename':candidate_name,'interviewname':interview_name})
            

    else:
        return render(request,'testregister_new.html')
def questionone(request):
    if request.method == 'POST':
        answer_1 = request.POST['answer_1']
        question_1 = request.session['question_1']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_1:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_1).update(answer=answer_1,is_attended=is_attend)
        return redirect('questiontwo')            
    else:
        question = request.session['question_1']
        return render(request,'one_new.html',{'question_1':question})
def questiontwo(request):
    if request.method == 'POST':
        answer_2 = request.POST['answer_2']
        question_2 = request.session['question_2']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_2:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_2).update(answer=answer_2,is_attended=is_attend)
        return redirect('questionthree')               
    else:
        question = request.session['question_2']
        return render(request,'two_new.html',{'question_2':question})    
def questionthree(request):
    if request.method == 'POST':
        answer_3 = request.POST['answer_3']
        question_3 = request.session['question_3']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_3:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_3).update(answer=answer_3,is_attended=is_attend)
        return redirect('questionfour')               
    else:
        question = request.session['question_3']
        return render(request,'three_new.html',{'question_3':question})
def questionfour(request):
    if request.method == 'POST':
        answer_4 = request.POST['answer_4']
        question_4 = request.session['question_4']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_4:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_4).update(answer=answer_4,is_attended=is_attend)
        return redirect('questionfive')               
    else:
        question = request.session['question_4']
        return render(request,'four_new.html',{'question_4':question})
def questionfive(request):
    if request.method == 'POST':
        answer_5 = request.POST['answer_5']
        question_5 = request.session['question_5']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_5:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_5).update(answer=answer_5,is_attended=is_attend)
        return redirect('questionsix')               
    else:
        question = request.session['question_5']
        return render(request,'five_new.html',{'question_5':question})
def questionsix(request):
    if request.method == 'POST':
        answer_6 = request.POST['answer_6']
        question_6 = request.session['question_6']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_6:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_6).update(answer=answer_6,is_attended=is_attend)
        return redirect('questionseven')               
    else:
        question = request.session['question_6']
        return render(request,'six_new.html',{'question_6':question})
def questionseven(request):
    if request.method == 'POST':
        answer_7 = request.POST['answer_7']
        question_7 = request.session['question_7']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_7:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_7).update(answer=answer_7,is_attended=is_attend)
        return redirect('questioneight')               
    else:
        question = request.session['question_7']
        return render(request,'seven_new.html',{'question_7':question})
def questioneight(request):
    if request.method == 'POST':
        answer_8 = request.POST['answer_8']
        question_8 = request.session['question_8']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_8:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_8).update(answer=answer_8,is_attended=is_attend)
        return redirect('questionnine')               
    else:
        question = request.session['question_8']
        return render(request,'eight_new.html',{'question_8':question})
def questionnine(request):
    if request.method == 'POST':
        answer_9 = request.POST['answer_9']
        question_9 = request.session['question_9']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_9:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_9).update(answer=answer_9,is_attended=is_attend)
        return redirect('questionten')               
    else:
        question = request.session['question_9']
        return render(request,'nine_new.html',{'question_9':question})
def questionten(request):
    if request.method == 'POST':
        answer_10 = request.POST['answer_10']
        question_10 = request.session['question_10']
        interview_name = request.session['interviewname']
        interview_id = request.session['interviewid']
        candidate_email = request.session['candidateemail']
        candidate_name = request.session['candidatename']
        is_attend = False
        if answer_10:
            is_attend = True
        Interview.objects.filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,question=question_10).update(answer=answer_10,is_attended=is_attend)
        
        return redirect('testcomplete')               
    else:
        question = request.session['question_10']
        return render(request,'ten_new.html',{'question_10':question})
def testcomplete(request):
    return render(request,'testcomplete_new.html')