# Christopher Brant
# linearTopo.py
# Linear Topology Script
# - Executes Creation of Linear Topology
# - Executes data and metric collection for topological analysis

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller, Host
from mininet.util import pmonitor


class LinearTopo(Topo):
    "Linear topology by Christopher Brant."

    def __init__(self):
        # Initialize topology
        super().__init__()

        # Add hosts
        h1 = self.addHost("h1", ip="10.0.0.1/24")
        h2 = self.addHost("h2", ip="10.0.0.2/24")
        h3 = self.addHost("h3", ip="10.0.0.3/24")
        h4 = self.addHost("h4", ip="10.0.0.4/24")
        h5 = self.addHost("h5", ip="10.0.0.5/24")
        h6 = self.addHost("h6", ip="10.0.0.6/24")
        h7 = self.addHost("h7", ip="10.0.0.7/24")
        h8 = self.addHost("h8", ip="10.0.0.8/24")

        # Add switches
        s1 = self.addSwitch("s1", cls=OVSSwitch)
        s2 = self.addSwitch("s2", cls=OVSSwitch)
        s3 = self.addSwitch("s3", cls=OVSSwitch)
        s4 = self.addSwitch("s4", cls=OVSSwitch)

        # FOR TEMPLATE HERE IS WHERE YOU'LL CREATE YOUR TOPO
        # BY ADDING THE CORRECT LINKS AND CONNECTIONS BETWEENE ALL THE HOSTS
        # AND SWITCHES AS NECESSARY FOR YOUR TOPO

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s2, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(s3, s4)
        self.addLink(h7, s4)
        self.addLink(h8, s4)


topos = {"lineartopo": (lambda: LinearTopo())}


def run():
    # Configure the network with custom topology
    topo = LinearTopo()
    c0 = Controller("c0")
    net = Mininet(topo=topo, controller=c0, switch=OVSSwitch)

    # Start the network
    net.start()

    # Get necessary nodes for running commands
    h1 = net.get("h1")
    h2 = net.get("h2")
    h3 = net.get("h3")
    h4 = net.get("h4")
    h5 = net.get("h5")
    h6 = net.get("h6")
    h7 = net.get("h7")
    h8 = net.get("h8")

    # Run iperf commands
    print("\nRunning Linear Topology Metrics\n")
    h1.sendCmd("iperf3 -s")

    hosts = [h2, h3, h5, h7]
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
