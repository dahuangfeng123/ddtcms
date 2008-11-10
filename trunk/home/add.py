from django.http import HttpResponse
from django.shortcuts import render_to_response


strhtml="""<form method="post" action="/add/">
    <input type="text" name="a" value="%d"> + <input type="text" name="b" value="%d">
    <input type="submit" value="="> <input type="text" value="%d">
</form>"""



def index(request):
    if request.POST.has_key('a'):
        a = int(request.POST['a'])
        b = int(request.POST['b'])
    else:
        a = 0
        b = 0
#    return HttpResponse(text % (a, b, a + b))
#    return HttpResponse("Hello, Django.")   
    helloworld= strhtml %  (a, b, a + b)
    return render_to_response('index.html',{'helloworld':helloworld })
    #return HttpResponse(helloworld)