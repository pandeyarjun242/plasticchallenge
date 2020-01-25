from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . models import Userdetails

# Create your views here.
bathroomParams =['detergents', 'shower', 'toohbrushes', 'toothpastes']
foodParams = ['petbottles', 'plasticbags','foodwrappers','yogurtcontainers']
newparams = ['plasticCups', 'straws', 'dispensableCutlery', 'plasticPlates']
params = ['petbottles', 'plasticbags','foodwrappers','yogurtcontainers', 'detergents', 'shower', 'toohbrushes', 'toothpastes','plasticCups', 'straws', 'dispensableCutlery', 'plasticPlates']

@login_required
def details(request):
    if request.method == 'POST':
            try:
              details = Userdetails.objects.get(user = request.user)
              details.delete()
              if request.POST['petbottles'] and request.POST['plasticbags'] and request.POST['straws'] and request.POST['shower'] and request.POST['yogurtcontainers']:
                  details = Userdetails()
                  details.petbottles = int(request.POST['petbottles'])
                  details.plasticbags = int(request.POST['plasticbags'])
                  details.foodwrappers = int(request.POST['foodwrappers'])
                  details.yogurtcontainers = int(request.POST['yogurtcontainers'])
                  details.detergents = int(request.POST['detergents'])
                  details.shower = int(request.POST['shower'])
                  details.toohbrushes = int(request.POST['toothbrushes'])
                  details.toothpastes = int(request.POST['toothpastes'])
                  details.plasticCups = int(request.POST['plasticCups'])
                  details.straws = int(request.POST['straws'])
                  details.dispensableCutlery = int(request.POST['dispensableCutlery'])
                  details.plasticPlates = int(request.POST['plasticPlates'])
                  details.saved = 0
                  details.user = request.user
                  details.save()
                  return render(request, 'index.html')
              else:
                  return render(request, 'details.html', {"error":"Please Fill in All Fields"})
            except:
             if request.POST['petbottles'] and request.POST['plasticbags'] and request.POST['straws'] and request.POST['shower'] and request.POST['yogurtcontainers']:
                 details = Userdetails()
                 details.petbottles = int(request.POST['petbottles'])
                 details.plasticbags = int(request.POST['plasticbags'])
                 details.foodwrappers = int(request.POST['foodwrappers'])
                 details.yogurtcontainers = int(request.POST['yogurtcontainers'])
                 details.detergents = int(request.POST['detergents'])
                 details.shower = int(request.POST['shower'])
                 details.toohbrushes = int(request.POST['toothbrushes'])
                 details.toothpastes = int(request.POST['toothpastes'])
                 details.plasticCups = int(request.POST['plasticCups'])
                 details.straws = int(request.POST['straws'])
                 details.dispensableCutlery = int(request.POST['dispensableCutlery'])
                 details.plasticPlates = int(request.POST['plasticPlates'])
                 details.user = request.user
                 details.save()
                 return render(request, 'index.html')
             else:
                 return render(request, 'details.html', {"error":"Please Fill in All Fields"})

    else:
        return render(request, 'details.html')
@login_required
def remove(request):
    if request.method == 'POST':
        details = Userdetails.objects.get(user = request.user)
        if request.POST['remove'] ==  params[0]:
            details.petbottles = 0
            details.save()
            details.saved += details.petbottles
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[1]:
            details.plasticbags = 0
            details.save()
            details.saved += details.plasticbags
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[2]:
            details.foodwrappers = 0
            details.save()
            details.saved += details.foodwrappers
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[3]:
            details.yogurtcontainers = 0
            details.save()
            details.saved+= details.yogurtcontainers
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[4]:
            details.detergents = 0
            details.save()
            details.saved+= details.detergents
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[5]:
            details.shower = 0
            details.save()
            details.saved+= details.shower
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[6]:
            details.toohbrushes = 0
            details.save()
            details.saved+= details.toohbrushes
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[7]:
            details.toothpastes = 0
            details.save()
            details.saved+= details.toothpastes
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[8]:
            details.plasticCups = 0
            details.save()
            details.saved+= details.plasticCups
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[9]:
            details.straws = 0
            details.save()
            details.saved+= details.straws
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[10]:
            details.dispensableCutlery = 0
            details.save()
            details.saved+= details.dispensableCutlery
            return render(request, 'index.html')
        elif request.POST['remove'] ==  params[11]:
            details.plasticPlates = 0
            details.save()
            details.saved+= details.plasticPlates
            return render(request, 'index.html')
@login_required
def dashboard(request):
    details = Userdetails.objects.get(user = request.user)
    total = 0
    return render(request, 'dashboard.html', {"details": details})
