## SUBNET CALCULATOR ##

**** 
This program lets the user determine the available hosts, first - last and broadcast
address for the IP and subnet mask entered.

**** EXECUTION
This is a Python3 application. Please run 'run.py' to start.

**** FILES
run.py --> Orchestrates the execution of the applcation
Validating_IP_and_SubnetMask.py --> Validates the user inputs before passing these parameters
				    to the next program.
Calculating_Hosts_and_Subnet.py --> Uses the inputs and calculates the said parameters, also
				    asks user to generate random IP from the calculated range.

*** UPDATE COMING SOON
Create a case when subnet mask (first octect) is < 255 (exeptional)
>> network address should not be 0.0.0.0, least it should be 1.0.0.0 for 128.0.0.0 subnet mask
>> also network address should not go beyond 223.255.255.255, 224 is multicast and 240+ is reserved for r&d
  