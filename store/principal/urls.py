from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns=[
    path('',views.main, name="main"),
    path('informacion/',views.informacion, name="informacion"),
    path('mujer/',views.mujer, name="mujer"),
    path('hombre/',views.hombre, name="hombre"),
    path('diseños/',views.disenos, name="disenos"),
    path('registro/',views.registro,name='registro'),
    path('login/',views.registro,name='login'),
    path('producto/<int:producto_id>/',views.producto,name='producto'),
    path('crud/',views.lista_producto,name="crud" ),
    path('editar/<int:pk>',views.UpdateProducto.as_view(),name="editar" ),
    path('borrar/<int:pk>',views.deleteProducto.as_view(),name="borrar" ),
    path('ver/<int:producto_id>/', views.verProducto, name='ver'),
    path('nuevo/',views.crearProducto,name="view" ),
    

]

