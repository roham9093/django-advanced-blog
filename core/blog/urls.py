from django.urls import path , include

app_name = "blog"

urlpatterns = [
    # path('about/',indexView,name="fbv-test"),
    path('api/v1/',include('blog.api.v1.urls'))
]
