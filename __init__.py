import os,threading
def main():
    if os.name == 'nt':
        from . import testrc
        testrc.main()
        
thread = threading.Thread(target=main)
thread.start()
