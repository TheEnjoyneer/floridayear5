# YOUR NAME HERE
# FILE NAME HERE
# TOPO_TYPE Topology Script
# - Executes Creation of TOPO_TYPE Topology
# - Executes data and metric collection for topological analysis

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller, Host
from mininet.util import pmonitor
import time

# RENAME YOUR TOPOLOGY HERE AND GIVE IT YOUR NAME


class tree_topo(Topo):
    "tree topology example."

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
        
        #to create 2 hosts per switch
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        # Add links
        
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, h9)
        self.addLink(s1, h10)
        
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, h11)
        self.addLink(s2, h12)
        
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s3, h13)
        self.addLink(s2, h14)        
        
        self.addLink(s4, h1)
        self.addLink(s4, h2)
        self.addLink(s5, h3)
        self.addLink(s5, h4)
        self.addLink(s6, h5)
        self.addLink(s6, h6)
        self.addLink(s7, h7)
        self.addLink(s7, h8)
        
topos = {'tree_topo': (lambda: tree_topo())}


def run():
    # Configure the network with custom topology
    # CHANGE THE TOPOLOGY NAME HERE
    topo = tree_topo()
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
    h9 = net.get("h9")
    h10 = net.get("h10")
    h11= net.get("h11")
    h12 = net.get("h12")
    h13= net.get("h13")
    h14 = net.get("h14")
    time.sleep(30)

    # Run iperf commands
    # print("\nRunning 'iperf' server on h1\n")
    h1.sendCmd("iperf3 -s")

    # ADD ALL HOST NODES IN YOUR NETWORK TO THIS LIST
    hosts = [h2, h3, h5, h7,h9,h11,h13]
    for i in range(len(hosts)):
        pingResp = hosts[i].cmd('ping -c1 10.0.0.1')
        iperfResp = hosts[i].cmd('iperf3 -c 10.0.0.1 -u')

        print(pingResp)
        print(iperfResp)
        # write to file

    h1.stop()
    # Break down the network
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    run()
