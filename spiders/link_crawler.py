# coding: urf-8

import re
import download
import urlparse
import robotparser
from libraries.throttle import *


def link_crawler(seed_url, link_regex, max_depth=2):
    """ Crawl from the given seed URL following links matched by link_regex """
    max_depth = 2
    crawl_queue = [seed_url]
    throttle = Throttle(delay)

    # keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restriction
        if check_robots(url, user_agent, robots_name='robots.txt'):
            throttle.wait(url)
            html = download.download(url, user_agent)

            # filter for links matching our regular expression
            for link in get_links(html):
                # check if link matches expected regex
                if re.match(link_regex, link):
                    # form absolute link
                    link = urlparse.urljoin(seed_url, link)
                    # check if have already seen thie link
                    if link not in seen:
                        seen.add(link)
                        crawl_queue.append(link)
        else:
            print 'Blocked by robots.txt: ', url


def get_links(html):
    """ Return a list of links from html """

    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>] +href=["\'](.*?)["\']', re.IGNORECASE)

    # list of all links from the webpage
    return webpage_regex.findall(html)


def check_robots(url, user_agent, robots_name='robots.txt'):
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, robots_name))
    rp.read()
    result = rp.can_fetch(user_agent, url)

    return result
