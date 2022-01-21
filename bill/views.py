from django.shortcuts import render

"""import pyrebase

config = {
    'apiKey': "AIzaSyCBormMVUMr31f6EMTwISdgibvAC2bfCWI",
  'authDomain': "bill-zenetic.firebaseapp.com",
  'projectId': "bill-zenetic",
  'storageBucket': "bill-zenetic.appspot.com",
  'messagingSenderId': "271904151253",
  'appId': "1:271904151253:web:a84db283d7b0640fd6b45c",
  'measurementId': "G-V71R5SHKC3"

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def home(request):
    day = database.child('Data').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request, "Home.html", {"day": day, "id": id, "projectname": projectname})"""