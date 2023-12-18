# 아파트 안내문 음성 안내 서비스

## 진행 기간 : 2021년 6월 28일 ~ 8월 23일

## 사용 기술
+ <img src ="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> - Programming Language
+ <img src ="https://img.shields.io/badge/django-%23092E20.svg?style=flat-square&logo=django&logoColor=white"/> - Python Web Framework
+ <img src ="https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white"/> - Database
+ <img src="https://img.shields.io/badge/Raspberry Pi-A22846?style=flat-square&logo=Raspberry Pi&logoColor=white"/> - LCD Touch Panel(Interface)
+ <img src="https://img.shields.io/badge/nginx-%23009639.svg?style=flat-square&logo=nginx&logoColor=white"/> <img src="https://img.shields.io/badge/uWSGI-%23009639.svg?style=flat-square&logo=uwsgi&logoColor=white"/> - Server

## 프로젝트 설명
+ 아파트에서 공고하는 게시물을 웹에서 음성으로 안내하는 시스템입니다.
+ 실제 아파트 게시판에 해당 기기를 설치하여 서비스를 제공하는 것을 목표로 한 프로젝트입니다.
+ 관리자는 로그인 기능을 통해 관리자 페이지로 접근하여 게시물(DB)을 관리합니다.
+ 사용자는 사용자 페이지에서 게시물에 접근하고 서비스(TTS 기능이 있는 게시물)를 제공 받습니다.
+ 한글로 제작한 해당 게시물에 대해 외국어 번역(총 7개국 언어)기능이 포함돼있어, 외국어로도 서비스를 제공합니다.
+ 해당 프로젝트는 라즈베리파이 파이썬 가상환경에서 Nginx, uWSGI를 통해 호스팅하여 웹사이트를 통해 제공합니다.

---
<summary><b> 기능 설명</b></summary>

### 1. 관리자 프로세스
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/admin-1.png"/>

### 1-1. 로그인 및 관리자 페이지 접근
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/admin-2.png"/>
  
### 1-2. 게시물, 음성파일 생성 및 DB 입력
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/admin-3.png"/>
  
### 1-3 게시물 수정 및 삭제, DB 수정
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/admin-4.png"/>
  
### 1-4. 데이터베이스
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/admin-5.png"/>
  
### 2. 사용자 프로세스
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/user-1.png"/>
  
### 2-1. 사이트 접근 및 게시물 선택
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/user-2.png"/>
  
### 2-2. 서비스 제공
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/user-3.png"/>

  
---
<details>
<summary><b> 실제 뷰 펼치기</b></summary>
<div markdown="1">

### 실제 서비스 과정(서버 실행 및 게시물 생성)
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/real_view_process.png"/>

### 실제 게시물 뷰
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/real_post_view.png"/>

### 게시물 생성 과정(파일 변경)
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/new_post_view.png"/>

### 게시물 삭제 과정(파일 변경)
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/delete_post_view.png"/>

### 전체 파일과 MariaDB
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/file_and_database_view.png"/>

### MySQL Workbench에서 본 데이터베이스
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/db_list_view.png"/>

### Nginx와 uWSGI를 활용한 서버 동작
<img src ="https://github.com/Mellowball/Voice-guidance-for-apartment-announcements/blob/main/Readme/uwsgi_com.png"/>


</details>
