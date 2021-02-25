import socket  

def get_version(arg1, arg2):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((arg1,arg2)) 
        s.settimeout(2)
        byte = str.encode("Server:\r\n")
        s.send(byte)

        banner = s.recv(1024)
        if str(banner):
            if arg2 == 21:
                if 'Pure-FTPd' in str(banner):
                    return 'Pure-FTPd'
                elif 'FTP Server' in str(banner):
                    return 'FTP Server'
            
            if arg2 == 22:
                if 'OpenSSH' in str(banner):
                    return 'OpenSSH'

            if arg2 == 25:
                if 'ESMTP Exim' in str(banner):
                    return 'ESMTP Exim'
            
            if arg2 == 26:
                if 'ESMTP Exim' in str(banner):
                    return 'ESMTP Exim'
            
            if arg2 == 80:
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

            if arg2 == 110:
                if 'Dovecot' in str(banner):
                    return 'Dovecot pop3d'

            if arg2 == 143:
                if 'IMAP' in str(banner):
                    return 'Dovecot imapd'
            
            if arg2 == 443:
                if 'nginx' in str(banner):
                    return 'Nginx'
                elif 'aruba-proxy' in str(banner):
                    return 'aruba-proxy'
                elif 'openresty' in str(banner):
                    return 'openresty'
                elif 'cloudflare' in str(banner):
                    return 'Cloudflare'

            if arg2 == 3306:
                return 'MySql'

            if arg2 == 8080:
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