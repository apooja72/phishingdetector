import re
import math
import numpy as np
from urllib.parse import urlparse

def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0
    probs = [text.count(c) / len(text) for c in set(text)]
    return -sum(p * math.log2(p) for p in probs)

def is_ip_address(url: str) -> int:
    return int(bool(re.search(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)))

def url_length(url: str) -> int:
    return len(url)

def count_special_chars(url: str) -> int:
    return len(re.findall(r'[@\-_=~%&]', url))

def count_digits(url: str) -> int:
    return sum(c.isdigit() for c in url)

def extract_domain(url: str) -> str:
    try:
        return urlparse(url).netloc
    except:
        return ""