# YOUR NAME HERE
# FILE NAME HERE
# TOPO_TYPE Topology Script
# - Executes Creation of TOPO_TYPE Topology
# - Executes data and metric collection for topological analysis

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller, Host, OVSBridge
from mininet.util import pmonitor
import time

# RENAME YOUR TOPOLOGY HERE AND GIVE IT YOUR NAME


class ring_topo(Topo):
    "ring topology example."

    def __init__(self):
        "Create custom topo."
        # Initialize topology
        super().__init__()

		
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        

        s1 = self.addSwitch('s1', cls=OVSBridge, stp=True)
        s2 = self.addSwitch('s2', cls=OVSBridge, stp=True)
        s3 = self.addSwitch('s3', cls=OVSBridge, stp=True)
        s4 = self.addSwitch('s4', cls=OVSBridge, stp=True)


        # Add links
        
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s1, s2,stp=True)
        
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s2, s3,stp=True)
        
        self.addLink(s3, h5)
        self.addLink(s3, h6)
        self.addLink(s3, s4,stp=True)        
        
        self.addLink(s4, h7)
        self.addLink(s4, h8)
        self.addLink(s4, s1,stp=True)
        
topos = {'ringtopo': (lambda: ring_topo())}


def run():
    # Configure the network with custom topology
    # CHANGE THE TOPOLOGY NAME HERE
    topo = ring_topo()
    c0 = Controller("c0")
    net = Mininet(topo=topo, controller=c0, switch=OVSSwitch)

    # Start the network
    net.start()

    # ADD ALL HOST NODES IN YOUR NETWORK HERE
    # Get necessary nodes for running commands
    h1 = net.get("h1")
    h2 = net.get("h2")
    h3 = net.get("h3")
    h4 = net.get("h4")
    h5 = net.get("h5")
    h6 = net.get("h6")
    h7 = net.get("h7")
    h8 = net.get("h8")

    time.sleep(30)

    # Run iperf commands
    # print("\nRunning 'iperf' server on h1\n")
    h1.sendCmd("iperf3 -s")

    # ADD ALL HOST NODES IN YOUR NETWORK TO THIS LIST
    hosts = [h1, h3, h5, h7,]
    for i in range(len(hosts)):
        pingResp = hosts[i].cmd('ping -c1 10.0.0.1')
        iperfResp = hosts[i].cmd('iperf3 -c 10.0.0.1 -u')
        print("\nGetting Stats between h1 and h" + str(i+2) + "\n")
        print(pingResp)
        print(iperfResp)
        # write to file

    h1.stop()
    # Break down the network
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    run()
