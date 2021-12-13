from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from video.models import Category,Item,VideoComment
# Create your views here.
def categorylist(request):
    categories=Category.objects.all()
    context={"categories":categories} 
    return render(request,'video/categorylist.html',context)

def categoryvideos(request,slug):
    category=Category.objects.filter(slug=slug).first()
    catvideos=Item.objects.filter(category=category)
    context={'catvideos':catvideos}
    return render(request,'video/catvideo.html',context)

def videodetail(request,slug):
    video=Item.objects.filter(slug=slug).first()
    comments=VideoComment.objects.filter(video=video,parent=None)
    replies=VideoComment.objects.filter(video=video).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)
    context={"videos":video,'comments':comments,'user':request.user,'repDict':repDict}
    # print(comments)
    # print(repDict)
    return render(request,'video/videodetail.html',context)

def comments(request):
    
    videocomment=request.POST.get('commentbox')
    user=request.user
    videosno=request.POST.get('videoSno')
    video=Item.objects.get(id=videosno)
    parentSno=request.POST.get('parentSno')
    if parentSno=="":
        comment1=VideoComment(comment=videocomment,user=user,video=video)
        comment1.save()
        messages.success(request,"Your comment has been posted")
        return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))
    else:
        parent=VideoComment.objects.get(srno=parentSno)
        comment1=VideoComment(comment=videocomment,user=user,video=video,parent=parent)
        comment1.save()
        messages.success(request,"Your reply has been added")
        return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))