from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Register, PressRelease,Event
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .forms import TalkForm
from django.shortcuts import redirect
from .models import Photo,Album
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail
import operator
from post_office import mail
#from post_office import mail, PRIORITY
from .tasks import user_send_activation_email , user_upload_activation_email
from endless_pagination.decorators import page_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    template = loader.get_template('home/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def album_list(request):
    album_choice = Album.objects.all()
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request, "talks/gallery.html", {'album_choice':album_choice,'events_recent':events_recent})

def photo_list(request,pk):

    album = get_object_or_404(Album, pk=pk)
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    pic = Photo.objects.filter(album = album)

    paginator = Paginator(pic, 8) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        pics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pics = paginator.page(paginator.num_pages)

    context = {
            "album" : album,
            "pics"  : pics,
            'events_recent':events_recent
            }
    return render(request, "talks/album_view.html", context)
    


def talks_list(request):
    talk = Register.objects.order_by('-date_and_time')

    paginator = Paginator(talk, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        talks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        talks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        talks = paginator.page(paginator.num_pages)

    return render(request, 'talks/talks_list.html', {'talks':talks})

def talk_new(request):
    if request.method == 'POST':
      form = TalkForm(request.POST, request.FILES)
      if form.is_valid():
         talk = form.save(commit=False)
         talk.author = request.user
         talk.save()
         user_send_activation_email.delay(user = request.user)
         #mail.send(request.user.email,settings.EMAIL_HOST_USER,subject='My email',message='Hi there!',html_message='Hi <strong>there</strong>!',)
         return redirect('talks_list')

    else:
      form = TalkForm()
    return render(request, 'talks/talk_edit.html', {'form': form})

def talks_detail(request):
   user = request.user
   talks = Register.objects.order_by('-date_and_time')
   return render(request, 'talks/talks_detail.html', {'talks':talks})

def talk_edit(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   if request.method == "POST":
      form = TalkForm(request.POST,request.FILES, instance=talk)
      if form.is_valid():
        form.save()
        user_upload_activation_email.delay(user = request.user)
        #send_mail('You Have Edited your talk', 'Confirmation mail', 'settings.EMAIL_HOST_USER',[request.user.email], fail_silently=False)
        #user_send_activation_email.delay(user = request.user)
        return redirect('talks_detail')
   else:
       form = TalkForm(instance=talk)
   return render(request, 'talks/talk_edit.html', {'form': form})

def talk_part(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   return render(request, 'talks/talk_part.html', {'talk': talk})


def release_unique(request,pk):
   pressrelease  = get_object_or_404(PressRelease, pk=pk)
   events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
   return render(request, 'pressrelease/release_unique.html', {'events_recent':events_recent,'pressrelease': pressrelease})

def pressrelease(request):
    pressreleases = PressRelease.objects.all().order_by('-date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request, 'pressrelease/pressrelease.html', {'pressreleases':pressreleases,'events_recent':events_recent})

def pressrelease_short(request):
    pressreleases = PressRelease.objects.order_by('-date')[:1]
    slider_photo= Photo.objects.all().order_by('id')[:4]
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')[:2]
    events=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request, 'pressrelease/slider.html', {'events_recent':events_recent,'events':events,'pressreleases':pressreleases ,'talks':talks, 'slider_photo':slider_photo})

def event(request):
    events=Event.objects.all().order_by('-date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request,'pressrelease/event.html',{'events':events,'events_recent':events_recent})

def base_footer(request):
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request,'talks/base.html', {'events_recent':events_recent})









































































