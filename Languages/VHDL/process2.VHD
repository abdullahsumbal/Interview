-- https://www.nandland.com/vhdl/tutorials/tutorial-introduction-to-vhdl-for-beginners.html
-- VHDL: Very High Speed Integrated Circuit Hardware Description Language

library ieee;
use ieee.std_logic_1164.all;


-- input and outputs are defined in entity
entity example_and is
  port (
    input_1 : in std_logic;
    input_2 : in std_logic;
    i_clock : in std_logic;
    and_result : out std_logic
  );
  and example_and;

  -- architecure is used to describe the functionality of the entity

architecure rtl of example_and is
  signal test1 : std_logic := '1';
  signal test2 : std_logic := '0';
  signal test3 : std_logic := '0';
  signal test4 : std_logic := '0';
-- input_1 and input_2 are in what is called a sensitivity list.
process (i_clock)
begin
--  using edge to trigger.
  if rising_edge(i_clock) then
    test2 <= test1;
    test3 <= test2;
    test4 <= test3;
  end if;
end process;
and_result <= test4;
end rtl;
