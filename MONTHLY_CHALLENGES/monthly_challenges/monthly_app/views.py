from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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
    "december" : "Make-A-List December",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<h1>Monthly Challenge</h1><ul>{list_items}</ul"
    return HttpResponse(response_data)
    


        
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
        response_data = f"<h1>{challenge}</h1>"
    except:
        response_data =f"<h1>Not a valid Month!!</h1>"
        return HttpResponseNotFound(response_data)
    
    return HttpResponse(response_data)
   
        


