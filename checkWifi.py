import subprocess
ps = subprocess.Popen(['iwconfig'], stdout = subprocess.PIPE,stderr = subprocess.STDOUT)
try:
    output = subprocess.check_output(('grep','ESSID'), stdin=ps.stdout)
    print( 1,"Wifi Connected to: " + str(output)) # this only print if connected
except subprocess.CalledProcessError:
    print(0,'No Wireless Connection') # should run QR script here
