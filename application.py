from flask import *
import ipaddress

app = Flask(__name__, template_folder='.')

@app.route("/", methods=['POST', 'GET'])
def index():
    variable = False
    if request.method == 'GET':
        return render_template("index.html", variable=variable)
    else:
        ip = request.form.get('ip')

        IP_Addr = ipaddress.ip_interface(ip)

        Net_Addr = IP_Addr.network
        pref_len = IP_Addr.with_prefixlen
        Mask = IP_Addr.with_netmask
        wildcard = IP_Addr.hostmask
        broadcast_address = Net_Addr.broadcast_address

        first_octet = int(ip.split('.')[0])
        class_of_octet = ''

        if first_octet >= 1 and first_octet <= 127:
            class_of_octet = "A"
        if first_octet >= 128 and first_octet <= 191:
            class_of_octet = "B"
        if first_octet >= 192 and first_octet <= 223:
            class_of_octet = "C"

        return render_template("index.html", Net_Addr=str(Net_Addr).split('/')[0], pref_len=pref_len.split('/')[1], Mask=Mask.split('/')[1], wildcard=wildcard, broadcast_address=broadcast_address, variable=True, first_ip=list(Net_Addr.hosts())[0], last_ip=list(Net_Addr.hosts())[-1], classes=class_of_octet)


        # print('Network Address : ', str(Net_Addr).split('/')[0])
        # print('Broadcast Address : ' , broadcast_address)
        # print('CIDR Notation : ', pref_len.split('/')[1])
        # print('Subnet Mask : ', Mask.split('/')[1])
        # print('Wildcard Mask : ' , wildcard)
        # print('First IP : ' , list(Net_Addr.hosts())[0])
        # print('Last IP : ' , list(Net_Addr.hosts())[-1])
