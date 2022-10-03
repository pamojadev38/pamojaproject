from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import VolunteerForm, MentorForm, MailListForm, ContactPageForm
from .models import ImageCategory, Volunteer, Post, ImageFile
from django.contrib import messages
from django.views.generic import CreateView

def home_view(request):
    if request.method == 'POST':
        form = MailListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email was submitted successfully')
            return redirect('mainapp:home')
    else:
        form = MailListForm()
    context = {'form':form}
    return render(request, 'mainapp/index.html', context)

def about_view(request):
    return render(request, 'mainapp/about.html')


########## Begining of Causes #############
def causes_view(request):
    return render(request, 'mainapp/causes.html')

def cause_detail_dreams(request):
    return render(request, 'mainapp/cause-dreams.html')

def cause_detail_ovc(request):
    return render(request, 'mainapp/cause-ovc.html')

def cause_child_sponsorship(request):
    return render(request, 'mainapp/cause-child-sponsorship.html')

def cause_detail_she_leads(request):
    return render(request, 'mainapp/cause-she-leads.html')

def cause_sustainable_livelihoods(request):
    return render(request, 'mainapp/cause-sustainable-livelihoods.html')

def cause_research(request):
    return render(request, 'mainapp/cause-research.html')

def cause_safe_water_projects(request):
    return render(request, 'mainapp/cause-safe-water-projects.html')

def cause_youth_center(request):
    return render(request, 'mainapp/cause-youth-center.html')




######### End of Causes ##################

def blog_view(request):
    return render(request, 'mainapp/blog.html')

def volunteer_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:volunteer')
    else:
        form = VolunteerForm()
    context = {'form':form} 
    return render(request, 'mainapp/volunteer.html', context)

def mentor_view(request):
    if request.method == 'POST':
        form = MentorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:mentor')
    else:
        form = MentorForm()
    context = {'form':form}
    return render(request, 'mainapp/mentor.html', context)

def impact_view(request):
    return render(request, 'mainapp/impact.html')

def gallery_view(request):
    images = ImageFile.objects.all()
    image_categories = ImageCategory.objects.all()
    context = {'images':images, 'image_categories':image_categories}
    return render(request, 'mainapp/gallery.html', context)

def gallery_detail(request, catego):
    images = ImageFile.objects.filter(category__category_name=catego)
    context = {'images':images, 'category': catego}
    return render(request, 'mainapp/gallery-detail.html', context)

def staff_view(request):
    return render(request, 'mainapp/staff.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactPageForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:contact')
    else:
        form = ContactPageForm()
    context = {'form':form}
    return render(request, 'mainapp/contact.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('mainapp:blog')