from django.contrib.auth.views import LoginView
from django.urls import path, include
from KPITracker import views

app_name = "KPIndustry"

urlpatterns = [
    path("", include("django.contrib.auth.urls"), {"next_page": "/"}, name="login"),
    path("", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("home/", views.HomeView.as_view(), name="homepage"),
    path("manage-users/", views.CreateUserView.as_view(), name="manage-users"),
    path("manage-users/<int:pk>/update/", views.UpdateUserView.as_view(), name="update-user"),
    path("manage-projects/<int:pk>/update/", views.UpdateProjectView.as_view(), name="update-project"),
    path("manage-projects/", views.CreateProjectsView.as_view(), name="manage-projects"),
    path("<int:pk>/deactivate/", views.deactivate_user, name="deactivate-user"),
    path("<int:pk>/finish/", views.finish_project, name="finish-project"),
    path("<int:pk>/reactivate/", views.reactivate_user, name="reactivate-user"),
    path("<int:pk>/reopen/", views.reopen_project, name="reopen-project"),
    path("view-projects/", views.ViewProjects.as_view(), name="view-projects"),
    path("<int:pk>/manage/", views.ManageProject.as_view(), name="manage-project"),
    path("<int:pId>/manage/<int:lId>/lt-add/", views.add_lead_to_project, name="lead-add-project"),
    path("<int:pId>/manage/<int:lId>/lt-rem/", views.rem_lead_to_project, name="lead-rem-project"),
]