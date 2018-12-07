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
begin
  and_gate <= input_1 and input_2;
  and_result <= and_gate;
end rtl;

signal s1, s2, s3 : std_logic_vector(3 downto 0);
...
s1(0) <= '0';
s1(1) <= '1';
s1(2) <= '1';
s1(3) <= '0';
s2 <= "1100";     -- sets s(3),s(2) to '1', s(1),s(0) to '0': same order as range in declaration
s3 <= s2          -- copies all of s2 into s3
s3 <= s1 and s2;  -- "0100"
