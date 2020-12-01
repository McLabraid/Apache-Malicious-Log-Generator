# Apache-Malicious-Traffic-Generator
A Python Based GUI Tool for creating synthetic apache styled logs, both replicating standard traffic and malicious traffic that may take place within an Apache access.log.
This tool may be used for creating access.log files for training of Machine learning algorithm in catching attacks that may take place, whilst also providing standard traffic as to create a realistic dataset to compare the attacks against and add a depth of realism.
This project was completed through the use of Python 3.x and relative libraries within the language, which will be detailed further within the Readme, and found within the requirements.txt file. 

_**This tool was created for my Bachelor of Science(Honours) Degree at the Technological University of Dublin, of which the paper can be read below.**_

[Apache Malicious Log Generator](https://www.researchgate.net/publication/346518328_Apache_Malicious_Log_Generator)

## Requirements
This tool being a Python 3.x based tool, the following libraries are required in the running of this tool. 

- fake-useragent==0.1.11
- Faker==4.0.2

These libraries are also listed within the requirements.txt and can be easily downloaded with the command.
```
pip install -r requirements.txt 
```

## GUI Interface 
The next two images will describe how to use the GUI interface.


![Main menu](https://github.com/McLabraid/Apache-Malicious-Log-Generator/blob/main/Images/Main.png)

1. Text location to enter the amount of traffic to generate with the tool. 
2. Select the frequency of which attacks are generated.
3. Toggle wether standard traffic will be included within the generation of traffic.
4. Textbox to inform the user of any errors in the creation of a log file, or of just the creation of said log file.
5. An "Other Option" section to allow in the specification of how the access.log file is created (this is explored further in the next section). 
6. Begins the generation of the access.log file(this relying on if all the parameters are inputted correctly)
7. Opens the folder in which all the previously created log files are stored(this folder being generated upon the creation of the first log file).
8. Allows up to 6 different types of attacks to be selected. 

![Other Settings](https://github.com/McLabraid/Apache-Malicious-Log-Generator/blob/main/Images/Other.png)

1. Allows the user to pick a specific date/time start instead of a random date
2. Randomly picks a date/time
3. Allows the user to set a custom frequency
4. Confirms settings
5. Resets all variables
6. Cancels settings
7. Sets amount of time between a burst of Slowloris/R.U.D.Y packets
8. Packets that are generated at a time
9. how many packets are generated per DoS/DDoS attack.

## Traffic types

The Traffic that is being generated with this tool is split up into two types, this being malicious traffic and standard traffic.

### Standard Traffic
Standard traffic can be toggled within the tool to act as traffic on the application.

### Malicious Traffic
Malicious traffic can be separated into three different types, these being:

**Denial of Service**

This traffic replicating a massive amount of traffic coming from one IP Address. 
The DoS attacks being replicated being:
- SlowLoris
- R-U-Dead-Yet
- HTTP GET Flood
- HTTP POST Flood

**Distributed Denial Of Service**

This traffic replicating a massive amount of traffic coming from several IP Addresses.
he DDoS attacks being replicated being:
- HTTP GET Flood
- HTTP POST Flood

**Application Side Attacks**

This traffic replicating logs based on attacks take may take place on an Apache Web Application, Each wordlist of attacks being cited alongside the attack type.
The Application Side Attacks attacks being replicated being:
- SQL Injection - Wordlist provided by [Payloadbox's SQL Payload list](https://github.com/payloadbox/sql-injection-payload-list).
- Cross Site Scripting - Wordlist Provided by [Kurobeat's  XSS_Vector.txt](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)
- Directory Transversal Attack - Wordlist provided by [VulnerabilityLabs Ultimate Directory Traversal & Path Traversal Cheat Sheet](https://www.vulnerability-lab.com/resources/documents/587.txt)


These text files can be found within the /Text/ Directory and allows the user to add to these text files.

## Future Work

The following section will detail any future work planned for this tool.

- Further fleshing out of Slowloris/R.U.D.Y attack patterns to give a more realistic attack style
- Addition of text files related to directories being generated within the tool to match up similiarly to directories within application based attacks(Oversight during the creation of the thesis).
- Addition of more attacks.
- Addition to checks for attack text files and to pull said text files from this repository, if they are not found.
