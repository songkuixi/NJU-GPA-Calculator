from django.conf.urls import url

from . import views
from . import GradePoint

urlpatterns = [
    url(r'^(.*)$', GradePoint.getGPA),
]