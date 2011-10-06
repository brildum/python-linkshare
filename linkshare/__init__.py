
import urllib2
from lxml import objectify

USER_AGENT = 'python-linkshare'
PRODUCT_SEARCH_URL = "http://productsearch.linksynergy.com/productsearch?token={0}"
RESULTS_URL = "{0}&MaxResults={1}&pagenumber={2}"

class API(object):
    def __init__(self, token='', max_results=20, **kwargs):
        self.token = token
        self.max_results = max_results

    def product_search(self, mid=None, keyword=None, cat=None, sorts=None, sorttypes=None):
        search_url_parts = [PRODUCT_SEARCH_URL.format(self.token)]
        if mid is not None:
            search_url_parts.append('mid={0}'.format(mid))
        if keyword is not None:
            search_url_parts.append('keyword={0}'.format(keyword))
        if cat is not None:
            search_url_parts.append('cat={0}'.format(cat))
        if sorts:
            if len(sorts) != len(sorttypes):
                raise ValueError("sorts sequence must be the same length as sorttypes sequence")
            for sort, sorttype in zip(sorts, sorttypes):
                search_url_parts.append('sort={0}&sorttype={1}'.format(sort, sorttype))
        search_url = '&'.join(search_url_parts)
        return _results_generator(search_url, self.max_results)

class MerchantAPI(API):
    def __init__(self, mid='', **kwargs):
        self.mid = mid
        API.__init__(self, **kwargs)

    def product_search(self, **kwargs):
        kwargs['mid'] = self.mid
        return API.product_search(self, **kwargs)

def _results_generator(base_url, max_results):
    page = 1
    opener = urllib2.build_opener()
    headers = {'User-Agent': USER_AGENT}
    while True:
        request = urllib2.Request(RESULTS_URL.format(base_url, max_results, page),
                headers=headers)
        result = objectify.parse(opener.open(request)).getroot()
        if hasattr(result, 'item'):
            for item in result.item:
                yield item
        else:
            break
        page += 1
