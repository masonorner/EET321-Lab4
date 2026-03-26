# EET321-Lab4

EET321		            Measurement and Tests Lab				
Lab 4 PLC Inputs and Outputs 
169.254.13.11
CPU: C2-01CPU
I/O: C2-08AR-4VC
Objectives:
1.	Assess the error of PLC analog inputs and outputs.
2.	Assess Vih and Vil on PLC discrete IO.

Task 1: Verify operation of a PLC’s analog voltage input.  Acquire the PLC reading via a 	PYTHON program.
1.	Configure the PLC’s analog inputs for voltage.
2.	Apply known voltages within the PLC’s range to the input and verify an appropriate reading in the PLC.
3.	Receive the voltage reading in a PYTHON program.

Task 2: Verify operation of a PLC’s analog current input.  Acquire the PLC reading via a 	PYTHON program.  
1.	Configure the PLC’s analog inputs for current.
2.	Design and build a system capable of providing the full range of current to the PLC.  To do this effectively, consider the internal resistance of the power supply/function generator, the internal resistance of the PLC analog input, and an intermediate resistor across which a voltage (and current indirectly) can be measured.
3.	Apply known currents within the PLC’s range to the input and verify an appropriate reading in the PLC.
4.	Receive the current reading in a PYTHON program.

Task 3: Verify operation of a PLC’s analog voltage output.  Control the PLC output via a		 PYTHON program.
1.	Configure the PLC’s analog outputs for voltage.
2.	Write an appropriate value to the analog voltage output register and verify a reasonable voltage is output.
3.	Write a PYTHON program to control this PLC register.

Task 4: Verify operation of a PLC’s analog current output.  Control the PLC output via a		 PYTHON program.
1.	Configure the PLC’s analog outputs for current.
2.	Write an appropriate value to the analog current output register and verify a reasonable current is output.  Consider using the resistor recommended in the manual as a load and measuring the voltage across it.
3.	Write a PYTHON program to control this PLC register.

Task 5: Develop a process for stepping through voltages on a power supply/function 	generator.  Test the PLC’s discrete input for its “transition” region.
1.	Write a PYTHON program capable of systematically stepping a power supply through a range of voltages.  The range and step size should be configurable.  Furthermore, the program should allow for going up and down.
2.	Program a PLC such that its discrete inputs directly fire its discrete outputs.
3.	Step through voltages from 0 through 24 volts observing the status of the discrete outputs (which in turn indicate the status of the inputs).  The goal is to narrow in on the range where the discrete IO switches state.


Experiment 1: Automate sequencing through the full range of analog voltage inputs		 acquiring the PLC reading for each step.
1.	Write PYTHON code to systematically step through the range of voltages accepted by the PLC analog voltage input.  The smaller the steps, the more precise your results will be.  
2.	For each voltage, acquire the corresponding reading from the PLC.
3.	Write the results to a database.


Experiment 2: Automate sequencing through the full range of analog current inputs		 acquiring the PLC reading for each step.
1.	Write PYTHON code to systematically step through the range of currents accepted by the PLC analog current input.  The smaller the steps, the more precise your results will be.  
2.	For each current, acquire the corresponding reading from the PLC.
3.	Write the results to a database.

 
Experiment 3: Automate sequencing through the full range of analog voltage outputs		 acquiring a voltage reading for each step.
1.	Write PYTHON code to systematically step through the range of voltage values for the PLC analog voltage output.  
2.	For each voltage setting, acquire the corresponding voltage output from the PLC.
3.	Write the results to a database.

Experiment 4: Automate sequencing through the full range of analog current outputs		 acquiring a current reading for each step.
1.	Write PYTHON code to systematically step through the range of current values for the PLC analog current output.  
2.	For each current setting, acquire the corresponding current output from the PLC.
3.	Write the results to a database.

Experiment 5: Automate sequencing through the full range of voltages input to discrete PLC inputs acquiring their status via associate discrete outputs.
1.	Write PYTHON code to systematically step through a range of voltage values for the PLC discrete voltage input.  Take larger steps for known regions and smaller steps within the transition region.
2.	For each voltage setting, acquire the corresponding voltage output from the PLC.
3.	Write the results to a database.

Optional Extension: Repeat Experiment 1 and 2 with C# program instead of Python
 
Data Analysis and Reporting: 
1.	For the discrete data, plot output voltage vs input voltage for all the applied voltages.  On the same graph, plot the maximum off voltage and minimum on voltage from the PLC data sheet.  Are there any points not within the listed tolerance?  What is the actual voltage hysteresis range of the inputs.
2.	For the analog inputs, plot actual voltage vs step by expected voltage vs step.  Are the results linear?  Discuss why or why not.  Also compare current to voltage; is one setup better than the other?
3.	For the analog outputs, plot actual voltage vs step by expected voltage vs step.  Are the results linear?  Discuss why or why not.  Also compare current to voltage; is one setup better than the other?
