# modules
from flask import *
import ipaddress

# initialzing our app
app = Flask(__name__, template_folder='.')

@app.route("/", methods=['POST', 'GET'])
def index():
    # if post request
    post_req = False
    # get request
    if request.method == 'GET':
        # rendering template index.html
        return render_template("index.html", post_req=post_req)
    else:
        # getting the ip
        ip = request.form.get('ip')

        # getting all the details
        IP_Addr = ipaddress.ip_interface(ip)

        # Details
        Net_Addr = IP_Addr.network
        pref_len = IP_Addr.with_prefixlen
        Mask = IP_Addr.with_netmask
        wildcard = IP_Addr.hostmask
        broadcast_address = Net_Addr.broadcast_address

        # first octet (number/word) of ip
        first_octet = int(ip.split('.')[0])
        # class
        class_of_octet = ''

        # checking which class
        if first_octet >= 1 and first_octet <= 127:
            class_of_octet = "A"
        if first_octet >= 128 and first_octet <= 191:
            class_of_octet = "B"
        if first_octet >= 192 and first_octet <= 223:
            class_of_octet = "C"

        # first ip array
        array_first_ip = str(Net_Addr).split('.')
        # last ip array
        array_last_ip = str(broadcast_address).split('.')

        
        # first ip last octet
        first_ip_last_octet = int((str(Net_Addr).split('.')[3]).split('/')[0])
        # last ip last octet
        last_ip_last_octet = int((str(broadcast_address).split('.')[3]).split('/')[0])


        # usable host
        octet_of_hostable = int((str(Net_Addr).split('.')[3]).split('/')[1])
        useable_host = (2 ** (32 - octet_of_hostable)) - 2

        # our last ip and first ip
        last_ip = f'{array_last_ip[0]}.{array_last_ip[1]}.{array_last_ip[2]}.{last_ip_last_octet - 1}'
        first_ip = f'{array_first_ip[0]}.{array_first_ip[1]}.{array_first_ip[2]}.{first_ip_last_octet + 1}'

        return render_template("index.html", useable_host=useable_host, Net_Addr=str(Net_Addr).split('/')[0], pref_len=pref_len.split('/')[1], Mask=Mask.split('/')[1], wildcard=wildcard, broadcast_address=broadcast_address, post_req=True, first_ip=first_ip, last_ip=last_ip, classes=class_of_octet)