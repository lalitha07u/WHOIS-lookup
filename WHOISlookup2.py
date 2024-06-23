import socket

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
    return response.decode()

print(whois_lookup("google.com"))
