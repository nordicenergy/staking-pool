from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from nordic_energy_pool.views import health, pools, deposit, balances, history, faq, pool, pool2, index, ajax_user_rewards, \
    ajax_user_events, ajax_user_pending, deposit2

urlpatterns = [
    url(r'^health/?', health),
    url(r'^history/?', history),
    url(r'^ajax_user_rewards/(?P<wallet>[^/]+)', ajax_user_rewards),
    url(r'^ajax_user_events/(?P<wallet>[^/]+)/(?P<pool>[^/]+)', ajax_user_events),
    url(r'^ajax_user_pending/(?P<wallet>[^/]+)/(?P<index>[^/]+)/(?P<pool>[^/]+)', ajax_user_pending),
    url(r'^nordic_energy-pool/deposit/?', deposit),
    url(r'^nordic_energy-pool2/deposit/?', deposit2),
    url(r'^balances/?', balances),
    url(r'nordic_energy-pool/', pool),
    url(r'nordic_energy-pool2/', pool2),
    url(r'pools/', pools),
    url(r'faq/', faq),
    url(r'^', index),
]

urlpatterns += staticfiles_urlpatterns()
