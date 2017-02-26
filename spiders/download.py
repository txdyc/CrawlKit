# coding: utf-8

import urllib2
from config import user_agents


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading: ', url
    headers = {'User-agents': user_agent}
    request = urllib2.Request(url, headers=headers)

    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None

        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries-1)

    return html
