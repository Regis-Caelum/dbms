import firebase_admin
from firebase_admin import credentials, firestore
import random
from datetime import datetime
import names
import math
from faker import Faker
fake = Faker()

n = int(input('Enter the Number of Records: '))

name = []
for i in range(n):
    name.append(names.get_full_name())

dob = []

for i in range(n):
    dob.append(str(fake.date_of_birth()))

age = []
for i in dob:  
    date_format = "%Y-%m-%d"
    a = datetime.strptime('2021-10-14', date_format)
    b = datetime.strptime(str(i), date_format)
    delta = a - b
    age.append(math.floor(delta.days/356.25))

address = []
for _ in range(n):
    address.append(str(fake.address()))

diseases = ["Galbanus Mollis (Soft Jaundice)"
,"Senilis Ilii (Ilium Weakness)"
,"Ignis Intermittens (Intermittent Burning)"
,"Abscessus Spissus (Dense Abscess)"
,"Perniciose Luteus (Yellow Pernicious)"
,"Morfirmus Acceciose"
,"Intesgina Pesrhagia"
,"Maties Angitium"
,"Privatas Galbus"
,"Apolitas Scorxia"
,"Catarrhus Bracium (Arm Catarrh)"
,"Contuses Pectus (Breast Bruised)"
,"Myelitis Senilis (Dry Paraplegia)"
,"Senilis Ulna (Elbow Weakness)"
,"Infectio Infantilis (Infantile Infection)"
,'Ambumus Vercinoma'
,"Scophuties Lesceptio"
,"Perisia Mararis"
,"Morsis Pernicus"
,"Hyrica Chopisis"]


cred = credentials.Certificate("/home/samsenpai/Desktop/RCOEM/V/DBMS/project/dbms/cred/dbms-cb3e4-firebase-adminsdk-g8ee3-bb05101dc0.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

for i in range(n):
    disease = random.choice(diseases)
    prev = [random.choice(diseases) for _ in range(random.randint(1, 5))]
    prev = list(dict.fromkeys(prev))
    prev = "\n".join(prev)
    prev = 'Suffered From:\n' + prev
    data = {
        u'active':True,
        u'Name':name[i],
        u'Age':age[i],
        u'Date of Birth':dob[i],
        u'Address':address[i],
        u'Disease':disease,
        u'Patient medical history':prev,
    }
    if(i < 300):
        db.collection(u'sam').add(data)
    elif(i >= 300 and i < 700):
        db.collection(u'daenerys').add(data)
    else:
        db.collection(u'jon').add(data)
