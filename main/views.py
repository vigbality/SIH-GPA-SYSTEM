import email
from django.shortcuts import redirect, render,HttpResponse
from flask import session
from .models import UserData
from datetime import datetime
import hashlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

now=datetime.now
parseDate=datetime.strptime
parseDate=datetime.strptime
sender_email="byeworld.sih@gmail.com"
password="byeworld69"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
message=[["Registartion Successful",'ByeWorld GPA System\n\n\nHey there User!\n\n\nYour Registration  is successful\n\nWelcome on-board!\n\nThanks and regards\nTeam ByeWorld\nbyeworld.sih@gmail.com'],
["Invalid password",'ByeWorld GPA System\n\n\nHey there User!\n\n the last attempt to login was unsuccessful. Too many wrong attempts might lock your account.\n\n\nFor any help logging in contact-  byeworld.sih@gmail.com \n\n\nThanks and regards\nTeam ByeWorld'],
["Account Locked",'ByeWorld GPA System\n\n\nHey there User!\n\nWrong password has been entered multiple times so your account is locked for the next 10 minutes .Try again later.\n\n\nFor any help logging in contact-  byeworld.sih@gmail.com \n\n\nThanks and regards\nTeam ByeWorld'],
["Login Successful",'ByeWorld GPA System\n\n\nHey there User!\n\nWelcome, Your login was successful.\n\n\nAny feedbacks to improve user experience or if you faced any problems logging in let us know through - byewrold.sih@gmail.com\n\n\nThanks and regards\nTeam ByeWorld']]

def sendMail(username,x,timeStamp):
    msg = MIMEMultipart()
    msg['Subject'] = message[x][0]
    msg['From'] = sender_email
    msg['To'] = username

    text = MIMEText(timeStamp+"\n\n"+message[x][1])
    msg.attach(text)
    try:
        server.sendmail(sender_email,username,msg.as_string())
    except:
        pass

def salt(raw_pwd):
    '''
    This function adds a fixed sequence of data
    to each password and then hashing it
    '''
    # creating a fixed 32-byte length salt
    # salt = hex(int("885e26c4b3e34067bd80cfd5e6cec4f3", 16))
    # salt='0x885e26c4b3e34067bd80cfd5e6cec4f3'
    # UTF-8 encoding
    salt=b'0x885e26c4b3e34067bd80cfd5e6cec4f3'

    # Generating hash object
    # sha256 : This hash function belong to hash class sha-2, the internal block size of it is 32 bits
    hash = hashlib.sha256(salt + raw_pwd.encode())

    # hash in  hexadecimal format
    return hash.hexdigest()



def index(request):
    if request.GET:
        return render(request,'main/index.html')
    elif request.POST:
        data=request.POST.dict()
        userEmail=data["email"]
        userType=data["type"]
        # print(userEmail)
        if userType=='Login':
            userObj=UserData.objects.filter(email=userEmail).first()
            if userObj==None:
                return render(request, "main/message.html",{'message':'Email is not registered with us, please sign up first :)'})
            else:
                request.session['email']=userEmail
                request.session['l']='1'
                return redirect('log1Page')
        elif userType=='Register':
            userObj=UserData.objects.filter(email=userEmail).first()
            if userObj != None:
                return render(request, "main/message.html",{'message':'Email already exists, please go ahead and login :)'})
            else:
                request.session['email']=userEmail
                request.session['r']='1'
                return redirect('reg1Page')
        else:
            return render(request,'main/index.html')
    else:
        return render(request,'main/index.html')



def reg1(request):
    if(request.POST):
        data=request.POST.dict()
        cat_chosen=data["cat"]
        request.session['r']='2'
        request.session['cat_chosen']=cat_chosen
        return redirect('reg2Page')
    else:
        try:
            rVal=request.session['r']
        except:
            rVal='0'

        if  rVal == '0':
            return redirect('indexPage')
        elif rVal == '1':
            return render(request,'main/category.html')
        else:
            return redirect('reg'+rVal+'Page')


