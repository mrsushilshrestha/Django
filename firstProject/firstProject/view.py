from django.http import HttpResponse

def about(request):
    myhtml="""
    <html>
    <marquee direction="right"><p>hello</p></marquee>
    
    </html>
    
    """
    return HttpResponse(myhtml)

def contact(request):
    return HttpResponse("This is Contact 98000")