import re
import logging
import json

from heapq import nsmallest

LOG = logging.getLogger(__name__)

class AccessLog(object):
    def __init__(self):
        self.ip = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        self.date = re.compile('\[\s*(\d+/\D+/.*?)\]')
        self.request = re.compile('"([^"]*) HTTP/1.\d"')
        self.response = re.compile('HTTP\/1\.1\" ([0-9]{3})')
        self.size = re.compile('\d+ (\d+)')
        self.referrer = re.compile('"([^"]*)" \"')
        self.agent = re.compile('" "([^"]*)"')

    def access_file(self, file):
            try:
                with open(file) as f:
                    mystr = '\t'.join([l.strip() for l in f])
                    self.ip = re.findall(self.ip, mystr)
                    self.date = re.findall(self.date, mystr)
                    self.request = re.findall(self.request, mystr)
                    self.response = re.findall(self.response, mystr)
                    self.size = re.findall(self.size, mystr)
                    self.referrer = re.findall(self.referrer, mystr)
                    self.agent = re.findall(self.agent, mystr)
            except (IOError, OSError) as e:
                LOG.error(f'Error: {e}')

    def get_all(self):
        log = [ {
            'IP': self.ip,
            'Date': self.date,
            'Request': self.request,
            'Response': self.response,
            'Size': self.size,
            'Referrer': self.referrer,
            'Agent': self.agent
        } for self.ip, self.date, self.request, self.response,
           self.size, self.referrer, self.agent in zip(
               self.ip, self.date, self.request, self.response,
               self.size, self.referrer, self.agent)]

        return log

    def top_occurrence(self, field):
        log_list = self.get_all()
        d = {}
        top = {}
        for log_dict in log_list:
            ip = log_dict[field]
            if ip in d:
                d[ip] += 1
            else:
                d[ip] = 1
        for ref, occurnum in nsmallest(10, d.items(), key=lambda kv: (-kv[1], kv[0])):
            d1 = {ref: occurnum}
            top.update(d1)
            
        return json.dumps(top, indent=1)

    def total_bandwidth(self):
        band_in_bytes = sum(int(x) for x in self.size)
        band_in_mb = band_in_bytes/(1024*1024)
        band_in_gigs  = band_in_bytes/(1024*1024*1204)
        d = {'Bytes': band_in_bytes,
             'MB': band_in_mb,
             'GB': band_in_gigs}
        return json.dumps(d, indent=1)

