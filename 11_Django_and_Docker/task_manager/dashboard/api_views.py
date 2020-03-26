from rest_framework import response, status, viewsets
from rest_framework.decorators import api_view

from dashboard import models
from dashboard import serializers


# @api_view(['GET', 'POST'])
# def project_list(request):
#     if request.method == 'GET':
#         qs = models.Project.objects.all()
#         serializer = serializers.ProjectSerializer(qs, many=True)
#         return response.Response(data=serializer.data)
#
#     elif request.method == 'POST':
#         serializer = serializers.ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(
#                 serializer.data, status=status.HTTP_201_CREATED)
#         return response.Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def project_detail(request, pk):
#     try:
#         obj = models.Project.objects.get(id=pk)
#     except models.Project.DoesNotExist:
#         return response.Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = serializers.ProjectSerializer(obj)
#         return response.Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = serializers.ProjectSerializer(obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data)
#         return response.Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         obj.delete()
#         return response.Response(status=status.HTTP_204_NO_CONTENT)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IssueSerializer
    queryset = models.Issue.objects.all()

