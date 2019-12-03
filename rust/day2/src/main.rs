mod lib;
mod tests;

use std::fs;
use lib::{find_noun_and_verb_resulting_in , IntCodeComputer};


fn main() {
    let program: Vec<u32> = fs::read_to_string("../../data/day2_input.txt")
        .unwrap().split(',').map(|x| x.parse::<u32>().unwrap()).collect();

    // Part 1
    let mut part_1_computer: IntCodeComputer = IntCodeComputer::new(&program);
    part_1_computer.change_noun(12);
    part_1_computer.change_verb(2);

    // Part 2
    let (noun, verb) = find_noun_and_verb_resulting_in(19690720, &program).unwrap();

    println!("Part 1:  {}", part_1_computer.get_result());
    println!("Part 2:  {}", 100 * noun + verb);
}
