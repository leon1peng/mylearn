from django.conf.urls import url
from .views import index, add, homework, Detail, update_time_comment

urlpatterns = [
    url(r'index', index),
    url(r'add', add),
    url(r'homework', homework),
    url(r'add_return', index),
    url(r'detail/new', update_time_comment),
    url(r'detail/(\w+)', Detail.as_view()),
]