def startdiet(request):
    foodObj = {new_list: [] for new_list in foodParams}
    details = Userdetails.objects.get(user = request.user)
    total = 0
    if details.petbottles > 1:
        foodObj['petbottles'].append('PET Bottles')
        foodObj['petbottles'].append('yes')
        foodObj['petbottles'].append('PET bottles contain several harmful chemicals that get transferred to the water. Try exhausting your consumption and Using Steel Bottles')
        foodObj['petbottles'].append(details.petbottles*1.9)
        total += details.petbottles*1.9
    else:
        foodObj['petbottles'].append('PET Bottles')
        foodObj['petbottles'].append('No')
        foodObj['petbottles'].append('PET bottles contain several harmful chemicals that get transferred to the water. Try exhausting your consumption and Using Steel Bottles')
        foodObj['petbottles'].append(details.petbottles*1.9)
        total += details.petbottles*1.9
    if details.plasticbags > 3:
        foodObj['plasticbags'].append('Plastic Bags')
        foodObj['plasticbags'].append('Yes')
        foodObj['plasticbags'].append('Plastic Bags are the most abundant cause of water plastic pollution. Use cloth bags and Jute bags as alternatives')
        foodObj['plasticbags'].append(int(str(details.plasticbags * 1.2)[:1]))
        total += details.plasticbags * 1.2
    else:
        foodObj['plasticbags'].append('Plastic Bags')
        foodObj['plasticbags'].append('No')
        foodObj['plasticbags'].append('Plastic Bags are the most abundant cause of water plastic pollution. Use cloth bags and Jute bags as alternatives')
        foodObj['plasticbags'].append(int(str(details.plasticbags * 1.2)[:1]))
        total += details.plasticbags * 1.2
    if details.foodwrappers > 1:
        foodObj['foodwrappers'].append('Food Wrappers')
        foodObj['foodwrappers'].append('yes')
        foodObj['foodwrappers'].append('Food Wrappers are often unavoidable. Try mending your diet. Store all Food Wrappers and Start Making EcoBricks')
        foodObj['foodwrappers'].append(int(str(details.foodwrappers * 0.8)[:1]))
        total += details.foodwrappers*0.7
    else:
        foodObj['foodwrappers'].append('Food Wrappers')
        foodObj['foodwrappers'].append('No')
        foodObj['foodwrappers'].append('Food Wrappers are often unavoidable. Try mending your diet. Store all Food Wrappers and Start Making EcoBricks')
        foodObj['foodwrappers'].append(int(str(details.foodwrappers * 0.8)[:1]))
        total += details.foodwrappers*0.7
    if details.yogurtcontainers > 1:
        foodObj['yogurtcontainers'].append('Yogurt/Dairy Containers')
        foodObj['yogurtcontainers'].append('yes')
        foodObj['yogurtcontainers'].append('Yogurt/Dairy Containers can be cleaned and used to make EcoBricks. Start making one today!')
        foodObj['yogurtcontainers'].append(details.yogurtcontainers*0.8)
        total += details.yogurtcontainers*0.8
    else:
        foodObj['yogurtcontainers'].append('Yogurt Containers')
        foodObj['yogurtcontainers'].append('No')
        foodObj['yogurtcontainers'].append('Yogurt/Dairy Containers can be cleaned and used to make EcoBricks. Start making one today!')
        foodObj['yogurtcontainers'].append(details.yogurtcontainers*0.8)
        total += details.yogurtcontainers*0.8
    return render(request, 'foodkitchen.html', {"foodObj":foodObj})
