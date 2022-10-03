from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),

    ####### CAUSES #######
    path('causes', views.causes_view, name='causes'),
    path('cause-detail/dreams', views.cause_detail_dreams, name='cause-dreams'),
    path('cause-detail/ovc', views.cause_detail_ovc, name='cause-ovc'),
    path('cause-detail/she-leads', views.cause_detail_she_leads, name='cause-she-leads'),
    path('cause-detail/child-sponsorship', views.cause_child_sponsorship, name='child-sponsorship'),
    path('cause-detail/sustainable-livelihoods', views.cause_sustainable_livelihoods, name='sustainable-livelihoods'),
    path('cause-detail/research', views.cause_research, name='cause-research'),
    path('cause-detail/safe-water-projects', views.cause_safe_water_projects, name='cause-safe-water-projects'),
    path('cause-detail/youth-center', views.cause_youth_center, name='cause-youth-center'),
    ####### END OF CAUSES #######
    
    path('blog', views.blog_view, name='blog'),
    path('post', views.PostCreateView.as_view(template_name='mainapp/post.html'), name='write-a-post'),
    path('volunteer', views.volunteer_view, name='volunteer'),
    path('mentor', views.mentor_view, name='mentor'),
    path('impact', views.impact_view, name='impact'),
    path('gallery', views.gallery_view, name='gallery'),
    path('gallery/<str:catego>/', views.gallery_detail, name='gallery-detail'),
    path('staff', views.staff_view, name='staff'),
    path('contact', views.contact_view, name='contact'),

]