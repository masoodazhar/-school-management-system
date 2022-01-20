
from django.urls import path
from academic.views import SectionCreate, SectionUpdate,  SectionDelete
from .views import (
    StudentView,
    AttendanceMark,
    AttendanceSearch,
    AttendanceView,
    IndividualMarksView,
    AdmissionCreate, 
    AdmissionView, 
    AdmissionDelete, 
    AdmissionUpdate, 
    AdmissionDetail,
    StudentMarkSearch,
    StudentMarkCreate,
    MarkDistributionCreate,
    MarkDistributionUpdate,
    MarkDistributionDelete,
    ExamsView,
    ExamsDetail,
    ExamsCreate,
    ExamsUpdate,
    ExamsDelete,
    get_class_asignments,
    SendEmail_SaveData,
    SendEmailForExam,
    get_fee,
    get_subject_by_class,
    get_already_marks,
    getting_marks_from_calculated
    )


app_name = 'student'
urlpatterns = [
    path('', StudentView, name='student_view'),
    path('admission/create/', AdmissionCreate.as_view(), name='admission_create'),
    path('admission/view/', AdmissionView.as_view(), name='admission_view'),
    path('admission/view/<int:pk>/detail', AdmissionDetail.as_view(), name='admission_detail'),
    path('admission/view/<int:pk>/update', AdmissionUpdate.as_view(), name='admission_update'),
    path('admission/view/<int:pk>/delete', AdmissionDelete.as_view(), name='admission_delete'),
    path('createSection/', SectionCreate.as_view(), name='create_section'),
    path('updateSection/<int:pk>', SectionUpdate.as_view(), name='update_section'),
    path('deleteSection/<int:pk>/delete', SectionDelete.as_view(), name='delete_section'),
    path('viewexams/view', ExamsView.as_view(), name='view_exams'),
    path('createexams/', ExamsCreate.as_view(), name='create_exams'),
    path('detailexams/<int:pk>/detail', ExamsDetail.as_view(), name='detail_exams'),
    path('updateexams/<int:pk>/edit', ExamsUpdate.as_view(), name='update_exams'),
    path('deleteexams/<int:pk>/delete', ExamsDelete.as_view(), name='delete_exams'),
    path('SendEmail_SaveData/', SendEmail_SaveData, name='SendEmail_SaveData'),
    path('sendemailforexam/', SendEmailForExam.as_view(), name='sendemailforexam'),
    path('attendance/view', AttendanceView.as_view(), name='attendance_view'),
    path('attendance/search', AttendanceSearch.as_view(), name='attendance_search'),
    path('attendance/mark', AttendanceMark.as_view(), name='attendance_mark'),
    path('student_mark/search', StudentMarkSearch.as_view(), name='student_mark'),
    path('student_mark/add', StudentMarkCreate.as_view(), name='student_mark_add'),
    path('mark_distribution/create', MarkDistributionCreate.as_view(), name='mark_distribution_create'),
    path('mark_distribution/<int:pk>/update', MarkDistributionUpdate.as_view(), name='mark_distribution_update'),
    path('mark_distribution/<int:pk>/delete', MarkDistributionDelete.as_view(), name='mark_distribution_delete'),
    path('report/<int:student_name>/info', IndividualMarksView.as_view(), name='view_individual_marks'),    
    path('report/<int:student_name>/info?year&tab', IndividualMarksView.as_view(), name='view_individual_marks2'),    
    path('get_fee', get_fee, name="get_fee"),
    path('get_subject_by_class/', get_subject_by_class , name="get_subject_by_class"),
    path('get_already_marks/', get_already_marks , name="get_already_marks"),
    path('get_class_asignments/<int:pk>/class/<int:class_name>/subject/<int:subject>', get_class_asignments , name="get_class_asignments"),
    path('getting_marks_from_calculated/', getting_marks_from_calculated , name="getting_marks_from_calculated")
]