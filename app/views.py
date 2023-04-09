from django.shortcuts import render, redirect
from .models import AnnounceBoard
from gtts import gTTS
import googletrans
import os
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# 언어 코드 리스트
languages = ['ko', 'en', 'zh-cn', 'ja', 'tl', 'vi', 'th']

# (한국어) 사용자 게시물 리스트(홈) 페이지
def index(request):
    # 게시물 리스트 최신순으로 요청
    postlist = AnnounceBoard.objects.all().order_by('-number')
    # 데이터베이스에 저장된 시간 형식을 바꿔서 저장
    for post in postlist:
        post.date_time = post.date_time.date
    # 요청하고 수정한 데이터 저장
    context = {
        'postlist': postlist
    }
    # index.html을 열 때 context에 저장된 데이터 사용
    return render(request, 'app/index.html', context)

# (한국어) 사용자 게시물 페이지
def board(request, tnum):
    # 게시물 번호에 맞는 데이터 요청
    post = AnnounceBoard.objects.get(number=tnum)
    # 해당 게시물의 시간 형식 변경
    post.date_time = post.date_time.date
    # 게시물 번호에 맞는 데이터 저장
    context = {
        'post': post,
    }
    # 게시물(board.html)을 열 때 context에 저장된 데이터 사용
    return render(request, 'app/board.html', context)

# (외국어) 사용자 게시물 리스트 페이지, 언어 코드(contrylang)에 맞는 언어 제공
def home_others(request, countrylang):
    # 게시물 리스트 최신순으로 요청
    postlist = AnnounceBoard.objects.all().order_by('-number')
    # Translator 클래스 객체 선언
    translator = googletrans.Translator()
    # 번역된 언어로 게시물 리스트에 재저장
    for post in postlist:
        # 게시물 제목 언어 코드에 맞는 언어로 번역
        transtitle = translator.translate(post.title, dest=countrylang)
        # 번역 후 저장
        post.title = transtitle.text
        # 시간 형식 변경
        post.date_time = post.date_time.date
    # 요청하고 수정(번역)한 데이터 저장
    context = {
        'postlist': postlist,
        'countrylang': countrylang,
    }
    # home_others.html을 열 때 context에 저장된 데이터 사용
    return render(request, 'app/home_others.html', context)
    
# (외국어) 사용자 게시물 페이지, 게시물 번호(tnum)에 맞는 게시물 및 언어 코드(contrylang)에 맞는 언어 제공 
def board_others(request, countrylang, tnum):
    # 게시물 번호에 맞는 데이터 요청
    post = AnnounceBoard.objects.get(number=tnum)
    # Translator 클래스 객체 선언
    translator = googletrans.Translator()
    # 게시물 제목과 내용 언어 코드에 맞게 번역
    transtitle = translator.translate(post.title, dest=countrylang)
    transtext = translator.translate(post.text, dest=countrylang)
    # 번역한 텍스트 저장
    post.title = transtitle.text
    post.text = transtext.text
    post.date_time = post.date_time.date
    # 게시물 번호에 맞고 수정(번역)한 데이터 저장
    context = {
        'post': post,
        'countrylang': countrylang,
    }
    # 게시물(board_others.html)을 열 때 context에 저장된 데이터 사용
    return render(request, 'app/board_others.html', context)

# 관리자 게시물 리스트 페이지
def admin_home(request):
    # 게시물 최신순 나열
    postlist = AnnounceBoard.objects.all().order_by('-number')
    # 시간 형식 변경
    for post in postlist:
        post.date_time = post.date_time.date
    # 수정한 데이터 저장
    context = {
        'postlist': postlist,
    }
    # admin_home.html을 열 때 context에 저장된 데이터 사용
    return render(request, 'app/admin_home.html', context)

# 관리자 게시물 생성 페이지
def admin_create(request):
    if request.method == "POST":
        post = AnnounceBoard()
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.save()
        
        translator = googletrans.Translator()
                
        for language in languages:
            transresult = translator.translate(post.text, dest=language)
            tts = gTTS(text=transresult.text, lang=language)    
            tts.save('%s.mp3' % os.path.join('./media/audio', "audio" + str(post.number) + "_" + language ))
    
        return redirect('admin_home')
    
    else:
        post = AnnounceBoard.objects.all()
        return render(request, 'app/admin_create.html', {'post': post})
    
def admin_fix(request, tnum):
    post = AnnounceBoard.objects.get(number=tnum)
    if 'create' in request.POST:
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.date_time = datetime.datetime.now()
        post.save()
        
        translator = googletrans.Translator()
                
        for language in languages:
            transresult = translator.translate(post.text, dest=language)
            tts = gTTS(text=transresult.text, lang=language)    
            tts.save('%s.mp3' % os.path.join('./media/audio', "audio" + str(post.number) + "_" + language ))

        return redirect('admin_home')
    
    elif 'delete' in request.POST:
        try:
            for language in languages:
                os.remove(os.path.join("./media/audio/audio"+ str(post.number) + "_" + language + ".mp3"))
        except:
            print('File error')
        post.delete()
        return redirect('admin_home')
    
    else:
        return render(request, 'app/admin_fix.html', {'post': post})

def admin_login(request):
    if request.method == "POST":
        input_id = request.POST['input_id']
        input_pw = request.POST['input_pw']
        user = auth.authenticate(request, username=input_id, password=input_pw)
        if user is not None:
            auth.login(request, user)
            return redirect('admin_home')
        else:
            return render(request, 'app/admin_login.html', {'error': 'ID 또는 비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'app/admin_login.html')

def admin_logout(request):
    auth.logout(request)
    return redirect('index')
