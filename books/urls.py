from django.urls import path, include
from .views import BookListApi, \
    BookDetailApiView, BookUpdateApiView, \
    BookDeleteApiView, BookCreateApiView, BookListCreateApiView, BookUpdateDeleteApiView, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApi.as_view(),),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
    # path('booklistcreate', BookListCreateApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]
urlpatterns =urlpatterns + router.urls