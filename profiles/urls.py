
from django.urls import path
from . import views
urlpatterns = [
        path("login/",views.user_login,name="user_login"),   
        path("signup/",views.user_signup,name="user_signup"),  
        path("logout/",views.user_logout,name="user_logout"),  
        path("profile/",views.user_profile.as_view(),name="user_profile"),  
        path("remove_cart/<int:id>",views.remove_cart,name="remove_cart"),  
        path("update-profile/",views.user_profile_edit,name="update_profile"),  
        path("update-pass/",views.password_update,name="update_pass"),  
]