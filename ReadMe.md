RV32I Processor Simulation

This project simulates single-stage and five-stage pipeline processors for the RV32I instruction set. It supports essential RISC-V instructions and provides performance metrics.

How to Run the Code

	1.	Prepare Input Files
	•	Place imem.txt (binary instructions) and dmem.txt (data memory) in the code directory.

	2.	Run the Simulation

python code/main.py --iodir <path-to-input-directory>

Replace <path-to-input-directory> with the folder containing imem.txt and dmem.txt.

	3.	Outputs
Results will be saved in the submissions directory:
	•	Register File States: SS_RFResult.txt, FS_RFResult.txt
	•	Memory Dumps: SS_DMEMResult.txt, FS_DMEMResult.txt
	•	State Tracking: StateResult_SS.txt, StateResult_FS.txt
	•	Performance Metrics: PerformanceMetrics.txt

