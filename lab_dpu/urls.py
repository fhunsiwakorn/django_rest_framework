from django.urls import path
from . import views
urlpatterns = [
    # path('member/', views.members),
    path('product/create/', views.ProjectCreate.as_view(), name='Product-Create'),
    path('product/list/<str:product_owner>',
         views.ProjectList, name='Product-List'),
    path('product/update/<int:pk>', views.ProjectUpdate.as_view(),
         name='Product-Update And Delete'),
]
