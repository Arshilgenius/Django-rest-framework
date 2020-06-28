from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('profiles/', views.profileList, name="profiles"),
    path('scribs/', views.scribList, name="scribs"),
    path('tags/', views.tagList, name="tags"),
    path('questions/', views.quesList, name="questions"),

    path('profiles/<int:pk>', views.profileListSingle, name="particular-profile"),
    path('scribs/<int:pk>', views.scribDetail, name="particular-scrib"),
    path('questions/<int:pk>', views.quesDetail, name="particular-question"),
    path('tags/<int:pk>', views.tagDetail, name="particular-tag"),

    path('addprofile/', views.profileAdd, name="add-profile"),
    path('addtag/', views.tagAdd, name="add-tag"),
    path('addscrib/', views.scribAdd, name="add-scrib"),
    path('addques/', views.quesAdd, name="add-ques"),

    path('votetag/<int:pk>', views.voteTag, name="vote-tag"),
    path('voteques/<int:pk>', views.voteQues, name="vote-tag"),

    path('deleteprofile/<str:pk>/', views.deleteProfile, name="delete-profile"),
    path('deletescrib/<str:pk>/', views.deletescrib, name="delete-scrib"),


    path('signup/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    # path('updateprofilelist/<str:pk>/', views.profileUpdate, name="update-profile-list"),

	# path('allusers/', views.userList, name="user-list"),
	# path('userupdate/<str:pk>/', views.userUpdate, name="user-update"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
