from django.http import HttpResponse
def home_page(request):
    print("In home page")
    return HttpResponse("This is home page")