from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
# Create your views here.

def index(request):
    myname = "ben bùi"
    hangXe = ["yamaha", "honda", "suzuki"]
    context = {"name" : myname, "thuonghieu" : hangXe}
    return render(request, "polls/index.html", context)

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

def vote(request):
    #q = Question.objects.get(pk=question_id)
    c = Choice.objects.all()
    context = {"dsRequest" : c}
    #dulieu_inpuit = request.POST["choice"]
    #return HttpResponse(dulieu_inpuit)
    return render(request, "polls/Choice.html", context)
    