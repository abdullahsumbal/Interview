### The Intel Programmable Solutions Group (PSG) offers FPGAs, SoC FPGAs, CPLDs and complementary power solutions to accelerate a smart and connected world.

### FPGA:  
 A field programmable gate array (FPGA) is a semiconductor device containing programmable logic components and programmable interconnects. It can be programmed or reprogrammed to the required functionality after manufacturing

FPGA is opposite of ASIC.

## FPGA are made up of

CLB (configurable logic blocks)   
Reconfigurable interconnects   
I/O block  
Fixed function logic block (multiplier)  
Block RAM  


### SoC:  
System on chip. They used in smartphones. They contains almost thing in one chip like
CPU,  
GPU  
DSP: digital processing unit used for video and audio  
Memory  
Connectivity module: WIFI, bluetooth  

### CPLD:  
 Complex Programmable logic Device. They are same as FPGA but has EEPROM Flash instead of logic blocks


### How FPGA are different from microcontroller?

In a microcontroller, we upload a piece and to do a certain task. On the other hand in FPGA we define the hardware to do a certain task. Can perform task in parallel.

### FGPA over GPU
The great thing about FPGA is that it can run DNN at low power.  
Advantages:  
Low Latency: this is why FPGA is used in jet planes   
Connect data source to any pin and high bandwidth.  
Disadvantages:  
	FPGA are much harder to program in hardware  
	But they can use HLS and openCL  compiler which makes it easier  
Energy efficiency: This is true for fixed point but not for floating points.  

### The two things holding back FPGA is the compile time and floating point computation.


### What is opencl?
This is specification to facilitate parallel computing

### What is HLS?
The Intel® HLS Compiler is a high-level synthesis (HLS) tool that takes in untimed C++ as input and generates production-quality register transfer level (RTL) code that is optimized for Intel FPGAs


### How FPGA relate to cloud?
they are programmable, you can do machine learning on them.

### Why FPGA becoming more popular now?
it hard to make dedicated chip. with FPGA you can make the solution on the fly. Now, they are performant.
They are trying to make it easier for developer by introducing HLS.


### FPGA in amazon?
technology in alexa for speech processing.

### What is OpenVino?
there is a component called Intel deep learning deployment toolkit (DLDT). DLDT has two parts Model optimizer
and interface engine. Model optimizer converts and optimizes model from different frameworks such as caffe and tensorflow. They are
converted into intermediate representation. Inference Engine runs the optimized model using C++ api. DLDT can used for different
platforms such CPU, FPGA and GPU.

### What FPGA Deep Learning Acceleration suits (DLAS)?
In order for DLDT to seamless work on FPGA, intel offer DLA suit. it allows user to take Advantages of the FPGA without going through
lengthy traditional FPGA development process. DLA contains various implementations of deep learning primitives that are tailored for
different types of deep learning topologies. This allows user to implement various networks like google net and LX net with out
recompiling the FPGA. DLA suits also has many primitives such as convolution fully connected, rectified linear unit, Relu and pooling

### What is the Acceleration slack platform solution?
![](images/stack.JPG)

### What I want to work at?
Inference engine. DLA plugin
