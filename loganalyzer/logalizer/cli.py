import argparse

class ArgParse(object):
    def __init__(self):
        self.msg = ''' python main.py logfile option
                       example: python main.py access.log top ip
                   '''
        self.parser = argparse.ArgumentParser(prog='LOGANALYZER',
                                              description='Analyze log files', 
                                              usage=self.msg)

    def arg_options(self):
        parser = self.parser
        parser.add_argument('file', help = "log filename or path")
        parser.add_argument('action', help='',
                            choices=['top', 'bandwidth'])
        parser.add_argument('field', nargs="?", help='',
                            choices=['ip', 'status', 'request',
                                     'referrer', 'agent'])
        return parser.parse_args()

