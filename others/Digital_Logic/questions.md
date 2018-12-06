### 1. what is 1's complement and 2's complement? where it is used?
![](images/complement.JPG)
### 2. Implementation of basic gates using MUX (they frequently ask this!!), also they may ask you to implement any function using MUX.(e.g. design D flip flop using MUX)
https://neovlsi.wordpress.com/2010/01/07/universal-logic-mux-to-logic-gates-conversion/

### 3. what is set up time and hold time in digital circuits? conditions for set up time violations and hold time violations?
Every flipflop or latch needs time to adapt to changes . The time account for setup during input and hold during output .

Setup time : it is the time before sampling edge where data should be stable . This time helps flip-flop to settle to proper data . If this time is not met you write different data than preferred . Not as critical as hold . If the setup time is not met you can tweak the circuit by changing its frequency of operation

Hold time : it is time after sampling edge where data should be stable . This time helps in writing proper data to output . This is a critical parameter to be met . If there is a hold violation on chip there is no way to correct .
4. how can you implement and/or/not gate using NAND/NOR?
### 5. what is the difference between flip flop and latches?
![](images/ff_latch.JPG)
6. conversion of flip flops (e.g. convert T flip flop to D flip flop)
### 7. Design a circuit to  divide a clock  by  2 ? and  by 3 ?
![](images/divide2.JPG)
### 8. What is the difference between mealy and moore?
In the Mealy model, the output is a function of both the present state and the input. In the Moore model, the output is a function of only the present state.
9. what is synchronous and asynchronous counter?
10. design mod x counter (x can be 2, 3, 5 etc.)
### 11. what is the difference between synchronous reset and asynchronous reset?
### 12. Explain the difference  between binary and gray encoding and the benefits of each
gray coding: only one bit can be changed at a time, hence called unique distance code. you use it where you want only one bit to change. In this cycle, there is only one bit switching on or off for each possible transition and this creates much less noise on the binary lines.
13. what is clock gating? how it is implemented? how glitch appears in AND gate based clock gating? how to avoid it?
### 14. What is the difference between Combinational and Sequential circuits?
Ans. Combination depends only on present input value. Combination also does not have a feedback and does not have clock. Sequential depends on present and past values and as well as past value. it has clock and feedback.
### 15. Implementation 2x1 MUX
![](images/mux.JPG)
### 16. truth table for JK flip flop
![](images/jk.JPG)
### 17. What is meant by an race condition?
A race condition is a behavior which occurs in software applications or electronic systems, such as logic systems, where the output is dependent on the timing or sequence of other uncontrollable events. Race conditions also occur in software which supports multithreading, use a distributed environment or are interdependent on shared resources. Race conditions often lead to bugs, as these events happen in a manner that the system or programmer never intended for. It can often result in a device crash, error notification or shutdown of the application.

A race condition is also known as a race hazard.

### design counter
This is moore (does not depend on the input)
![](images/image1.JPG)
![](images/image2.JPG)
![](images/image3.JPG)
![](images/image4.JPG)
![](images/image5.JPG)

### Design a sequential detector (Mealy) (depend on the input)
![](images/seq1.JPG)
![](images/seq2.JPG)
