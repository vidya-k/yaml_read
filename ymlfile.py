import yaml
import urllib.parse
import sys

if len(sys.argv) < 2:
    raise Exception( "no parameter found")
       

serverIp=sys.argv[1]
stream = open("multi-tenancy.yaml", "r")
writestream = open("output.txt", "w")
ipMatched = False
docs = yaml.load_all(stream, yaml.FullLoader)
for doc in docs:
    if doc['groupName'] == serverIp:
         ipMatched = True
         for d in doc['tenantDataList']:
            writestream.write('db_naame='+d['uri'].split('//')[1].split(':')[2].split('/')[1] + '\n')
            writestream.write('db_ip='+d['uri'].split('//')[1].split(':')[1].split('@')[1].split(':')[0] + '\n')
            writestream.write('user_name=' +d['uri'].split('//')[1].split(':')[0]+ '\n')
            writestream.write('password='+urllib.parse.unquote(d['uri'].split('//')[1].split(':')[1].split('@')[0]) + '\n')
            writestream.write( '\n' + '-----------------------------------------' + '\n')
if ipMatched is False :
        raise Exception( "Wrong IP")