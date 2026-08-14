from django.shortcuts import render


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")

        return render(
            request,
            "home.html",
            {
                "success": f"Thank you {name}! Your order has been received."
            }
        )

    return render(request, "home.html")


def thankyou(request):
    return render(request, "thankyou.html")

def contact(request):
    return render(request, 'contact.html')