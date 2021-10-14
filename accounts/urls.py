from django.urls import path
from. import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('login', views.login_view,name='login'),
    path('logout', views.logout_view,name='logout'),
    path('doctor_home', views.doctor_home,name='DoctorHome'),
    path('addpatient', views.addpatient,name='AddPatient'),
    path('release', views.releasepatient,name='ReleasePatient'),
    path('patient_profile', views.releasepatient,name='PatientProfile'),
]