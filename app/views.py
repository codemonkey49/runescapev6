from django.shortcuts import render
from forms import componentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect


from models import *
# Create your views here.
def index(request):
    template="app/index.html"
    context={}
    
    tutorials=tutorialModel.objects.all()
    context["tutorials"]=tutorials
        
    
    return render(request,template,context)

def viewTutorial(request,tutorial):
    template="app/view.html"
    context={}
    
    tutorial=tutorialModel.objects.get(id=tutorial)
    context["tutorial"]=tutorial
    components=[]
    for i in tutorial.component.all().order_by("order"):
        components.append(i)
    context["components"]=components
    
    return render(request,template,context)

@staff_member_required    
def editTutorial(request,tutorial):
    template="app/edit.html"
    context={}
    
    #c1=componentModel(componentType="text",order=0,componentContent="this is the second tutorial")
    #c2=componentModel(componentType="text",order=1,componentContent="This comes second")
    #c3=componentModel(componentType="image",image="http://lazypenguins.com/wp-content/uploads/2015/08/Red-Panda-Surprise.jpg",imageCaption="this is a red panda")
    #c1.save()
    #c2.save()
    #c3.save()
    #t1=tutorialModel(title="how to do stuff2,electric boogaloo")
    #t1.save()
    #t1.component.add(c1,c2,)#c3)
    #t1.save()
    try:
        a=tutorial=tutorialModel.objects.get(id=tutorial)
    except:
        a=tutorialModel(title=tutorial)
    context["tutorial"]=a
    components=[]
    for i in a.component.all().order_by("order"):
        components.append(i)
        
    
    
    forms=[]
    for i in components:
        forms.append(componentForm(instance=i))
        
    
        
    context["components"]=components
    context["forms"]=forms
    zipList=zip(components,forms)
    context["zipList"]=zipList    

    
    
    return render(request,template,context)
@staff_member_required
def addComponent(request,tutorial):
        
        component=componentModel(order=0)
        component.save()
        
@staff_member_required    
def editComponent(request,primaryKey):
    try:
        component=componentModel.objects.filter(id=primaryKey)[0]
    except:
        component=componentModel(order=0)
        component.save()
    
    if request.method=="POST":
        form = componentForm(request.POST,instance=component)
        if form.is_valid:
            form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
