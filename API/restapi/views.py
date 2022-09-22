from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many = True)

    return Response({'status': 200, 'payload' : serializer.data})

class StudentAPI(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many = True)
        return Response({'status': 200, 'payload' : serializer.data})

    def put(self, request):
        pass

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
 
            serializer = StudentSerializer(data= request.data)
            if  not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'payload' : serializer.error, 'message': 'Something wend wrong'})

            serializer.save()
            return Response({'status': 200, 'payload' : serializer.data, 'message': 'Successful'})

        except Exception as e:
            return Response({'status': 403, 'message': 'Invalid Id'})

    def post(self, request):
        pass

    def delete(self, request):
        pass



# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)

#     return Response({'status': 200, 'payload' : serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data= request.data)

#     if  not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'payload' : data, 'message': 'Something wend wrong'})

#     serializer.save()
#     return Response({'status': 200, 'payload' : data, 'message': 'Successful'})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id = id)
 
#         serializer = StudentSerializer(data= request.data)
#         if  not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'payload' : serializer.error, 'message': 'Something wend wrong'})

#         serializer.save()
#         return Response({'status': 200, 'payload' : serializer.data, 'message': 'Successful'})

#     except Exception as e:
#         return Response({'status': 403, 'message': 'Invalid Id'})
        
