#
# This is completely borrow from django-mobile:
# https://github.com/gregmuellegger/django-mobile
#

import re

class MobileDetection(object):
    user_agents_test_match = (
        "w3c ", "acs-", "alav", "alca", "amoi", "audi",
        "avan", "benq", "bird", "blac", "blaz", "brew",
        "cell", "cldc", "cmd-", "dang", "doco", "eric",
        "hipt", "inno", "ipaq", "java", "jigs", "kddi",
        "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
        "maui", "maxo", "midp", "mits", "mmef", "mobi",
        "mot-", "moto", "mwbp", "nec-", "newt", "noki",
        "xda",  "palm", "pana", "pant", "phil", "play",
        "port", "prox", "qwap", "sage", "sams", "sany",
        "sch-", "sec-", "send", "seri", "sgh-", "shar",
        "sie-", "siem", "smal", "smar", "sony", "sph-",
        "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
        "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
        "wapi", "wapp", "wapr", "webc", "winw", "winw",
        "xda-",)
    user_agents_test_search = u"(?:%s)" % u'|'.join((
        'up.browser', 'up.link', 'mmp', 'symbian', 'smartphone', 'midp',
        'wap', 'phone', 'windows ce', 'pda', 'mobile', 'mini', 'palm',
        'netfront', 'opera mobi',
    ))
    user_agents_exception_search = u"(?:%s)" % u'|'.join((
        'ipad',
    ))
    http_accept_regex = re.compile(
        "application/vnd\.wap\.xhtml\+xml",
        re.IGNORECASE
    )

    def __init__(self, request):
        self.request = request
        user_agents_test_match = r'^(?:%s)' % '|'.join(
            self.user_agents_test_match
        )
        self.user_agents_test_match_regex = re.compile(
            user_agents_test_match, re.IGNORECASE
        )
        self.user_agents_test_search_regex = re.compile(
            self.user_agents_test_search, re.IGNORECASE
        )
        self.user_agents_exception_search_regex = re.compile(
            self.user_agents_exception_search, re.IGNORECASE
        )

    def __call__(self):
        return self.request.session.setdefault(
            'is_mobile', self.detect_mobile()
        )

    def detect_mobile(self):
        """Returns a boolean indicating if `self.request` was made from a mobile
        device.
        """
        if self.request.META.has_key('HTTP_USER_AGENT'):
            user_agent = self.request.META['HTTP_USER_AGENT']

            # Test common mobile values.
            if self.user_agents_test_search_regex.search(user_agent) and \
               not self.user_agents_exception_search_regex.search(user_agent):
                return True
            else:
                # Nokia like test for WAP browsers.
                # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension
                if self.request.META.has_key('HTTP_ACCEPT'):
                    http_accept = self.request.META['HTTP_ACCEPT']
                    if self.http_accept_regex.search(http_accept):
                        return True

            # Now we test the user_agent from a big list.
            if self.user_agents_test_match_regex.match(user_agent):
                return True

        return False
