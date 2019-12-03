mod lib;
mod tests;

use std::fs::File;
use std::fs;
use std::io::{BufRead, BufReader};
use lib::IntCodeComputer;


fn main() {
    let program: Vec<u32> = fs::read_to_string("../../data/day2_input.txt")
        .unwrap().split(',').map(|x| x.parse::<u32>().unwrap()).collect();

    let computer: IntCodeComputer = IntCodeComputer::new(program);
}
