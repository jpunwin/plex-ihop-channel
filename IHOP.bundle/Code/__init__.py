# -*- coding: utf-8 -*-
MAXRESULTS = 50
IHOP_FEED_URL = "http://feed.theplatform.com/f/IfSiAC/5ct7EYhhJs9Z/"
IHOP_FEED_QUERY = "?q=%s&range=0-%s&=&sort=pubDate|desc&count=true"
IHOP_FEED_FILT = "&byCustomValue={ihopkc$setType}{Intercession}"
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'
TITLE = L('IHOP')
ICON = 'icon-default.png'

####################################################################################################
def Start():
    HTTP.CacheTime = CACHE_1HOUR
    HTTP.Headers['User-Agent'] = USER_AGENT