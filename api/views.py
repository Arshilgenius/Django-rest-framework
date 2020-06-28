from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile,Scrib,Ques,Tag
from .serializers import ProfileSerializer,QuesSerializer,ScribSerializer,TagSerializer


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		"Get All Scribbling":"/scribs/",
	    "Get All Tags":"/tags/",
		"Get All Profiles":"/profiles/",
		"Get All Questions":"/questions/",
		"Get Particular User Scribs":"/scribs/<idno>",
		"Get Particular User Tags":"/tags/<idno>",
		"Get Particular User Ques":"/questions/<idno>",
    	"Get Particular User Profile": "/profiles/<idno>",
    	"Add New Profile": "/addprofile/",
    	"Add New Tag": "/addtag/",
    	"Add New Scrib": "/addscrib/",
    	"Add New Ques": "/addques/",
		"Vote Tag": "/votetag/<id>",
		"Vote Ques": "/voteques/<id>",
    	"Update Profile": "/updateprofilelist/<id>",
    	"Delete Profile": "/deleteprofile/<idno>",
    	"Delete Scrib": "/deletescrib/<id>",

    	}
	return Response(api_urls)

""" _______________________________ GET  REQUESTS __________________________"""
@api_view(['GET'])
def profileList(request):
	profiles = Profile.objects.all()
	serializer = ProfileSerializer(profiles,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def scribList(request):
	scribs = Scrib.objects.all()
	serializer = ScribSerializer(scribs,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def quesList(request):
	ques = Ques.objects.all()
	serializer = QuesSerializer(ques,many=True)
	return Response(serializer.data)



@api_view(['GET'])
def tagList(request):
	tag = Tag.objects.all()
	serializer = TagSerializer(tag,many=True)
	return Response(serializer.data)




@api_view(['GET'])
def profileListSingle(request,pk):
	profile = Profile.objects.filter(idno=pk)
	serializer = ProfileSerializer(profile,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def scribDetail(request,pk):
	scribs = Scrib.objects.filter(to=pk)
	serializer = ScribSerializer(scribs,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def quesDetail(request,pk):
	ques = Ques.objects.filter(to=pk)
	serializer = QuesSerializer(ques,many=True)
	return Response(serializer.data)



@api_view(['GET'])
def tagDetail(request,pk):
	tag = Tag.objects.filter(to=pk)
	serializer = TagSerializer(tag,many=True)
	return Response(serializer.data)

""" ___________________________ POST REQUESTS _____________________________"""

@api_view(['POST','PUT'])
def tagAdd(request):
	serializer = TagSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data)


@api_view(['POST','PUT'])
def profileAdd(request):
	serializer = ProfileSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data)


@api_view(['POST','PUT'])
def scribAdd(request):
	serializer = ScribSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data)


@api_view(['POST','PUT'])
def quesAdd(request):
	serializer = QuesSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data)

""" _______________________UPDATE REQUEST ______________________"""



@api_view(['PATCH'])
def voteTag(request,pk):
	tag = Tag.objects.get(id=pk)
	serializer = TagSerializer(instance=tag,data=request.data,partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(request.data)



@api_view(['PATCH'])
def voteQues(request,pk):
	ques = Ques.objects.get(id=pk)
	serializer = QuesSerializer(instance=ques,data=request.data,partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(request.data)

# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()


# 	return Response(serializer.data)



# @api_view(['POST'])
# def taskUpdate(request,pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task,data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(request.data)

""" __________________  DELETE REQUESTS _________________________"""
@api_view(['DELETE'])
def deleteProfile(request,pk):
	profile = Profile.objects.get(idno=pk)
	profile.delete()

	return Response("deleted item")


@api_view(['DELETE'])
def deletescrib(request,pk):
	scrib = Scrib.objects.get(id=pk)
	scrib.delete()

	return Response("deleted item")
