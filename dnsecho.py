#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
DNS Echo script
send a DNS request every second and print the output
=> equivalent of the icmp echo request but for testing DNS server

Author: Sebastian Metzner
'''

__author__ = 'Sebastian Metzner'
__version__ = '1.0'
__date__ = '2020-04'

# Modules
import argparse
import sys
import dns.resolver
import time

def main():
    
    # Arguments
    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser()
    parser.add_argument('foo', nargs='+')
    args = parser.parse_args()
    
    #print(args)
    
    #arguments = len(sys.argv)
    #print(arguments)
    
    # DNS resolve routine
    def_resolver = dns.resolver.Resolver()
    def_resolver.nameservers = ['172.30.20.107']
    dns_record = 'bla.zone04'
    # echo time intervall in seconds for dns request
    echo_intervall = 1
    print(echo_intervall)
    # count variable in while-loop
    i = 0
    
    # First Line Print for script
    print('DNS Echo every 1 second')
    while True:
        answer = def_resolver.query(dns_record, 'A')
        for data in answer:
            print(f'[{i}] The IP address for {dns_record} is: {data.address}')
        i += 1
        time.sleep(echo_intervall)


# Main
if __name__ == "__main__":
    #echo_intervall = 2
    #main(echo_intervall)
    main()
