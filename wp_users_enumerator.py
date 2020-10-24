#!/usr/bin/env python
import argparse
import json
import requests
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='WordPress users enumerator')
parser.add_argument('--target', metavar='url', help='URL ex: python wp_users_enumerator.py --target www.example.com/blog')
parser.add_argument('--output', metavar='output', help='File where save the request output')
args = parser.parse_args()

def method_1():  
  write_output = False
    
  if args.output is not None:
    write_output = True
    with open(args.output, "w") as output_file:
      output_file.write('Target: ' + args.target + '\n')

  try:
    print(bcolors.WARNING + ' Trying with WP Api...' + bcolors.ENDC)
    req = requests.get(url + '/wp-json/wp/v2/users')
    data = json.loads(req.content)
      
    if len(data) > 0:
      print(bcolors.OKGREEN + '\n ' + str(len(data)) + ' users found:' + bcolors.ENDC)
    else:
      print(bcolors.FAIL + '\n ' + str(len(data)) + ' users found:' + bcolors.ENDC)
   
    for user in data:
      print ' Name: ' + user['name']
      print ' Username: ' + user['slug'] + '\n'

      if write_output:
        with open(args.output, "a") as output_file:
          output_file.write('Name: ' + user['name'] + '\n')
          output_file.write('Username: ' + user['slug'] + '\n\n')
         
  except requests.ConnectionError as e:
    if 'Name or service not known' in str(e):
      print(bcolors.FAIL + ' Check the url.' + bcolors.ENDC)
    else:
      print(bcolors.FAIL + ' Connection error.' + bcolors.ENDC)

if __name__ == "__main__":
  if args.target is not None:
    if 'http' not in str(args.target):
      url = 'http://' + str(args.target)
    else:
      url = str(args.target)

    print(bcolors.HEADER + ' Enumerating users of ' + str(url) + bcolors.ENDC)
    method_1()
  else:
    print 'WordPress users enumerator'
    print 'ex: python wp_users_enumerator.py --target www.example.com/blog'

