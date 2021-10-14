from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import firebase_admin
from firebase_admin import credentials, firestore
from .models import patients

cred = credentials.Certificate("/home/samsenpai/Desktop/RCOEM/V/DBMS/project/dbms/cred/dbms-cb3e4-firebase-adminsdk-g8ee3-bb05101dc0.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Create your views here.
def index(request):
    return render(request,'home.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username,password=password)

    if user is None:
        return redirect('Home')
    
    login(request, user)
    return redirect('DoctorHome')

def logout_view(request):
    logout(request)
    return redirect('Home')

def doctor_home(request):
    collection = db.collection(request.user.username)
    docs = collection.stream()

    patient=[]

    for doc in docs:
        temp = doc.to_dict()
        if temp['active'] == True:
            patient.append(patients(doc.id, temp['Name']))
    
    context = {
        'patients':patient,
    }

    return render(request, 'doctor_home.html',context=context)

def releasepatient(request):
    if request.method == 'POST':
        collection = db.collection(request.user.username)
        docs = collection.stream()

        patient=[]

        for doc in docs:
            temp = doc.to_dict()
            doc_id = str(doc.id)
            if doc_id == request.POST['doc_id']:
                data = {
                    u'active': False
                }
                temp = db.collection(request.user.username).document(doc_id).update(data)
            elif temp['active'] == True:
                patient.append(patients(doc_id, temp['Name']))
        
        context = {
            'patients':patient,
        }

        return render(request, 'doctor_home.html',context=context)

def addpatient(request):
    name = request.POST['name']
    age = request.POST['age']
    dob = request.POST['dob']
    address = request.POST['address']
    disease = request.POST['disease']
    prev = request.POST['prev']

    data = {
        u'active':True,
        u'Name':name,
        u'Age':age,
        u'Date of Birth':dob,
        u'Address':address,
        u'Disease':disease,
        u'Patient medical history':prev,
    }

    db.collection(request.user.username).add(data)
    return redirect('DoctorHome')



def patient_profile(request):
    if request.method == 'POST':
        doc = db.collection(request.user.username).document(request.POST['doc_id'])
        return render(request, 'patient_profile.html', context=doc.to_dict())
