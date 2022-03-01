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

        array_first_ip = str(Net_Addr).split('.')
        array_last_ip = str(broadcast_address).split('.')

        last_octet = int((str(Net_Addr).split('.')[3]).split('/')[0])
        last_octet_1 = int((str(broadcast_address).split('.')[3]).split('/')[0])


        octet_of_hostable = int((str(Net_Addr).split('.')[3]).split('/')[1])
        total_host = (2 ** (32 - octet_of_hostable)) - 2

        last_ip = f'{array_last_ip[0]}.{array_last_ip[1]}.{array_last_ip[2]}.{last_octet_1 - 1}'
        first_ip = f'{array_first_ip[0]}.{array_first_ip[1]}.{array_first_ip[2]}.{last_octet + 1}'
        return render_template("index.html", total_host=total_host, Net_Addr=str(Net_Addr).split('/')[0], pref_len=pref_len.split('/')[1], Mask=Mask.split('/')[1], wildcard=wildcard, broadcast_address=broadcast_address, variable=True, first_ip=first_ip, last_ip=last_ip, classes=class_of_octet)

        return first_ip
    
        return str(Net_Addr)


        last_octet = int((str(Net_Addr).split('.')[3]).split('/')[0])
        last_octet_1 = int((str(broadcast_address).split('.')[3]).split('/')[0])
        first_ip = last_octet + 1
        last_ip = last_octet_1 - 1


