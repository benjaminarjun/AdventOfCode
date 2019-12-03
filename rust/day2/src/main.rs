mod lib;
mod tests;

use std::fs::File;
use std::fs;
use std::io::{BufRead, BufReader};
use lib::IntCodeComputer;


fn main() {
    let program: Vec<u32> = fs::read_to_string("../../data/day2_input.txt")
        .unwrap().split(',').map(|x| x.parse::<u32>().unwrap()).collect();

    let mut computer: IntCodeComputer = IntCodeComputer::new(program);
    computer.change_noun(12);
    computer.change_verb(2);

    println!("Part 1:  {}", computer.get_result());
}
