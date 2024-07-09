from django.urls import path
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, Site
from viewflow.workflow.flow import FlowAppViewset
from my_pizza.flows import PizzaFlow

site = Site(
    title="Pizza Flow Demo",
    viewsets=[
        FlowAppViewset(PizzaFlow, icon="local_pizza"),
    ]
)

urlpatterns = [
    path("accounts/", AuthViewset().urls),
    path("", site.urls),
]
