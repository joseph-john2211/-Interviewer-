from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.forms import formset_factory
from .models import Interview, QuestionsTable
from .forms import InterviewForm, AddcandidateForm


# Create your views here.       
def user(request):
    
    return render(request, 'index_new.html')
def signout(request):
    auth.logout(request)
    return redirect('/')

def createInterview(request): 
    if request.method == 'POST':
        interviewname = request.POST['interviewname']
        interviewid = request.POST['interviewid']
        noofcandidate = request.POST['noofcandidate']
      
        current_user = request.user
        current_username = current_user.username
        order = formset_factory(InterviewForm,extra=10)
        formset = order(request.POST)
        i = 0

        if formset.is_valid():
            while i < int(noofcandidate):
                for form in formset:
                    question = form.cleaned_data.get('question')
                    if question:
                        Interview(question=question,interviewname=interviewname,interviewid=interviewid,interviewerusername=current_username).save()
                i = i+1
            return redirect(user)
    else:
        order = formset_factory(InterviewForm,extra=10)
        formset = order()
        return render(request,'createInterview_new.html',{'formset':formset})



def addcandidates(request):
    if request.method == 'POST':
        interviewname = request.POST['interviewname']
        interviewid = request.POST['interviewid']
        candidateemail1 = request.POST['candidateemail1']
        candidateemail2 = request.POST['candidateemail2']
        candidateemail3 = request.POST['candidateemail3']
        candidateemail4 = request.POST['candidateemail4']
        candidateemail5 = request.POST['candidateemail5']
        candidateemail6 = request.POST['candidateemail6']
        candidateemail7 = request.POST['candidateemail7']
        candidateemail8 = request.POST['candidateemail8']
        candidateemail9 = request.POST['candidateemail9']
        candidateemail10 = request.POST['candidateemail10']
        candidatename1 = request.POST['candidatename1']
        candidatename2 = request.POST['candidatename2']
        candidatename3 = request.POST['candidatename3']
        candidatename4 = request.POST['candidatename4']
        candidatename5 = request.POST['candidatename5']
        candidatename6 = request.POST['candidatename6']
        candidatename7 = request.POST['candidatename7']
        candidatename8 = request.POST['candidatename8']
        candidatename9 = request.POST['candidatename9']
        candidatename10 = request.POST['candidatename10']
        last_record = Interview.objects.last()
        last_record_id = int(str(last_record)[18:-1])
        start_record_id = last_record_id - 99
        email = []
        email.extend((candidateemail1,candidateemail2,candidateemail3,candidateemail4,candidateemail5,candidateemail6,candidateemail7,candidateemail8,candidateemail9,candidateemail10))
        for i in range(start_record_id,start_record_id+10):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail1,candidatename=candidatename1)
        for i in range(start_record_id+10,start_record_id+20):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail2,candidatename=candidatename2)
        for i in range(start_record_id+20,start_record_id+30):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail3,candidatename=candidatename3)
        for i in range(start_record_id+30,start_record_id+40):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail4,candidatename=candidatename4)
        for i in range(start_record_id+40,start_record_id+50):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail5,candidatename=candidatename5)
        for i in range(start_record_id+50,start_record_id+60):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail6,candidatename=candidatename6)
        for i in range(start_record_id+60,start_record_id+70):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail7,candidatename=candidatename7)
        for i in range(start_record_id+70,start_record_id+80):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail8,candidatename=candidatename8)
        for i in range(start_record_id+80,start_record_id+90):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail9,candidatename=candidatename9)
        for i in range(start_record_id+90,start_record_id+100):
            Interview.objects.filter(pk=i).update(candidateemail=candidateemail10,candidatename=candidatename10)
        return redirect(user)
    else:
        return render(request,'addcandidate_new.html')
def results(request):
    if request.method == 'POST':
        current_user = request.user
        current_username = current_user.username
        interview_name = request.POST['interviewname']
        interview_id = request.POST['interviewid']
        candidate_name = request.POST['candidatename']
        candidate_email = request.POST['candidateemail']

        candidate_questions = list(set(Interview.objects.values_list('question',flat=True).filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,interviewerusername=current_username)))
        
        candidate_answer = []
        original_answer = []
        for ques in candidate_questions:
            ques_key = list(set(Interview.objects.values_list('answer',flat=True).filter(interviewname=interview_name,interviewid=interview_id,candidatename=candidate_name,candidateemail=candidate_email,interviewerusername=current_username,question=ques)))[0]
            candidate_answer.append(ques_key)

        
        for ques in candidate_questions:
            ques_key = list(set(QuestionsTable.objects.values_list('answer',flat=True).filter(question=ques)))[0]
            original_answer.append(ques_key)

        import spacy_universal_sentence_encoder
        nlp = spacy_universal_sentence_encoder.load_model('en_use_md')
        scores = []
        for i in range(len(candidate_answer)):
            doc_1 = nlp(candidate_answer[i])
            doc_2 = nlp(original_answer[i])
            accuracy = doc_1.similarity(doc_2)
            scores.append(accuracy)


        data = []
        for i,s,q,a in zip(range(1,len(scores)+1),scores,candidate_questions,candidate_answer):
            temp = []
            temp.extend((i,s,q,a))
            data.append(temp)

        performance = round(((sum(scores) / len(scores)) * 100),2) 
        remarks = ''
        if performance > 70:
            remarks = remarks + 'Candidate performed Well, and can be considered'
        elif performance >= 50 and performance <= 70:
            remarks = remarks + 'Candidate performed Okay, Can be accepted if the candidate is willing to get trained'
        else:
            remarks = remarks + 'Candidate performed Poor!!!! and should not be considered for this job'       
        
        return render(request,'report_new.html',{'data':data,'performance':performance,'remarks':remarks,'name':candidate_name})

    else:
        current_user = request.user
        current_username = current_user.username
        result = Interview.objects.values_list('interviewname','interviewid','candidatename','candidateemail').distinct().filter(interviewerusername=current_username,is_attended=True)
        


        return render(request,'results_new.html',{'username':current_username,'result':result})
