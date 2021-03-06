from django.conf.urls import url

from slider import views

urlpatterns = [
    url(r'^create_page/$', views.create_page, name='create_page'),
    url(r'^create/$', views.create, name='create'),
    url(r'^home/$', views.home, name='slider_home'),
    url(r'^$', views.home, name='slider_home'),

    url(r'^detail/(?P<slider_id>[0-9]+)/$', views.detail, name='slider_detail'),
    url(r'^detail/$', views.home, name='home'),

    url(r'^image/(?P<slider_id>[0-9]+)/$', views.add_image_to_slider, name='add_image_to_slider'),
    url(r'^image/add/(?P<slider_id>[0-9]+)/$', views.add_image, name='add_image'),

    url(r'^ajax/remove/(?P<slider_id>[0-9]+)/(?P<image_id>[0-9]+)$', views.remove_image_from_slider, name='remove_image_from_slider'),
    url(r'^ajax/change_slider_status/$', views.switch_slider_status, name='switch slider status'),


    url(r'^ajax/change_slider_status/$', views.switch_slider_status, name='switch slider status'),

    # url(r'^show/(?P<hash>[A-Za-z0-9]+)/(?P<speed>[0-9]+)/$', views.slider_shower, name='show slider'),
    url(r'^show/(?P<hash>[A-Za-z0-9]+)/$', views.slider_shower, name='show slider'),

    url(r'^show_error/$', views.slider_show_error, name='show slider error'),

    url(r'^edit/(?P<slider_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^edit_action/(?P<slider_id>[0-9]+)/$', views.edit_action, name='edit action'),

    url(r'^remove_action/(?P<slider_id>[0-9]+)/$', views.remove_action, name='remove action'),

    url(r'^share/(?P<slider_id>[0-9]+)/$', views.share, name='share'),

    url(r'^code/$', views.code, name='code'),
    url(r'^code_action/$', views.code_action, name='code action'),



]
