from html2text import html2text
import re
import urllib

def generate_image_url(sid, name):
    raw_url = "http://rp.sg/staffdirectory/ShowImage.aspx?id=%s-%s.JPG" % (sid, name)
    return urllib.urlquote(raw_url, '://?=')

def get_name_pairs(raw_string):

    NAME_RE_PATTERN = "\*\*(.*)\*\*"
    SID_RE_PATTERN = "mailto:(\d{5,6}@myrp)"

    formatted_string = html2text(raw_string)

    name_regex = re.compile(NAME_RE_PATTERN)
    sid_regex = re.compile(SID_RE_PATTERN)

    name_pairs = []
    for s in formatted_string.split('\n\n')[1:-5]:
        sid = sid_regex.search(s).group(1)
        name = name_regex.search(s).group(1)
        image_url = generate_image_url(sid, name)
        name_pairs.append((sid, name, image_url))

    return name_pairs

