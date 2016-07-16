#!/usr/bin/env python

import multiprocessing, urllib2, argparse, sys, logging, datetime, time

def host_request(host):
    file = "identifiy_server.log"
    bufsize = 0
    e = open(file, 'a', bufsize)
    print("[*] Reading file %s") % (file)    
    print("[*] Testing %s") % (str(host))
    target = "http://" + host
    target_secure = "https://" + host
    timenow = time.time()
    record = datetime.datetime.fromtimestamp(timenow).strftime('%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(record)
    try:
        request = urllib2.Request(target)
        request.get_method = lambda : 'HEAD'
        response = urllib2.urlopen(request)
        response_data = str(response.info())
        e.write("[*] %s" % response_data)
        response.close()
    except:
        response = None
        response_data = None
    try:
        request_secure = urllib2.urlopen(target_secure)
        request_secure.get_method = lambda : 'HEAD'
        response_secure = str(urllib2.urlopen(request_secure).read())
        response_secure_data = str(response.info())
        e.write("[*] %s" % response_secure_data)
        response_secure.close()
    except:
        response_secure = None
        response_secure_data = None

    if response_data != None and response_secure_data != None:
        print("[*] Response from %s") % (str(target))
        print(response_data)
        print("[*] Response from %s") % (str(target_secure))
        print(response_secure_data)
    elif response_data == None and response_secure_data == None:
        print("[*] Response from %s") % (str(target))
        print(response_data)
        print("[*] Response from %s") % (str(target_secure))
        print(response_secure_data)
    elif response_data != None and response_secure_data == None:
        print("[*] Response from %s") % (str(target))
        print(response_data)
        print("[*] Response from %s") % (str(target_secure))
        print(response_secure_data)  
    elif response_secure_data != None and response_data == None:
        print("[*] Response from %s") % (str(target))
        print(response_data.info())
        print("[*] Response from %s") % (str(target_secure))
        print(response_secure_data)
    else:
        logger.debug("[-] No results were recorded for %s or %s" % (str(target), str(target_secure)))
        
    e.close()
    

def log_init(log):
    level = logging.DEBUG                                                                             # Logging level
    format = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s") # Log format
    logger_obj = logging.getLogger()                                                                  # Getter for logging agent
    file_handler = logging.FileHandler(log)                                                           # File Handler
    #stderr_handler = logging.StreamHandler()                                                          # STDERR Handler
    targets_list = []

    # Configure logger formats for STDERR and output file
    file_handler.setFormatter(format)
    #stderr_handler.setFormatter(format)

    # Configure logger object
    logger_obj.addHandler(file_handler)
    #logger_obj.addHandler(stderr_handler)
    logger_obj.setLevel(level)

def main():
    usage = '''usage: %(prog)s [-t hostfile] [-m processes] [-f filename] [-l logfile.log] [-m 2]'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-t", action="store", dest="targets", default=None, help="Filename for hosts to test")
    parser.add_argument("-f", "--filename", type=str, action="store", dest="filename", default="xml_output", help="The filename that will be used to create an XLSX")
    parser.add_argument("-m", "--multi", action="store", dest="processes", default=1, type=int, help="Number of proceses, defaults to 1")
    parser.add_argument("-l", "--logfile", action="store", dest="log", default="results.log", type=str, help="The log file to output the results")
    args = parser.parse_args()

    # Argument Validator
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if (args.targets == None):
        parser.print_help()
        sys.exit(1)

    # Set Constructors
    targets = args.targets                                                                            # Targets to be parsed
    processes = args.processes                                                                        # processes to be used
    log = args.log                                                                                    # Configure the log output file
    if ".log" not in log:
        log = log + ".log"

    # Load the targets into a list and remove trailing "\n"
    with open(targets) as f:
        targets_list = [line.rstrip() for line in f.readlines()]

    # Establish thread list
    pool = multiprocessing.Pool(processes=processes, initializer=log_init(log))

    # Queue up the targets to assess
    pool.map(host_request, targets_list)

if __name__ == '__main__':
    main()
