from django.shortcuts import render
from events.models import Event
from django.utils import timezone
def home_page(request):
    now=timezone.now()
    
    active_hackathons=Event.objects.filter(
        is_approved=True,start_date__lt=now,end_date__gt=now
    )
    past_hackatons=Event.objects.filter(
        is_approved=True,
        end_date__lt=now
    )
    upcoming_hockatons=Event.objects.filter(
         is_approved=True,
         start_date__gt=now
    )
    # print(active_hackathons)
    return render(request,'home.html',context={
        'active_hackathons':active_hackathons,
        'past_hackatons':past_hackatons,
        'upcoming_hockatons':upcoming_hockatons,
        })