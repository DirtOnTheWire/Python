import psutil
import netsnmp

COMMUNITY_STRING = '<puppy>'
SNMP_PORT = 161
a_device = ('192.168.1.151', COMMUNITY_STRING, SNMP_PORT) 
def cpu():
    snmp_data = netsnmp.snmpgetbulk('.1.3.6.1.4.1.2021.11.9.0', '1','192.168.1.151','public')
    #snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.4.1.2021.11.9.0', display_errors=True)
    output = (snmp_data)
    a = output
    #a = "blarg"
    print (a)
    return "%2.2f" %a


def mem():
    snmp_data = netsnmp.snmpgetbulk('.1.3.6.1.4.1.2021.11.9.0', '1','192.168.1.151','public')
    #snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.4.1.2021.11.9.0', display_errors=True)
    output = (snmp_data)
    a = output
    #a = "blarg"
    print (a)
    return "%2.2f" %a

def dsk():
    snmp_data = netsnmp.snmpgetbulk('.1.3.6.1.4.1.2021.11.9.0', '1','192.168.1.151','public')
    #snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.4.1.2021.11.9.0', display_errors=True)
    output = (snmp_data)
    a = output
    #a = "blarg"
    print (a)
    return "%2.2f" %a
'''
def mem():
    a=psutil.phymem_usage().percent
    return "%2.2f" %a
def dsk():
    a=psutil.disk_partitions()
    b=[]
    x=0
    y=0
    for i in range (0,len(a)):
        b.append(a[i][1])
        x+=psutil.disk_usage(b[i])[0]
        y+=psutil.disk_usage(b[i])[1]
        z=float(y)/float(x)*100
    return "%2.2f" %z 
'''