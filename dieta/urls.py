from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nova_dieta/$', views.nova_dieta, name='nova_dieta'),
    url(r'^deletar_dieta/(?P<pk>\d+)/$', views.deletar_dieta, name='deletar_dieta'),

    url(r'^lista_dietas/$', views.lista_dietas, name='lista_dietas'),
    url(r'^detalhe_dieta/(?P<pk>\d+)/$', views.detalhe_dieta, name='detalhe_dieta'),
    url(r'^dieta_selecionada/(?P<pk>\d+)/$', views.dieta_selecionada, name='dieta_selecionada'),

    url(r'^salvar_dieta$', views.salvar_dieta, name='salvar_dieta'),
    url(r'^editar_dieta/(?P<pk>\d+)/$', views.editar_dieta, name='editar_dieta'),

    url(r'^seg_desjejum/(?P<pk>\d+)/$', views.seg_desjejum, name='seg_desjejum'),
    url(r'^add_desjejum_seg/(?P<pk>\d+)/$', views.add_desjejum_seg, name='add_desjejum_seg'),
    url(r'^del_desjejum_seg/(?P<pk>\d+)/$', views.del_desjejum_seg, name='del_desjejum_seg'),

    url(r'^seg_almoco/(?P<pk>\d+)/$', views.seg_almoco, name='seg_almoco'),
    url(r'^add_almoco_seg/(?P<pk>\d+)/$', views.add_almoco_seg, name='add_almoco_seg'),
    url(r'^del_almoco_seg/(?P<pk>\d+)/$', views.del_almoco_seg, name='del_almoco_seg'),
    url(r'^seg_jantar/(?P<pk>\d+)/$', views.seg_jantar, name='seg_jantar'),
    url(r'^add_jantar_seg/(?P<pk>\d+)/$', views.add_jantar_seg, name='add_jantar_seg'),
    url(r'^del_jantar_seg/(?P<pk>\d+)/$', views.del_jantar_seg, name='del_jantar_seg'),
    url(r'^seg_lanches/(?P<pk>\d+)/$', views.seg_lanches, name='seg_lanches'),
    url(r'^add_lanches_seg/(?P<pk>\d+)/$', views.add_lanches_seg, name='add_lanches_seg'),
    url(r'^del_lanches_seg/(?P<pk>\d+)/$', views.del_lanches_seg, name='del_lanches_seg'),

    url(r'^ter_desjejum/(?P<pk>\d+)/$', views.ter_desjejum, name='ter_desjejum'),
    url(r'^add_desjejum_ter/(?P<pk>\d+)/$', views.add_desjejum_ter, name='add_desjejum_ter'),
    url(r'^del_desjejum_ter/(?P<pk>\d+)/$', views.del_desjejum_ter, name='del_desjejum_ter'),
    url(r'^ter_almoco/(?P<pk>\d+)/$', views.ter_almoco, name='ter_almoco'),
    url(r'^add_almoco_ter/(?P<pk>\d+)/$', views.add_almoco_ter, name='add_almoco_ter'),
    url(r'^del_almoco_ter/(?P<pk>\d+)/$', views.del_almoco_ter, name='del_almoco_ter'),
    url(r'^ter_jantar/(?P<pk>\d+)/$', views.ter_jantar, name='ter_jantar'),
    url(r'^add_jantar_ter/(?P<pk>\d+)/$', views.add_jantar_ter, name='add_jantar_ter'),
    url(r'^del_jantar_ter/(?P<pk>\d+)/$', views.del_jantar_ter, name='del_jantar_ter'),
    url(r'^ter_lanches/(?P<pk>\d+)/$', views.ter_lanches, name='ter_lanches'),
    url(r'^add_lanches_ter/(?P<pk>\d+)/$', views.add_lanches_ter, name='add_lanches_ter'),
    url(r'^del_lanches_ter/(?P<pk>\d+)/$', views.del_lanches_ter, name='del_lanches_ter'),

    url(r'^qua_desjejum/(?P<pk>\d+)/$', views.qua_desjejum, name='qua_desjejum'),
    url(r'^add_desjejum_qua/(?P<pk>\d+)/$', views.add_desjejum_qua, name='add_desjejum_qua'),
    url(r'^del_desjejum_qua/(?P<pk>\d+)/$', views.del_desjejum_qua, name='del_desjejum_qua'),
    url(r'^qua_almoco/(?P<pk>\d+)/$', views.qua_almoco, name='qua_almoco'),
    url(r'^add_almoco_qua/(?P<pk>\d+)/$', views.add_almoco_qua, name='add_almoco_qua'),
    url(r'^del_almoco_qua/(?P<pk>\d+)/$', views.del_almoco_qua, name='del_almoco_qua'),
    url(r'^qua_jantar/(?P<pk>\d+)/$', views.qua_jantar, name='qua_jantar'),
    url(r'^add_jantar_qua/(?P<pk>\d+)/$', views.add_jantar_qua, name='add_jantar_qua'),
    url(r'^del_jantar_qua/(?P<pk>\d+)/$', views.del_jantar_qua, name='del_jantar_qua'),
    url(r'^qua_lanches/(?P<pk>\d+)/$', views.qua_lanches, name='qua_lanches'),
    url(r'^add_lanches_qua/(?P<pk>\d+)/$', views.add_lanches_qua, name='add_lanches_qua'),
    url(r'^del_lanches_qua/(?P<pk>\d+)/$', views.del_lanches_qua, name='del_lanches_qua'),

    url(r'^qui_desjejum/(?P<pk>\d+)/$', views.qui_desjejum, name='qui_desjejum'),
    url(r'^add_desjejum_qui/(?P<pk>\d+)/$', views.add_desjejum_qui, name='add_desjejum_qui'),
    url(r'^del_desjejum_qui/(?P<pk>\d+)/$', views.del_desjejum_qui, name='del_desjejum_qui'),
    url(r'^qui_almoco/(?P<pk>\d+)/$', views.qui_almoco, name='qui_almoco'),
    url(r'^add_almoco_qui/(?P<pk>\d+)/$', views.add_almoco_qui, name='add_almoco_qui'),
    url(r'^del_almoco_qui/(?P<pk>\d+)/$', views.del_almoco_qui, name='del_almoco_qui'),
    url(r'^qui_jantar/(?P<pk>\d+)/$', views.qui_jantar, name='qui_jantar'),
    url(r'^add_jantar_qui/(?P<pk>\d+)/$', views.add_jantar_qui, name='add_jantar_qui'),
    url(r'^del_jantar_qui/(?P<pk>\d+)/$', views.del_jantar_qui, name='del_jantar_qui'),
    url(r'^qui_lanches/(?P<pk>\d+)/$', views.qui_lanches, name='qui_lanches'),
    url(r'^add_lanches_qui/(?P<pk>\d+)/$', views.add_lanches_qui, name='add_lanches_qui'),
    url(r'^del_lanches_qui/(?P<pk>\d+)/$', views.del_lanches_qui, name='del_lanches_qui'),

    url(r'^sex_desjejum/(?P<pk>\d+)/$', views.sex_desjejum, name='sex_desjejum'),
    url(r'^add_desjejum_sex/(?P<pk>\d+)/$', views.add_desjejum_sex, name='add_desjejum_sex'),
    url(r'^del_desjejum_sex/(?P<pk>\d+)/$', views.del_desjejum_sex, name='del_desjejum_sex'),
    url(r'^sex_almoco/(?P<pk>\d+)/$', views.sex_almoco, name='sex_almoco'),
    url(r'^add_almoco_sex/(?P<pk>\d+)/$', views.add_almoco_sex, name='add_almoco_sex'),
    url(r'^del_almoco_sex/(?P<pk>\d+)/$', views.del_almoco_sex, name='del_almoco_sex'),
    url(r'^sex_jantar/(?P<pk>\d+)/$', views.sex_jantar, name='sex_jantar'),
    url(r'^add_jantar_sex/(?P<pk>\d+)/$', views.add_jantar_sex, name='add_jantar_sex'),
    url(r'^del_jantar_sex/(?P<pk>\d+)/$', views.del_jantar_sex, name='del_jantar_sex'),
    url(r'^sex_lanches/(?P<pk>\d+)/$', views.sex_lanches, name='sex_lanches'),
    url(r'^add_lanches_sex/(?P<pk>\d+)/$', views.add_lanches_sex, name='add_lanches_sex'),
    url(r'^del_lanches_sex/(?P<pk>\d+)/$', views.del_lanches_sex, name='del_lanches_sex'),

    url(r'^sab_desjejum/(?P<pk>\d+)/$', views.sab_desjejum, name='sab_desjejum'),
    url(r'^add_desjejum_sab/(?P<pk>\d+)/$', views.add_desjejum_sab, name='add_desjejum_sab'),
    url(r'^del_desjejum_sab/(?P<pk>\d+)/$', views.del_desjejum_sab, name='del_desjejum_sab'),
    url(r'^sab_almoco/(?P<pk>\d+)/$', views.sab_almoco, name='sab_almoco'),
    url(r'^add_almoco_sab/(?P<pk>\d+)/$', views.add_almoco_sab, name='add_almoco_sab'),
    url(r'^del_almoco_sab/(?P<pk>\d+)/$', views.del_almoco_sab, name='del_almoco_sab'),
    url(r'^sab_jantar/(?P<pk>\d+)/$', views.sab_jantar, name='sab_jantar'),
    url(r'^add_jantar_sab/(?P<pk>\d+)/$', views.add_jantar_sab, name='add_jantar_sab'),
    url(r'^del_jantar_sab/(?P<pk>\d+)/$', views.del_jantar_sab, name='del_jantar_sab'),
    url(r'^sab_lanches/(?P<pk>\d+)/$', views.sab_lanches, name='sab_lanches'),
    url(r'^add_lanches_sab/(?P<pk>\d+)/$', views.add_lanches_sab, name='add_lanches_sab'),
    url(r'^del_lanches_sab/(?P<pk>\d+)/$', views.del_lanches_sab, name='del_lanches_sab'),

    url(r'^dom_desjejum/(?P<pk>\d+)/$', views.dom_desjejum, name='dom_desjejum'),
    url(r'^add_desjejum_dom/(?P<pk>\d+)/$', views.add_desjejum_dom, name='add_desjejum_dom'),
    url(r'^del_desjejum_dom/(?P<pk>\d+)/$', views.del_desjejum_dom, name='del_desjejum_dom'),
    url(r'^dom_almoco/(?P<pk>\d+)/$', views.dom_almoco, name='dom_almoco'),
    url(r'^add_almoco_dom/(?P<pk>\d+)/$', views.add_almoco_dom, name='add_almoco_dom'),
    url(r'^del_almoco_dom/(?P<pk>\d+)/$', views.del_almoco_dom, name='del_almoco_dom'),
    url(r'^dom_jantar/(?P<pk>\d+)/$', views.dom_jantar, name='dom_jantar'),
    url(r'^add_jantar_dom/(?P<pk>\d+)/$', views.add_jantar_dom, name='add_jantar_dom'),
    url(r'^del_jantar_dom/(?P<pk>\d+)/$', views.del_jantar_dom, name='del_jantar_dom'),
    url(r'^dom_lanches/(?P<pk>\d+)/$', views.dom_lanches, name='dom_lanches'),
    url(r'^add_lanches_dom/(?P<pk>\d+)/$', views.add_lanches_dom, name='add_lanches_dom'),
    url(r'^del_lanches_dom/(?P<pk>\d+)/$', views.del_lanches_dom, name='del_lanches_dom'),
]
