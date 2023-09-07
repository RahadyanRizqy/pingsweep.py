import subprocess
from concurrent.futures import ProcessPoolExecutor

def ping_ip(ip):
    result = subprocess.run(['ping', ip, '-n', '1', '-w', '1000'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return ip, True
    else:
        return ip, False

if __name__ == '__main__':
    ip_range = ['192.168.1.' + str(i) for i in range(2, 255)]
    
    with ProcessPoolExecutor(max_workers=61) as pool:
        results = pool.map(ping_ip, ip_range)
    
    for ip, response in results:
        if not response:
            print(f"{ip} is unused.")