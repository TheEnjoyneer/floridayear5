/* readme.txt */
/* Christopher Brant */
/* Lab 2 Linear Code Readme Instructions */

My python code should be fully self contained.

Execute my full python script with its checks for pingall and qperf

$ sudo python3 Linear-Code-Teammate2.py

This should output all of the results for pingall, as well as the 
qperf latency experiments for tcp/udp for each host connecting
to h1 host.

Note: h1.stop() on line 108 of my Linear-Code-Teammate2.py file 
is there as it solves an issue that python encounters because I
run the 'qperf' command as h1.sendCmd() as async. Just disregard it
if you are worried lol.