def bathroom(request):
    details = Userdetails.objects.get(user = request.user)
    total = 0
    bathroomObj = {new_list: [] for new_list in bathroomParams}
    if details.detergents > 2:
        bathroomObj['detergents'].append('Detergents')
        bathroomObj['detergents'].append('yes')
        bathroomObj['detergents'].append('Use plastic free storage for detergents')
        bathroomObj['detergents'].append(details.detergents)
        total += details.detergents
    else:
        bathroomObj['detergents'].append('Detergents')
        bathroomObj['detergents'].append('No')
        bathroomObj['detergents'].append('Detergents')
        bathroomObj['detergents'].append(details.detergents)
        total += details.detergents
    if details.shower > 1:
        bathroomObj['shower'].append('Shower Equipment')
        bathroomObj['shower'].append('yes')
        bathroomObj['shower'].append('Shower Equipment')
        bathroomObj['shower'].append(int(str(details.shower * 0.9)[:1]))
        total += details.shower*0.9
    else:
        bathroomObj['shower'].append('Shower Equipment')
        bathroomObj['shower'].append('No')
        bathroomObj['shower'].append('Shower Equipment')
        bathroomObj['shower'].append(int(str(details.shower * 0.9)[:1]))
        total += details.shower*0.9
    if details.toohbrushes > 1:
        bathroomObj['toohbrushes'].append('Toothbrushes')
        bathroomObj['toohbrushes'].append('yes')
        bathroomObj['toohbrushes'].append('Toothbrushes')
        bathroomObj['toohbrushes'].append(int(str(details.toohbrushes * 1.1)[:1]))
        total += details.toohbrushes*1.1
    else:
        bathroomObj['toohbrushes'].append('Toothbrushes')
        bathroomObj['toohbrushes'].append('No')
        bathroomObj['toohbrushes'].append('Toothbrushes')
        bathroomObj['toohbrushes'].append(int(str(details.toohbrushes * 1.1)[:1]))
        total += details.toohbrushes*1.1
    if details.toothpastes > 1:
        bathroomObj['toothpastes'].append('Toothpastes')
        bathroomObj['toothpastes'].append('yes')
        bathroomObj['toothpastes'].append('Toothpastes')
        bathroomObj['toohbrushes'].append(int(str(details.toothpastes * 0.9)[:1]))
        total += details.toothpastes*0.9
    else:
        bathroomObj['toothpastes'].append('Toothpastes')
        bathroomObj['toothpastes'].append('No')
        bathroomObj['toothpastes'].append('Toothpastes')
        bathroomObj['toohbrushes'].append(int(str(details.toothpastes * 0.6)[:1]))
        total += details.toothpastes*0.9
    return render(request, 'bathroom.html', {"bathroomObj":bathroomObj})
def disposables(request):
    details = Userdetails.objects.get(user = request.user)
    total = 0
    recomObj = {new_list: [] for new_list in newparams}
    if details.plasticCups > 1:
        recomObj['plasticCups'].append('Plastic Cups/Utilities')
        recomObj['plasticCups'].append('yes')
        recomObj['plasticCups'].append('Plastic Cups, apart from the usual plastic cups, paper cups also have much usage of plastic Replace with bottles or steel glasses')
        recomObj['plasticCups'].append(int(str(details.plasticCups*2.1)[:1]))
        total += details.plasticCups*2.1
    else:
        recomObj['plasticCups'].append('Plastic Cups')
        recomObj['plasticCups'].append('No')
        recomObj['plasticCups'].append('Plastic Cups')
        recomObj['plasticCups'].append(int(str(details.plasticCups*2.1)[:1]))
        total += details.plasticCups*2.1
    if details.straws > 1:
        recomObj['straws'].append('Straws')
        recomObj['straws'].append('yes')
        recomObj['straws'].append('Straws')
        recomObj['straws'].append(int(str(details.straws*0.8)[:1]))
        total += details.straws*0.7
    else:
        recomObj['straws'].append('Straws')
        recomObj['straws'].append('No')
        recomObj['straws'].append('Straws')
        recomObj['straws'].append(int(str(details.straws*0.8)[:1]))
        total += details.straws*0.7
    if details.dispensableCutlery > 1:
        recomObj['dispensableCutlery'].append('Dispensables')
        recomObj['dispensableCutlery'].append('yes')
        recomObj['dispensableCutlery'].append('Dispensables')
        recomObj['dispensableCutlery'].append(int(str(details.dispensableCutlery)[:1]))
        total += details.dispensableCutlery
    else:
        recomObj['dispensableCutlery'].append('Dispensabless')
        recomObj['dispensableCutlery'].append('No')
        recomObj['dispensableCutlery'].append('Dispensables')
        recomObj['dispensableCutlery'].append(int(str(details.dispensableCutlery)[:1]))
        total += details.dispensableCutlery
    if details.plasticPlates > 1:
        recomObj['plasticPlates'].append('Plastic Plates')
        recomObj['plasticPlates'].append('yes')
        recomObj['plasticPlates'].append('Plastic Plates')
        recomObj['plasticPlates'].append(int(str(details.plasticPlates*0.4)[:1]))
        total += details.plasticPlates*0.4
    else:
        recomObj['plasticPlates'].append('Plastic Plates')
        recomObj['plasticPlates'].append('No')
        recomObj['plasticPlates'].append('Plastic Plates')
        recomObj['plasticPlates'].append(int(str(details.plasticPlates*0.4)[:1]))
        total += details.plasticPlates * 0.4
    return render(request, 'disposables.html', {"recomObj":recomObj})
