# -*- coding:utf-8 -*-
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework import permissions

User = get_user_model()
# Create your views here.

# @csrf_exempt
# def snippet_list(request):
#     """
#     第一种方法:直接写一个def方法,我们队request的方法进行区别，如果为get就直接返回，如果为post，然后实现返回当前json字段
#     """
#     if request.method == 'GET':
#         snippet = Snippet.objects.all()  # 创建一个queryset，将当前的信息都搜索出来
#         serializer = SnippetSerializer(snippet, many=True)  # 创建一个序列化器
#         return JsonResponse(serializer.data, safe=False)  # 返回一个JsonResponse的对象
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)                    # Step 1.先从request中解析出来数据
#         serializer = SnippetSerializer(data=data)             # Step 2.使用序列器,将数据进行序列化，得到serializer
#         if serializer.is_valid():                             # Step 3.验证是否数据正常
#             serializer.save()                                 # Step 4.如果正常，保存数据
#             return JsonResponse(serializer.data, status=201)  # Step 5. 返回一个Json响应
#         return JsonResponse(serializer.errors, status=400)
#@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
    第一种方法,但是使用Response，因为Response里面有一个重要的方法,request.data \n
    旁支:不用JsonResponse，直接使用Response这个类 from rest_from.response import Response
    """
    if request.method == 'GET':
        snippets =Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class SnippetList(APIView):
#     """
#     第二种:使用类的方式实现，通过类里面的方法自动区分 get post put 等
#     List all snippets, or create a new snippet.
#     列出所有的snippet,通过post的时候还会保存一个新的snippet
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin, GenericAPIView):
#     """
#     第三种: 使用类，并通过使用mixin的混合多态，来实现 Retriver，update or delete a snippet instance.abs\n
#     搜索、更新、或者删除一个snippet的实例
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class SnippetList(generics.ListCreateAPIView):
    """
    第四种:我们直接Using generic class-based views ，使用通类的基类视图。 本次我们使用generics.
    ListCreateAPIView.\n
    第二种使用普通类，需要进行区分 def get,def post,继承自 APIView\n
    第三种，使用GenericAPIView和 mixins里面的ListModelMixin和CreateModelMixin\n
    """
    #定义当前的对象权限
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    '''这个地方是将当前创建的Snippet同当前登录用户绑定起来'''
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

############################################################################################################
###########下面实现的是 Snippet_detail                                            ###########################
############################################################################################################
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     第一种方法:直接写一个def方法,我们对request的方法进行区别，如果为get就直接返回，如果为post，然后实现返回当前json字段
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=400)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
#@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk, format=None):
    """
    第一种方法加工,但是使用Response，因为Response里面有一个重要的方法,request.data \n
    旁支:不用JsonResponse，直接使用Response这个类 from rest_from.response import Response \n
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data = request.data)
        if serializer.is_valid:
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
# class SnippetDetail(APIView):
#     """
#     第二种 使用类的方式来设计视图 \n
#     Retriver，update or delete a snippet instance.abs\n
#     搜索、更新、或者删除一个snippet的实例
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, fromat=None):
#         snippet = Snippet.objects.get(pk)  # 使用Django ORM Snippet.objects.get(pk)来找到对应的snippet
#         serializer = SinppetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         #snippet = Snippet.objects.get(pk)
#          snippet = self.get_object(pk)  # 这样就可以直接处理了，不用每个都需要使用Try ,except
#         serializer = SinppetSerializer(snippet, data = request.data)  #这个会调用 create(self, instalce , data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk, format=None):
#         snippet = Sinppet.objects.get(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
#     """
#     第三种: 使用类，并通过使用mixin的混合多态，来实现 
#     Retriver，update or delete a snippet instance.abs
#     搜索、更新、或者删除一个snippet的实例
#     """

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)   
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    第四种: 使用通用的基础类视图，Rest-framework，更进一步在混合类基础上，又省略了一步
    直接将list delete update 混到到了基础类视图中
    来实现Retriver，update or delete a snippet instance.abs
    搜索、更新、或者删除一个snippet的实例
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    """
    实现UserList的序列化，调用序列化器处理视图，
    def query_get():
        if request.method == 'GET:
            queryset = User.objects.all()
            serializer = UserSerializer(questset)
            return Response(serializer.data)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
############################################################################################################
###########  class UserDetail(generics.RetrieveAPIView)
############################################################################################################
class UserDetail(generics.RetrieveAPIView):
    """
    实现UserList的序列化，调用序列化器处理视图
    其实就是对 Put delete post进行处理
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

