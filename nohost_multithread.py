import subprocess
import threading

def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return ip, True
    else:
        return ip, False

def worker(ip_range):
    for ip in ip_range:
        response = ping_ip(ip)
        if not response[1]:
            print(f"{response[0]} is unused.")

if __name__ == '__main__':
    ip_range = ['192.168.1.' + str(i) for i in range(2, 255)]
    num_threads = len(ip_range)
    
    threads = []
    chunk_size = len(ip_range) // num_threads
    
    for i in range(0, len(ip_range), chunk_size):
        thread = threading.Thread(target=worker, args=(ip_range[i:i+chunk_size],))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
