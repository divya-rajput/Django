from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Pack-A-Lunch January",
    "february" : "No-Eating-Out February",
    "march" : "$20 Fridays in March",
    "april" : "$10 Cash Envelope Saving Challenge in April",
    "may" : "Freezer and Pantry in May",
    "june" : "$2-A-Day in June",
    "july" : "Generic July",
    "august" : "Sell Two Items in August",
    "september" : "Decrease Your Bills in September",
    "october" : "Make Your Own Coffee October",
    "november" : "No-Spend November",
    "december" : None,
}
# "Make-A-List December"

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges_app/index.html",{
        "months":months,
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge",args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<h1>Monthly Challenge</h1><ul>{list_items}</ul"
    # return HttpResponse(response_data)
    


        
def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Not a valid Month!!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
def monthly_challenge(request,month):
    
    try: 
        challenge = monthly_challenges[month]

        return render(request,"challenges_app/challenge.html",{
            "month": month.capitalize(),
            "text": challenge,
        })
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    
    
   
        


