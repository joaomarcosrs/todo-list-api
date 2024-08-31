from . import views


routes_list = (
    (r'register', views.ResgisterViewSet, 'register'),
    (r'login', views.LoginViewSet, 'login'),
)