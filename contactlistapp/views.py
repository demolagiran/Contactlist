from django.shortcuts import render , redirect
from .forms import Contactform
from .models import Mycontact

def viewContacts(request):
    contacts = Mycontact.objects.all()
    return render(request, 'viewcontacts.html', {'contacts' : contacts})

def allContacts(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('viewContacts')
            except:
                pass
    else:
        form = Contactform()
        return render(request,'index.html',{'form' : form})

def editContact(request, pk):
    contact = Mycontact.objects.get(id = pk)
    return render(request, 'editcontact.html', {'contact' : contact})

def updateContact(request, pk):
    contact = Mycontact.objects.get(id = pk)
    updateForm = Contactform(instance=contact)
    if request.method == 'POST':
        updateForm = Contactform(request.POST, instance=contact)
        if updateForm.is_valid():
            updateForm.save()
        return redirect('viewContacts')
    return render(request, 'editcontact.html', {'contact' : contact, 'updateform' : updateForm})

def deleteContact(request, pk):
    contact = Mycontact.objects.get(id = pk)
    contact.delete()
    return redirect('viewContacts')
# Create your views here.