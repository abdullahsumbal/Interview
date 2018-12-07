-- https://www.nandland.com/vhdl/tutorials/tutorial-introduction-to-vhdl-for-beginners.html
-- VHDL: Very High Speed Integrated Circuit Hardware Description Language

library ieee;
use ieee.std_logic_1164.all;


-- input and outputs are defined in entity
entity example_and is
  port (
    input_1 : in std_logic;
    input_2 : in std_logic;
    and_result : out std_logic
  );
  and example_and;

  -- architecure is used to describe the functionality of the entity

architecure rtl of example_and is
  signal and_gate : std_logic;
-- input_1 and input_2 are in what is called a sensitivity list.
process (input_1, input_2)
begin
  and_gate <= input_1 and input_2;
end process;
and_result <= and_gate;
end rtl;
