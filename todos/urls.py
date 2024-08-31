from . import views


routes_list = (
    (r'todos', views.TodosViewSet, 'todos'),
)
