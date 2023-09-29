import socket

def port_scanner(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            connection = sock.connect((host, port))
            open_ports.append(port)
            connection.close()
        except:
            pass

    return open_ports

host = input('Enter the host: ')
start_port = int(input('Enter the start port: '))
end_port = int(input('Enter the end port: '))

open_ports = port_scanner(host, start_port, end_port)

if open_ports:
    print('Open ports:')
    for port in open_ports:
        print(port)
else:
    print('No open ports found.')
