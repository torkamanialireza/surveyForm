from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else :
        request.session['counter'] = 1
    print(request.session['counter'])
    return render(request,"surveyApp/index.html")
def process(request):
    if request.method == "POST":
        request.session['your_name'] = request.POST['your_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return redirect("/result")
def result(request):

    return render(request,"surveyApp/result.html")
def reset(request):
    request.session.clear()
    return redirect('/')
