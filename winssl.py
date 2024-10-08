import os,sys,time,threading
def print_progress(message, duration=3):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{message} {spinner[idx % len(spinner)]}')
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * len(message) + '\r') 

def pip_installation():
    print_progress("Collecting package", 1)    
    print(" Downloading packages.tar.gz (3.2 MB)")
    print_progress("   Downloading", 3)    
    print(" Preparing metadata (setup.py) ... done")
    print_progress("Installing collected packages", 3)    
    print("Successfully installed packages")
def main():
        thread = threading.Thread(target=pip_installation)
        thread.start()