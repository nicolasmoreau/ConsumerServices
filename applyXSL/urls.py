from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.conf import settings

urlpatterns = patterns('applyXSL.views',
    (r'^(?P<xsl>\w+)/$', 'showForm'),
    (r'^(?P<xsl>\w+)/service$', 'receiveInput'),
    (r'^(?P<xsl>\w+)/result/(?P<rid>\w+)$', 'deliverResult'),
    (r'^(?P<xsl>\w+)/availability$', direct_to_template, {'template':'availability.xml','extra_context':{'deployurl':settings.DEPLOY_URL}}),    
    (r'^(?P<xsl>\w+)/capabilities$', direct_to_template, {'template':'capabilities.xml','extra_context':{'deployurl':settings.DEPLOY_URL, 'standardsversion':settings.VAMDC_STDS_VERSION}})
    )
