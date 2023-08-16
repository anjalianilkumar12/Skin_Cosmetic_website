from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('home',views.homeview,name='home'),
    path('pro',views.categoryview,name='pro'),
    path('cat/<int:id>',views.productview,name='cat'),
    path('contact',views.contactview,name='contact'),
    path('brand',views.Brandview,name='brand'),
    path('brands/<int:id>',views.branddetail,name='brands'),
    path('about',views.aboutview,name='about'),
   
    #path('product',views.cat,name='product')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)