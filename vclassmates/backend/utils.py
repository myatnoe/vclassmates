from ntlm.HTTPNtlmAuthHandler import HTTPNtlmAuthHandler
from html2text import html2text
import re
import urllib
import urllib2

def get_raw_html(sid, password, url):
    sid = "RP\\" + sid
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    ntlm_auth = HTTPNtlmAuthHandler(password_mgr)
    opener = urllib2.build_opener(ntlm_auth)
    urllib2.install_opener(opener)
    password_mgr.add_password(None, url, sid, password)
    return urllib2.urlopen(url).read()

def generate_image_url(sid, name):
    raw_url = "http://rp.edu.sg/staffdirectory/ShowImage.aspx?id=%s-%s.JPG" % (sid, name.upper())
    return urllib.quote(raw_url, '://?=')

def get_name_pairs(sid, password, url):
    
    NAME_RE_PATTERN = "\*\*(.*)\*\*"
    SID_RE_PATTERN = "mailto:(\d{5,6})@myrp"

    raw_html = get_raw_html(sid, password,url)
    formatted_string = html2text(raw_html)

    name_regex = re.compile(NAME_RE_PATTERN)
    sid_regex = re.compile(SID_RE_PATTERN)

    name_pairs = []
    for s in formatted_string.split('\n\n')[1:-5]:
        d = {}
        sid = sid_regex.search(s).group(1)
        d['sid'] = sid
        name = name_regex.search(s).group(1)
        d['name'] = name
        d['image_url'] = generate_image_url(sid, name)
        name_pairs.append(d)

    return name_pairs

def get_module_info(sid, password, url):
    """ helper method to get respective pairs of course ids and class codes"""
    
    CLASS_CODE_PATTERN = ">([A-Z][0-9][0-9][0-9]-\d-[A-Z]\d{2}[A-Z]-[ABC])"
    COURSEID_PATTERN = "template.asp\?courseid=(.{38})"

    c_re = re.compile(CLASS_CODE_PATTERN)
    cid_re = re.compile(COURSEID_PATTERN)

    raw_html = get_raw_html(sid, password, url)

    class_codes = c_re.findall(raw_html)
    courseids = c_re.findall(raw_html)[:-1]

    return zip(class_codes, courseids)

    
    



