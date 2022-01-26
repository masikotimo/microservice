import authentication._views.system_admin_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateSystemAdminViewSet.as_view({'post': 'create'})),
    path('', views.ViewSystemAdminsListViewSet.as_view(
        {'get': 'list'}), name="view_system_admin"),
    path(r'<str:id>/', views.RetrieveSystemAdminViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_system_admin"),
    path(r'<str:id>/update/',
         views.UpdateSystemAdminViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteSystemAdminViewSet.as_view({'delete': 'destroy'})),
]
