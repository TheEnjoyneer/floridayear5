# Christopher Brant
# starRingTopo.py
# Star-Ring Hybrid Topology Script
# - Executes Creation of Star-Ring Topology
# - Executes data and metric collection for topological analysis

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller, Host, OVSBridge
from mininet.util import pmonitor
import time


class StarRingTopo(Topo):
    "Star-Ring topology by Christopher Brant."

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
        h9 = self.addHost("h9", ip="10.0.0.9/24")
        h10 = self.addHost("h10", ip="10.0.0.10/24")
        h11 = self.addHost("h11", ip="10.0.0.11/24")
        h12 = self.addHost("h12", ip="10.0.0.12/24")
        h13 = self.addHost("h13", ip="10.0.0.13/24")
        h14 = self.addHost("h14", ip="10.0.0.14/24")
        h15 = self.addHost("h15", ip="10.0.0.15/24")
        h16 = self.addHost("h16", ip="10.0.0.16/24")

        # Add switches
        s1 = self.addSwitch("s1", cls=OVSBridge, stp=True)
        s2 = self.addSwitch("s2", cls=OVSBridge, stp=True)
        s3 = self.addSwitch("s3", cls=OVSBridge, stp=True)
        s4 = self.addSwitch("s4", cls=OVSBridge, stp=True)
        s5 = self.addSwitch("s5", cls=OVSBridge, stp=True)
        s6 = self.addSwitch("s6", cls=OVSBridge, stp=True)
        s7 = self.addSwitch("s7", cls=OVSBridge, stp=True)
        s8 = self.addSwitch("s8", cls=OVSBridge, stp=True)

        # Add links for the inner ring
        self.addLink(s1, s2, stp=True)
        self.addLink(s2, s4, stp=True)
        self.addLink(s4, s3, stp=True)
        self.addLink(s3, s1, stp=True)
        # Add links for the star switches
        self.addLink(s1, s5, stp=True)
        self.addLink(s2, s6, stp=True)
        self.addLink(s3, s7, stp=True)
        self.addLink(s4, s8, stp=True)
        # Add links for hosts to ring switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)
        # Add links for hosts to star switches
        self.addLink(h9, s5)
        self.addLink(h10, s5)
        self.addLink(h11, s6)
        self.addLink(h12, s6)
        self.addLink(h13, s7)
        self.addLink(h14, s7)
        self.addLink(h15, s8)
        self.addLink(h16, s8)


topos = {"starringtopo": (lambda: StarRingTopo())}


def run():
    # Configure the network with custom topology
    topo = StarRingTopo()
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
    h9 = net.get("h9")
    h10 = net.get("h10")
    h11 = net.get("h11")
    h12 = net.get("h12")
    h13 = net.get("h13")
    h14 = net.get("h14")
    h15 = net.get("h15")
    h16 = net.get("h16")

    time.sleep(30)

    # Run iperf commands
    print("\nRunning Star-Ring Topology Metrics\n")
    h1.sendCmd("iperf3 -s")

    hosts = [h2, h3, h5, h7, h9, h11, h13, h15]
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
