from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name = 'dispatch')
class HomeView(View):
    def get(self, request):
        diaries = Diary.objects.filter(author = request.user)
        context = {
            'diaries' : diaries
        }
        return render(request, 'Diary/home.html', context)

@method_decorator(login_required, name = 'dispatch')
class DiaryCreateView(View):
    def get(self, request):
        form = DiaryForm(request.user)
        context = {
            'form' : form
        }
        return render(request, 'Diary/diary-create.html', context)

    def post(self, request):
        form = DiaryForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return redirect(request.path_info)        

@method_decorator(login_required, name = 'dispatch')
class DiaryRetrieveView(View):
    def get(self, request, pk):
        try:
            diary = Diary.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            chapters = Chapter.objects.filter(diary = diary).order_by('created_on') 
            context = {
                'diary' : diary,
                'chapters' : chapters
            }
            return render(request, 'Diary/diary-retrieve.html', context)

@method_decorator(login_required, name = 'dispatch')
class DiaryUpdateView(View):
    def get(self, request, pk):
        try:
            diary = Diary.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            form = DiaryForm(request.user, instance = diary)
            context = {
                'form' : form
            }
            return render(request, 'Diary/diary-update.html', context)

    def post(self, request, pk):
        try:
            diary = Diary.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            form = DiaryForm(request.user, instance = diary, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('/home/')
            else:
                return redirect(request.path_info)  

@method_decorator(login_required, name = 'dispatch')
class DiaryDeleteView(View):
    def get(self, request, pk):
        try:
            diary = Diary.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            diary.delete()
            return redirect('/home/')

@method_decorator(login_required, name = 'dispatch')
class ChapterCreateView(View):
    def get(self, request):
        form = ChapterForm(request.user)
        context = {
            'form' : form
        }
        return render(request, 'Diary/chapter-create.html', context)

    def post(self, request):
        form = ChapterForm(request.user, data = request.POST)
        if form.is_valid():
            print('chapter saved')
            instance = form.save()
            redirect_url = '/diary/' + str(instance.diary.id) + '/'
            return redirect(redirect_url)
        else:
            return redirect(request.path_info)      

@method_decorator(login_required, name = 'dispatch')
class ChapterRetrieveView(View):
    def get(self, request, pk):
        try:
            chapter = Chapter.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            context = {
                'chapter' : chapter
            }    
            return render(request, 'Diary/chapter-retrieve.html', context)

@method_decorator(login_required, name = 'dispatch')
class ChapterUpdateView(View):
    def get(self, request, pk):
        try:
            chapter = Chapter.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            form = ChapterForm(request.user, instance = chapter)
            context = {
                'form' : form
            }
            return render(request, 'Diary/chapter-update.html', context)

    def post(self, request, pk):        
        try:
            chapter = Chapter.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            form = ChapterForm(request.user, data = request.POST, instance = chapter)
            if form.is_valid():
                instance = form.save()
                redirect_url = '/chapter/' + str(instance.id) + '/'
                return redirect(redirect_url)
            else:
                return redirect(request.path_info)    

@method_decorator(login_required, name = 'dispatch')
class ChapterDeleteView(View):
    def get(self, request, pk):
        try:
            chapter = Chapter.objects.get(id = pk)
        except ObjectDoesNotExist:
            raise Http404    
        else:
            redirect_url = '/diary/' + str(chapter.diary.id) + '/'
            chapter.delete()
            return redirect(redirect_url)            