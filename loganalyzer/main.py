import logging

from logalizer.cli import ArgParse
from logalizer.web import AccessLog

logging.basicConfig(format='%(message)s',
                    level=logging.INFO)

def main():
    args = ArgParse().arg_options()
    file = args.file
    access_log = AccessLog()
    access_log.access_file(file)
    if args.action == 'top' \
       and args.field == 'ip':
        logging.info(access_log.top_occurrence('IP'))
    if args.action == 'top' \
       and args.field == 'status':
        logging.info(access_log.top_occurrence('Response'))
    if args.action == 'top' \
        and args.field == 'request':
        logging.info(access_log.top_occurrence('Request'))
    if args.action == 'top' \
       and args.field == 'referrer':
        logging.info(access_log.top_occurrence('Referrer'))
    if args.action == 'top' \
       and args.field == 'agent':
        logging.info(access_log.top_occurrence('Agent'))
    if args.action == 'bandwidth':
        logging.info(access_log.total_bandwidth())
        

if __name__=="__main__":
    main()