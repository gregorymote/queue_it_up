from django.shortcuts import render

def start(request):
    if not request.session.session_key:
        request.session.create()
    sk = request.session.session_key
    print(sk)
    
    return render(request, 'start.html', {})