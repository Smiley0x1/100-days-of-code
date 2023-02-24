from scapy.all import Ether, ARP, srp, sr1, IP, TCP, conf

from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)

def networkScan(gateWay):
    gateWay+="/24"
    arp = ARP(pdst=gateWay)
    
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

def portScan(ip,mac):
    common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 123: "NTP", 135: "Microsoft RPC", 143: "IMAP", 443: "HTTPS",
    465: "SMTPS", 587: "Submission", 636: "LDAPS", 993: "IMAPS", 995: "POP3S",
    1723: "PPTP", 3306: "MySQL", 3389: "RDP", 5900: "VNC", 8080: "HTTP Alternate",
    8443: "HTTPS Alternate", 8834: "Nessus", 10000: "Webmin", 11211: "Memcached",
    27017: "MongoDB", 27018: "MongoDB", 28017: "MongoDB", 50000: "DB2", 50070: "HDFS",
    50030: "HDFS", 50060: "HDFS", 50020: "HDFS", 50010: "HDFS", 6379: "Redis",
    8888: "Sun Web Server Admin", 6667: "IRC", 6697: "IRC SSL", 61616: "ActiveMQ",
    5672: "AMQP", 15672: "RabbitMQ management", 25672: "Erlang distribution", 4369: "epmd",
    5671: "AMQP over SSL", 15671: "RabbitMQ management over SSL", 25671: "Erlang distribution over SSL", 
    61613: "STOMP", 1883: "MQTT", 8883: "MQTT over SSL",
    161: "SNMP", 162: "SNMP Trap", 179: "BGP", 389: "LDAP", 427: "SLP", 443: "HTTPS",
    444: "SNPP", 445: "SMB", 548: "AFP", 631: "IPP", 636: "LDAPS", 989: "FTPS Data",
    990: "FTPS Control", 992: "Telnet over SSL", 993: "IMAP over SSL", 995: "POP3 over SSL",
    1025: "Microsoft RPC", 1026: "Windows Admin Shares", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "Microsoft SQL Server", 1434: "Microsoft SQL Monitor", 1701: "L2TP", 1718: "H.323 Gatekeeper",
    1719: "H.323 Call Control", 1720: "H.323 Host Call Control", 1723: "PPTP", 1812: "RADIUS Authentication",
    1813: "RADIUS Accounting", 1883: "MQTT", 1900: "UPnP", 2000: "Cisco SCCP", 2002: "Cisco ACS",
    2049: "NFS", 2121: "FTP Proxy", 2701: "Microsoft Exchange IMAP4", 2967: "Symantec AntiVirus",
    3050: "Firebird SQL", 3128: "Squid HTTP Proxy", 3306: "MySQL", 3389: "RDP", 3632: "Distributed Compiler Daemon",}

    openPorts=[]
    conf.verb = 0
    for i in common_ports.keys():
        src_port = 20
        SYNACK = 0x12
        tcp_connect = sr1(IP(dst=ip)/TCP(sport=src_port,dport=i,flags="S"),verbose=0,timeout=2)
        if tcp_connect==None:
            pass
        elif(tcp_connect.getlayer(TCP).flags == SYNACK):
            openPorts.append(i)
        else:
            pass
    if openPorts ==[]:
        result = str("IP:    " + ip + "    MAC Address:    " + mac)
        result +="    No Open Ports Found"
        return result
    else:
            result = str("IP:    " + ip + "    MAC Address:    " + mac + "    Open Ports:    ")
            for i in openPorts:
                result+=str( str(i) + " / " + common_ports[i] + ", ")
                
            result=str(result[0:len(result)-2])
            return result
    

def main(target):
    data = networkScan(target)
    ipopenports = []
    for i in data:
        ipopenports.append(portScan(i['ip'],i['mac']))
    return ipopenports

if __name__=="__main__":
    main()        
    
    