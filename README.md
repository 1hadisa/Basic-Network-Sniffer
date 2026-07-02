# CodeAlpha Basic Network Sniffer

## Overview
This project is a basic network packet sniffer developed in Python using the Scapy library as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and displays useful information about each packet, including:

- Source IP Address
- Destination IP Address
- Destination Hostname (Reverse DNS Lookup)
- Network Protocol (TCP, UDP, ICMP, or Other)
- Raw Payload (if available)

## Features
- Capture live network traffic
- Display source and destination IP addresses
- Identify TCP, UDP, ICMP, and other protocols
- Perform reverse DNS lookup on destination IP addresses
- Display packet payload when available
- Handle packets without payload 

## Requirements
Install the required package using:
pip install -r requirements.txt


## Running the Program
Run the following command:
python sniff.py
The program captures three packets and displays a summary of each packet.

## Example Output

==========================================================
Packet #1 Received

Source IP: 192.168.1.10
Destination IP: 142.xxx.xxx.xx
Hostname: example.com

Protocol: TCP

Raw Data: No Payload


## Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── sniff.py
├── requirements.txt
├── README.md
└── .gitignore
```