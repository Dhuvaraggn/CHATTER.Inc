from django.shortcuts import render,redirect
from .models import Room,Member,Message,Accounts
from datetime import datetime
from itertools import chain
from .serializers import *

# Create your views here.
present_acc=Accounts()
def signup(request):
    
    return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        user_form=request.POST
        print(user_form)
        print('en')
        Accounts(user_form["Username"],user_form["Password"],user_form["Phoneno"]).save()
       # UserProfile('1001',password,datetime.now(),False,False,all,username,False,False,False,datetime.now(),phoneno).save()
        present_acc=Accounts(user_form["Username"],user_form["Password"],user_form["Phoneno"])
        print("Saved")
    return render(request,'login.html')
    
def enterroom(request):
    if request.method=='POST':
        log=request.POST
        print(log)
        if Accounts.objects.filter(phoneno=log["phoneno"],password=log["password"]).exists() :
            present_acc=Accounts.objects.get(phoneno=log["phoneno"])
            print(present_acc.name,present_acc.phoneno)
            sendd={'name':present_acc.name,'phone':present_acc.phoneno}
            print(sendd)
            return render(request,'enterroom.html', {'name':present_acc.name,'phone':present_acc.phoneno})
        else:
            return render(request,'login.html')

def newroom(request):
    dat=request.POST
    print(dat)
    return render(request,'newroom.html',{'phoneno':dat["phoneno"],'name':dat["name"]})

def roomcreate(request):
    if request.method=='POST':
        dict=request.POST
        print("check room is available")
        print(dict)
        if Room.objects.filter(roomid=dict["roomid"]).exists():
            print('already room exist')
            return render(request,'newroom.html',{'errti':'already exist','name':dict["name"],'phoneno':dict["phoneno"]})
        else:
            print('creating new room')
            Newmem=Member(dict["phoneno"],dict["name"])
            r=Room(roomid=dict["roomid"],roomname=dict["roomname"])
            r.save()
            startmsg=Message(rmid=r,msgfrom="chatter .inc",text="Your chatter room is created join with your friends.Enjoy!!!!")
            newmem=Member(room=r,phoneno=dict["phoneno"],nameofmem=dict["name"])
            startmsg.save()
            newmem.save()
            print('created')

            if Room.objects.filter(roomid=dict["roomid"]).exists():
                print('room present')
                msg=Room.objects.filter(roomid=dict["roomid"])[0]
                send=RoomSerializer(msg).data
                print("roomserial")
                print(send)
                msgs=msg.message_set.all()
                mems=msg.member_set.all()
                ms=[];me=[]
                for i in msgs:
                    msgsend=MessageSerializer(i).data
                    print(msgsend)
                    ms.append(msgsend)
                for j in mems:
                    memsend=MemberSerializer(j).data
                    print(memsend)
                    me.append(memsend)
                    print("end")
                return render(request,'room.html',{'name':dict["name"],'phone':dict["phoneno"],'roomid':send,'messages':ms,'members':me})
def rooms(request):
    print("started new msg")
    if request.method=='POST':
        check=request.POST
        ph=check["phoneno"]
        print(ph)
        print(check)   
        if check["newms"]:
            if Accounts.objects.filter(phoneno=int(check["phoneno"])).exists() :
                acc=Accounts.objects.get(phoneno=check["phoneno"])
                r=Room.objects.get(roomid=check["roomid"])   
                Message(id=None,rmid=r,msgfrom=acc.name,text=check["msgtosend"]).save()

            if Room.objects.filter(roomid=check["roomid"]).exists():
                print('room present')
                msg=Room.objects.filter(roomid=check["roomid"])[0]
                send=RoomSerializer(msg).data
                print("roomserial")
                print(send)
                msgs=msg.message_set.all()
                mems=msg.member_set.all()
                ms=[];me=[]
                for i in msgs:
                    msgsend=MessageSerializer(i).data
                    print(msgsend)
                    ms.append(msgsend)
                for j in mems:
                    memsend=MemberSerializer(j).data
                    print(memsend)
                    me.append(memsend)
                    print("end")
                return render(request,'room.html',{'name':acc.name,'phone':ph,'roomid':send,'messages':ms,'members':me})

def room(request):
    print("room")
    if request.method=='POST':
        check=request.POST
        ph=check["phoneno"]
        print(ph)
        print(check)
        if Room.objects.filter(roomid=check["roomid"]).exists():
            msg=Room.objects.filter(roomid=check["roomid"])[0]
            send=RoomSerializer(msg).data
            print("roomserial")
            print(send)
            if Member.objects.filter(room=check["roomid"],phoneno=check["phoneno"],nameofmem=check["name"]).exists():
                print("member already added")
            else:
                m=Member(room=msg,phoneno=check["phoneno"],nameofmem=check["name"])
                m.save()
                print("member saved")
            print('room present')
            
            msgs=msg.message_set.all()
            mems=msg.member_set.all()
            ms=[];me=[]
            for i in msgs:
                msgsend=MessageSerializer(i).data
                print("datae")
                print(datetime.now())
                print(msgsend["msgtime"])
                ms.append(msgsend)
            for j in mems:
                memsend=MemberSerializer(j).data
                print(memsend)
                me.append(memsend)
                print("end")
            print(me)
            return render(request,'room.html',{'name':check["name"],'phone':ph,'roomid':send,'messages':ms,'members':me})
        else:
            print('no room present')
            return render(request,'enterroom.html',{'errti':'Wrong roomid plz enter correct roomid or create new room id','name':check["name"],'phone':check["phoneno"]})

def members(request):
    if request.method=="POST":
        msg=request.POST
        print(msg)
        r=Room.objects.filter(roomid=msg["room"])[0]
        me=r.member_set.all()
        mems=[]
        for k in me:
            memse=MemberSerializer(k).data
            print(memse)
            mems.append(memse)

    return render(request,'members.html',{'members':mems})