# This Dataset is generated by processing the Pcap files of CTU-13 Dataset using CICFlowMeter Tool.

In order to create this CSV dataset:

We imported all Pcap files of CTU-13 Dataset using CICFlowMeter Tool.
The CICFlowMeter Tool converts the given Pcap Files into CSV Files based on Packet Flows.
We then merged all attack traffic samples into CTU13_Attack_Traffic.csv based on Attack IPs.
Similarly, we merged all normal traffic samples into CTU13_Normal_Traffic.csv by considering all IPS other than Attack IPs.
In short, You see 2 CSV Files in this repo:

CTU13_Attack_Traffic.csv contains Botnet attack traffic samples.
CTU13_Normal_Traffic.csv contains Normal traffic samples.
The Original Dataset can be found at: CTU-13 Dataset

The CTU-13 Dataset is a Labeled Dataset with Botnet, Normal and Background traffic

The CTU-13 is a dataset of botnet traffic that was captured in the CTU University, Czech Republic, in 2011.
The goal of the dataset was to have a large capture of real botnet traffic mixed with normal traffic and background traffic.
The CTU-13 dataset consists in thirteen captures (called scenarios) of different botnet samples. On each scenario we executed a specific malware, which used several protocols and performed different actions.
