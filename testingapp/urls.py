from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .models import post,photo
from .views import postDetailView, postListView,dashpostview,post_chart,save_location,add_to_favorites,favorite_list,liked_recipes,delete_image,Updaterecipeview,Deletepost,UpdatePassword,acc_settings, UpdateProfile,trendingview,customer_render_pdf_view,like_view,dislike_view
from .views import custom_cards,delete_account,year_recap,credits,cuisines
from .views import CustomPasswordResetView,CustomPasswordResetDoneView,CustomPasswordResetConfirmView,CustomPasswordResetCompleteView
from django.views.i18n import set_language



urlpatterns = [
    path('',views.landingpg,name="landingpg"),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('newnavbar_navrail',views.newnavbarnavrail,name="newnavbarnavrail"),
    
    path('explore/',postListView.as_view(),name="explore"),
    
    path('home/',dashpostview.as_view(),name="home"),
    
    path('login/',views.login_view,name="login"),   
    
    path('login_required/<pk>',views.topostlogin,name="topostlogin"),
    
    path('signup/',views.signup_view,name="signup"),
    
    path('logout/',views.logout_view,name="logout"),
    
    path('profile/',views.profile_view,name="profile"),
    
    path('newrecipe/',views.post_post_view,name="createpost"), 
    
    path('searchresults/',views.searchresults_view,name="searchresults"),
    
    path('aa/',views.aa_view,name="aa"), 
    
    path('recipe/<pk>',postDetailView.as_view(),name="viewpost"), #post
    
    path('post/comment',postDetailView.as_view(),name="comment"),

    path('like-view/',views.like_view,name="like-view"),
    
    path('dislike/',views.dislike_view,name="dislike-view"),

    # path('like/<int:pk>',views.like_view,name="likes"),

    # path('<first>_<last>/<pk>',views.userchannel,name="userchannelpage"),

    path('user_channel/<pk>',views.userchannel,name="userchannelpage"),

    path('dashboard',views.dashboard,name="dashboard"),

    path('post/<int:pk>/delete',Deletepost.as_view(),name="delete"),

    path('updaterecipe/<title>/<pk>',views.Updaterecipeview,name="updaterecipe"),
    
    path('delete_image/<int:image_pk>/', views.delete_image, name='delete_image'),

    path('updateprofile/',views.UpdateProfile,name="updateprofile"),
    
    path('changepassword/',UpdatePassword.as_view(),name="updatepassword"),

    path('account_settings/',views.acc_settings,name="account_settings"),

    path('liked_recipes/',views.liked_recipes,name="liked_recipes"),

    path('<feed>/<pk>/download pdf',views.customer_render_pdf_view,name="customerrender"),

    path('trending/',trendingview.as_view(),name="trending"),

    path('timeline/',views.timeline,name="timeline"),

    path('history/', views.blog_history, name='blog_history'),

    path('delete_entry/<pk>', views.delete_entry, name='delete_blog'),

    path('delete_entry/', views.bulk_delete_blogs, name='bulk_delete'),

    path('delete_account/', views.delete_account, name='delete_account'),

    path('recap/',views.year_recap,name="year_recap"),

    path('appearance',views.appearance,name="appearance"),

    path('reset_colors/', views.reset_colors, name='reset_colors'),

    path('reset_dark_theme/', views.reset_dark_theme, name='reset_dark'),

    path('new_color_palette/', views.default_color_palette1, name='dcp_1'),

    path('save_location/', save_location, name='save_location'),

    path('fav/<int:id>/', views.add_to_favorites, name='add_to_favorites'),

    path('favourites/', views.favorite_list, name='favourites'),

    path('post_chart/', views.post_chart, name='post_chart'),

    path('<slug>',views.custom_cards,name="custom_cards"),

    path('credits/',views.credits,name="credits"),

    path('<slug>/',views.cuisines,name="cuisines"),
]