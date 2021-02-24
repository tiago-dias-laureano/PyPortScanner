import socket  

def get_version(ip_address, port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, port)) 
        s.settimeout(2)
        byte = str.encode("Server:\r\n")
        s.send(byte)

        banner = s.recv(1024)
        if str(banner):
            if port == 21:
                if 'Pure-FTPd' in str(banner):
                    return 'Pure-FTPd'
                elif 'FTP Server' in str(banner):
                    return 'FTP Server'
            
            if port == 22:
                if 'OpenSSH' in str(banner):
                    return 'OpenSSH'

            if port == 25:
                if 'ESMTP Exim' in str(banner):
                    return 'ESMTP Exim'
            
            if port == 26:
                if 'ESMTP Exim' in str(banner):
                    return 'ESMTP Exim'
            
            if port == 80:
                if 'Apache' in str(banner):
                    return 'Apache'
                elif 'nginx' in str(banner):
                    return 'Nginx'
                elif 'Microsoft-HTTPAPI'in str(banner):
                    return 'Microsoft-HTTPAPI'
                elif 'aruba-proxy' in str(banner):
                    return 'aruba-proxy'
                elif 'openresty' in str(banner):
                    return 'openresty'
                elif 'cloudflare' in str(banner):
                    return 'Cloudflare'

            if port == 110:
                if 'Dovecot' in str(banner):
                    return 'Dovecot pop3d'

            if port == 143:
                if 'IMAP' in str(banner):
                    return 'Dovecot imapd'
            
            if port == 443:
                if 'nginx' in str(banner):
                    return 'Nginx'
                elif 'aruba-proxy' in str(banner):
                    return 'aruba-proxy'
                elif 'openresty' in str(banner):
                    return 'openresty'
                elif 'cloudflare' in str(banner):
                    return 'Cloudflare'

            if port == 3306:
                return 'MySql'

            if port == 8080:
                if 'nginx' in str(banner):
                    return 'Nginx'
                elif 'aruba-proxy' in str(banner):
                    return 'aruba-proxy'
                elif 'openresty' in str(banner):
                    return 'openresty'
                elif 'cloudflare' in str(banner):
                    return 'Cloudflare'

        else: 
            return " "
    except:
        return " "