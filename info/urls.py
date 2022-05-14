from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('afkey/', views.afkey_view, name='afkey'),
    path('akazam/', views.akazam_view, name='akazam'),
    path('alakir/', views.alakir_view, name='alakir'),
    path('ezshra/', views.ezshra_view, name='ezshra'),
    path('cook/', views.cook_view, name='cook'),
    path('mukla/', views.mukla_view, name='mukla'),
    path('mutanus/', views.mutanus_view, name='mutanus'),
    path('tess/', views.tess_view, name='tess'),
    path('galewing/', views.galewing_view, name='galewing'),
    path('omu/', views.omu_view, name='omu'),
    path('scabbs/', views.scabbs_view, name='scabbs'),
    path('flurgl/', views.flurgl_view, name='flurgl'),
    path('zephy/', views.zephy_view, name='zephy'),
    path('chenvala/', views.chenvala_view, name='chenvala'),
    path('maiev/', views.maiev_view, name='maiev'),
    path('gally/', views.gally_view, name='gally'),
    path('elise/', views.elise_view, name='elise'),
    path('millhouse/', views.millhouse_view, name='millhouse'),
    path('galakrond/', views.galakrond_view, name='galakrond'),
    path('toki/', views.toki_view, name='toki'),
    path('darkmoon/', views.darkmoon_view, name='darkmoon'),
    path('rafam/', views.rafam_view, name='rafam'),
    path('guyen/', views.guyen_view, name='guyen'),
    path('george/', views.george_view, name='george'),
    path('voljin/', views.voljin_view, name='voljin'),
    path('xyrella/', views.xyrella_view, name='xyrella'),
    path('yoggsaron/', views.yoggsaron_view, name='yoggsaron'),
    path('kragg/', views.kragg_view, name='kragg'),
    path('yshra/', views.yshra_view, name='yshra'),
    path('hooktusk/', views.hooktusk_view, name='hooktusk'),
    path('douck/', views.douck_view, name='douck'),
    path('bran/', views.bran_view, name='bran'),
    path('malygos/', views.malygos_view, name='malygos'),
    path('deryl/', views.deryl_view, name='deryl'),
    path('jaraxus/', views.jaraxus_view, name='jaraxus'),
    path('faelin/', views.faelin_view, name='faelin'),
    path('dawngrasp/', views.dawngrasp_view, name='dawngrasp'),
    path('aranna/', views.aranna_view, name='aranna'),
    path('tickatus/', views.tickatus_view, name='tickatus'),
    path('nzoth/', views.nzoth_view, name='nzoth'),
    path('reno/', views.reno_view, name='reno'),
    path('nozdormu/', views.nozdormu_view, name='nozdormu'),
    path('finley/', views.finley_view, name='finley'),
    path('greybough/', views.greybough_view, name='greybough'),
    path('blackthorn/', views.blackthorn_view, name='blackthorn'),
    path('jandice/', views.jandice_view, name='jandice'),
    path('patches/', views.patches_view, name='patches'),
    path('lnistormcoil/', views.lnistormcoil_view, name='lnistormcoil'),
    path('sindragosa/', views.sindragosa_view, name='sindragosa'),
    path('lichking/', views.lichking_view, name='lichking'),
    path('sunstrider/', views.sunstrider_view, name='sunstrider'),
    path('brukan/', views.brukan_view, name='brukan'),
    path('barov/', views.barov_view, name='barov'),
    path('curator/', views.curator_view, name='curator'),
    path('alexstra/', views.alexstra_view, name='alexstra'),
    path('eudora/', views.eudora_view, name='eudora'),
    path('guff/', views.guff_view, name='guff'),
    path('deathwing/', views.deathwing_view, name='deathwing'),
    path('onyxia/', views.onyxia_view, name='onyxia'),
    path('saurfang/', views.saurfang_view, name='saurfang'),
    path('kurtrus/', views.kurtrus_view, name='kurtrus'),
    path('tamsin/', views.tamsin_view, name='tamsin'),
    path('tavshi/', views.tavshi_view, name='tavshi'),
    path('pyramad/', views.pyramad_view, name='pyramad'),
    path('cariel/', views.cariel_view, name='cariel'),
    path('rakanishu/', views.rakanishu_view, name='rakanishu'),
    path('ragnaros/', views.ragnaros_view, name='ragnaros'),
    path('vancleef/', views.vancleef_view, name='vancleef'),
    path('wagtoggle/', views.wagtoggle_view, name='wagtoggle'),
    path('rat/', views.rat_view, name='rat'),
    path('lich/', views.lich_view, name='lich'),
    path('millificent/', views.millificent_view, name='millificent'),
    path('biggles/', views.biggles_view, name='biggles'),
    path('ctun/', views.ctun_view, name='ctun'),
    path('patchwerk/', views.patchwerk_view, name='patchwerk'),
    path('yesera/', views.yesera_view, name='yesera'),
    path('illidan/', views.illidan_view, name='illidan'),
    path('vandir/', views.vandir_view, name='vandir'),
    path('sneed/', views.sneed_view, name='sneed'),
    path('drekthar/', views.drekthar_view, name='drekthar'),
    path('guide/', views.guide_view, name='guide'),

    path('type/', views.type_view, name='type'),

]