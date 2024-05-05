from django.urls import path
from .views import dashboard,course_view,course_add,course_update,course_delete

urlpatterns=[
    path('',dashboard,name="dashboard"),

    path('course/view/',course_view,name='course_view'),
    path('course/add/',course_add,name='course_add'),
    path('course/update/',course_update,name='course_update'),
    path('course/delete/',course_delete,name='course_delete'),
]