def reg2(request):
    if(request.POST):
        data=request.POST.dict()
        if data['pwdValue']=='':
            return redirect('reg2Page')
        request.session['pwd1']=data['pwdValue']
        request.session['r']='3'
        print("\n\n\n-----------------------------",data['pwdValue'])
        return redirect('reg3Page')
    else:
        try:
            rVal=request.session['r']
        except: 
            rVal='0'

        if  rVal == '0':
            return redirect('indexPage')
        elif rVal == '2':
            return render(request, "main/choose-pwd.html",{'cat':request.session['cat_chosen']})
        else:
            return redirect('reg'+rVal+'Page')

def reg3(request):
    if(request.POST):
        data=request.POST.dict()
        if data['pwdValue']=='':
            return redirect('reg3Page')
        if request.session['pwd1']!=data['pwdValue']:
            request.session['r']='2'
            return render(request, "main/message.html",{'message':'Entered passwords did not match, try again :('})
        else:
            UserData(email=request.session['email'],pwd=salt(data['pwdValue']),failedAttempts=0,lastLoginTime=str(now())).save()
            sendMail(request.session['email'],0,str(now()))
            request.session['r']='0'
            request.session.flush()
            return render(request, "main/message.html",{'message':'Registration was successful!'})
    else:
        try:
            rVal=request.session['r']
        except: 
            rVal='0'

        if  rVal == '0':
            return redirect('indexPage')
        elif rVal == '3':
            return render(request, "main/confirm-pwd.html",{'cat':request.session['cat_chosen']})
        else:
            return redirect('reg'+rVal+'Page')


def log1(request):
    if(request.POST):
        data=request.POST.dict()
        cat_chosen=data["cat"]
        request.session['l']='2'
        request.session['cat_chosen']=cat_chosen
        return redirect('log2Page')
    else:
        try:
            lVal=request.session['l']
        except:
            lVal='0'

        if  lVal == '0':
            return redirect('indexPage')
        elif lVal == '1':
            userObj=UserData.objects.filter(email=request.session['email']).first()
            if userObj.failedAttempts==3:
                lastLogin=parseDate(userObj.lastLoginTime, '%Y-%m-%d %H:%M:%S.%f')
                currTime=now()
                secondsDiff=(currTime-lastLogin).seconds
                if secondsDiff > 600:
                    userObj.failedAttempts=0
                    userObj.save()
                    return render(request,'main/category.html')
                else:
                    minsLeft=secondsDiff//60
                    secsLeft=secondsDiff%60
                    request.session['l']='0'
                    return render(request, "main/message.html",{'message':'Try again after {0} mins and {1} secs!'.format(minsLeft,secsLeft)})
            else:
                return render(request,'main/category.html')
        else:
            return redirect('log'+lVal+'Page')

def log2(request):
    if(request.POST):
        userObj=UserData.objects.filter(email=request.session['email']).first()
        data=request.POST.dict()
        if data['pwdValue']=='':
            return redirect('log2Page')
        pwdInput=salt(data['pwdValue'])
        if pwdInput == userObj.pwd:
            sendMail(request.session['email'],3,str(now()))
            request.session['l']='0'
            request.session.flush()
            return render(request, "main/message.html",{'message':'Login was successful!'})
        else:
            if userObj.failedAttempts==2:
                userObj.failedAttempts=3
                userObj.lastLoginTime=str(now())
                userObj.save()
                sendMail(request.session['email'],2,str(now()))
                request.session['l']='0'
                request.session.flush()
                return render(request, "main/message.html",{'message':'Too many wrong attempts! Account locked for 10 mins!'})
            else:
                userObj.failedAttempts+=1
                userObj.lastLoginTime=str(now())
                userObj.save()
                sendMail(request.session['email'],1,str(now()))
                request.session['l']='0'
                request.session.flush()
                return render(request, "main/message.html",{'message':'Invalid password, {} attempts remaining!'.format(3-userObj.failedAttempts)})
           
    else:
        try:
            lVal=request.session['l']
        except: 
            lVal='0'

        if  lVal == '0':
            return redirect('indexPage')
        elif lVal == '2':
            return render(request, "main/confirm-pwdL.html",{'cat':request.session['cat_chosen']})
        else:
            return redirect('reg'+lVal+'Page')