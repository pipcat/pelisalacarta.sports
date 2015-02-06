# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para ustream
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os

from core import scrapertools
from core import logger
from core import config

DEBUG = config.get_setting("debug")

def find_url_play(data, headers):
    logger.info("[ustream.py] find_url_play")

    '''
<iframe width="700" height="450" src="http://www.ustream.tv/embed/19903720?v=3&amp;wmode=direct" scrolling="no" frameborder="0" style="border: 0px none transparent;"> </iframe>
    '''

    cid = scrapertools.find_single_match (data, 'src="http://www.ustream.tv/embed/([^\?]+)')
    if cid == '':
        #cid = scrapertools.find_single_match (data, "ustream.vars.contentId=['\"]([^'\"]+)")
        cid = scrapertools.find_single_match (data, "ustream.vars.channelId=['\"]([^'\"]+)")        
        if cid == '':
            return ''

    url = 'http://iphone-streaming.ustream.tv/uhls/%s/streams/live/iphone/playlist.m3u8' % cid

    return url
