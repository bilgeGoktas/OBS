"""obs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from obs.obs_student.views import StudentViewSet 
from obs.obs_student.views import UserViewSet 
from obs.obs_faculty.views import FacultyViewSet 
from obs.obs_advisor.views import AdvisorViewSet  
from obs.obs_lecturer.views import LecturerViewSet 
from obs.obs_announcement.views import AnnouncementViewSet
from obs.obs_course.views import CourseViewSet  
from obs.obs_department.views import DepartmentViewSet
from obs.obs_education_plan.views import EducationPlanViewSet
from obs.obs_management.views import ManagementViewSet
from obs.obs_offered_course.views import OfferedCourseViewSet
from obs.obs_register.views import RegisterViewSet
from obs.obs_register_note.views import RegisterNoteViewSet
from obs.obs_semester.views import SemesterViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet) 
router.register(r'users', UserViewSet) 
router.register(r'faculties', FacultyViewSet)
router.register(r'advisors', AdvisorViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'education_plans', EducationPlanViewSet)
router.register(r'managements', ManagementViewSet)
router.register(r'offered_courses', OfferedCourseViewSet)
router.register(r'registers', RegisterViewSet)
router.register(r'register_notes', RegisterNoteViewSet)
router.register(r'semesters', SemesterViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
