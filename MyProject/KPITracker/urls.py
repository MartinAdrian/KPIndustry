from django.contrib.auth.views import LoginView
from django.urls import path, include
from KPITracker import views

app_name = "KPIndustry"

urlpatterns = [
    path("", include("django.contrib.auth.urls"), {"next_page": "/"}, name="login"),
    path("", views.LogIn.as_view(), name="login"),
    path("home/", views.HomeView.as_view(), name="homepage"),
    path("manage-users/", views.CreateUserView.as_view(), name="manage-users"),
    path("manage-users/<int:pk>/update/", views.UpdateUserView.as_view(), name="update-user"),
    path("manage-projects/<int:pk>/update/", views.UpdateProjectView.as_view(), name="update-project"),
    path("manage-projects/", views.CreateProjectsView.as_view(), name="manage-projects"),
    path("<int:pk>/deactivate/", views.deactivate_user, name="deactivate-user"),
    path("<int:pk>/finish/", views.finish_project, name="finish-project"),
    path("<int:pk>/reactivate/", views.reactivate_user, name="reactivate-user"),
    path("<int:pk>/reopen/", views.start_project, name="start-project"),
    path("view-projects/", views.ViewProjects.as_view(), name="view-projects"),
    path("<int:pk>/manage-project/", views.ManageProject.as_view(), name="manage-project"),
    path("<int:pId>/manage/<int:lId>/user-add/", views.add_user_to_project, name="user-add-project"),
    path("<int:pId>/manage/<int:lId>/user-rem/", views.rem_user_from_project, name="user-rem-project"),
    path("<int:pk>/manage/edit-desc/", views.EditDesc.as_view(), name="edit-desc-project"),
    path("<int:pk>/personal/", views.PersonalInfoView.as_view(), name="pers-view"),
    path("manage-locations", views.ManageLocations.as_view(), name="manage-locations"),
    path("password_reset", views.ResetPasswordView.as_view(), name="password_reset"),
    path("<int:pk>/daily-report", views.ReportCompleting.as_view(), name="daily-report"),
    # path("report-redirect", views.report_redirect(), name="report-redirect"),
]