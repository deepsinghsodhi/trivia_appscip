from django.shortcuts import render
from django.views.generic import CreateView
from firstapp.models import Quizz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstapp.serializers import quizzserializer
from rest_framework import status
# Create your views here.

# this is default home page without giving any url.
def homepage(request):
    return render(request,'firstapp/homepage.html')


class QuizzView(CreateView): # inheriting the build in view to create form automatically : CreateView
    model = Quizz # name of the model
    fields = "__all__" # pick up all the fields from model and creates a form on HTMl Page.

#  Function Shows the current player game status.
def Result(request):
    result = Quizz.objects.all().order_by('-id')[0] # this will fetch the latest record from the model, in this way we can get the details of the current user
    return render(request,'firstapp/result.html',{'result':result}) # will render on the template with objects

# This function view will print complete history of quizz record.
def History(request):
    historydata = Quizz.objects.all().order_by('-created') # to fetch all data from Quizz model order_by created date (decreasing order)
    return render(request,'firstapp/history.html', {'historydata':historydata})   # will render to the specified template with the specified context object




                                # API Starts From Here ->>>>>>>>>>>>>>>

# GET AND POST FROM REST Frmaework
@api_view(['GET','POST'])
def QuizList(request):
    # GET is used to Read data:-
    if request.method == 'GET':
        obj = Quizz.objects.all() # all the data of game model is present in "obj" but in dictionary form
        serializer = quizzserializer(obj, many = True) # all the data present "obj" is coverted into JSON format & saves into serializer
        return Response(serializer.data) # this will return all data present in serializer

    # POST is used to insert New Data:-
    if request.method == 'POST':
        serializer = quizzserializer(data = request.data)
        if serializer.is_valid(): # Check wether the data is valid or not.
            serializer.save() # Save query of ORM
            return Response(serializer.data, status = status.HTTP_201_CREATED) # It will return a response of the action received successfully.
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) # Return 4XX Error if failed to fetch data or syntext error.



# function to get the data of any specific record corresponding to its id and converted
# into JSON format or dictionary.
@api_view(['GET','PUT','DELETE'])
def QuizDetail(request, pk):
    try:
        obj = Quizz.objects.get(id = pk) # only the data of specific id is present in the "obj" in dictionary format
    except Quizz.DoesNotExist: # if the entered id is not present in the model than this block will handle(except) the 404 error.
        return Response(status = status.HTTP_404_NOT_FOUND)

    # code to get the details of any specific game record by id (pk or primary key)
    if request.method == 'GET':
        serializer = quizzserializer(obj) # all the data present "obj" is coverted into JSON format & saves into serializer
        return Response(serializer.data) # this will return all data present in serializer

    # code to update game summary
    elif request.method == 'PUT':
        serializer = quizzserializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) #4XX Show Client Errer, It means Request containt incorrect syntext
                                                                                # and cannot be fullfilled

    # code to delete game record
    elif request.method == 'DELETE':
        obj.delete() #ORM Query to delete object or data.
        return Response(status=status.HTTP_200_OK) #2XX show the action was received successfully and, understoor and accepted.
