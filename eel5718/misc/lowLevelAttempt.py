#!/usr/bin/python

from mininet.node import Host, OVSSwitch, Controller
from mininet.link import Link

h1 = Host('h1')
h2 = Host('h2')
h3 = Host('h3')
h4 = Host('h4')
h5 = Host('h5')
h6 = Host('h6')
h7 = Host('h7')
h8 = Host('h8')

s1 = OVSSwitch('s1', inNamespace=False)
s2 = OVSSwitch('s2', inNamespace=False)
s3 = OVSSwitch('s3', inNamespace=False)
s4 = OVSSwitch('s4', inNamespace=False)

c0 = Controller('c0', inNamespace=False)                                                                      

# Create the links here
Link(h1, s1)
Link(h2, s1)
Link(h3, s1)
Link(h4, s1)
Link(s1, s2)
Link(s2, s3)
Link(s3, s4)
Link(h5, s4)
Link(h6, s4)
Link(h7, s4)
Link(h8, s4)

h1.setIP('10.0.0.1/24')  
h2.setIP('10.0.0.2/24')  
h3.setIP('10.0.0.3/24')  
h4.setIP('10.0.0.4/24')  
h5.setIP('10.0.0.5/24')  
h6.setIP('10.0.0.6/24')  
h7.setIP('10.0.0.7/24')  
h8.setIP('10.0.0.8/24')  

# Start the controller
c0.start()

# Start the switches
s1.start([c0])
s2.start([c0])
s3.start([c0])
s4.start([c0])

# Print all the IP addresses for the individual nodes
print(h1.IP)
print(h2.IP)
print(h3.IP)
print(h4.IP)
print(h5.IP)
print(h6.IP)
print(h7.IP)
print(h8.IP)

# Do the pingall command for the network
print('Pinging All...')
print(h1.cmd('ping -c3 ', h2.IP()))     
print(h1.cmd('ping -c3 ', h3.IP()))


# Stop everything once done
s1.stop()                               
s2.stop()       
s3.stop()
s4.stop()
c0.stop() 
