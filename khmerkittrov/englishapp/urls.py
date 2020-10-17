from django.urls import path
from . import views
from .views import ENGView, ENGDetailView

from newsapp.views import IndexView, ArticleDetailView
from aiapp.views import AIView, AIDetailView
from mathapp.views import MATHView, MATHDetailView
from pthnapp.views import PTHNView

urlpatterns = [
    path('', IndexView.as_view(), name= "news-page"),
    # path('news/<int:pk>/', ArticleDetailView.as_view(), name = "news-details"),

    path('english_course/', ENGView.as_view(), name='eng-course-page'),
    path('english_course/<int:pk>/', ENGDetailView.as_view(), name="eng-course-details"),
    path('english_course_search/', views.eng_search, name = 'eng-course-search-result-page'),
    path('english_course_chapter_list/', views.eng_chapter_list, name='eng-course-chapter-list-page'),
    path('english_course_chapter/<str:engcpt>/', views.eng_each_chapter, name='eng-course-each-chapter-page'),

    path('artificial_intelligence/', AIView.as_view(), name='ai-page'),
    path('mathematics/', MATHView.as_view(), name='math-page'),
    path('python/', PTHNView.as_view(), name='python-page'),

]
#Note:  For all the functions views.index, views.englishcourse, views.mathematics
#       views.artificialintelligence, and views.post, their () are dropped
#       when we dont need their default values
