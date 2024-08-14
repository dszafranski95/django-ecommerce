from rest_framework import viewsets
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from allauth.account.views import LoginView, SignupView


class CustomLoginView(LoginView):
    template_name = "shop/login.html"  # Ustaw swój szablon logowania


class CustomSignupView(SignupView):
    template_name = "shop/register.html"  # Ustaw swój szablon rejestracji


def index(request):
    return render(request, "shop/index.html")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
