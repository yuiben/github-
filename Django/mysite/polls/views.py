from msilib.schema import Class
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

class IndexClass(View):
    def get(self, request):
        ketqua = "123214"
        return HttpResponse(ketqua)

def viewlist(request):
    #lấy đối tượng với tham số khóa chính là = 1, nếu không có sẽ lỗi 404
    #lưu ý khi chỉ lấy 1 đối tượng thì không để trong list duyệt vòng for mà duyệt thẳng đối tượng đó ra 
    #list_question = get_object_or_404(Question, pk=5)
    #lấy dữ liệu từ bảng question
    list_question = Question.objects.all()
    context = {"dsRequest" : list_question}
    return render(request, "polls/QuestionList.html", context)

def detailView(request, question_id):
    qs = Question.objects.get(pk = question_id)
    #print(qs.question_text)
    context = {"question" : qs}
    return render(request, "polls/detail_question.html", context)

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    #context = {"dsRequest" : c}
    try:
        dulieu_input = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu_input)
    except:
        HttpResponse("Lỗi không có choice")
    
    c.vote = c.vote + 1
    c.save()
    #return HttpResponse(c.vote)
    return render(request, "polls/result.html", {"question":q})

###########################

#sử dụng class
class PostClass(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})
    
class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})
    
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Luu OK')
        else:
            return HttpResponse('Khong dc validate')
    
#Sử dụng function
def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f':a})

def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Luu OK')
        else:
            return HttpResponse('Khong dc validate')
    else:
        return HttpResponse('Khong phai Post Request')
    
def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})

def email_request(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            #cach 1 để lấy dữ liệu từng field
            # tieude = m.cleaned_data['title']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # cc = m.cleaned_data['cc']
            # context = {'title':tieude, 'content':noidung, 'email_':email, 'cc_':cc}
            #cach 2 để lấy từng field trong form
            context2 = {'email_data': m}
            return render(request, 'news/print_email.html',context2)
        else:
            return HttpResponse('Form not Validate')
    else:
        return HttpResponse('Not Post Method')
    