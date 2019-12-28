mod lib;
mod tests;

use std::fs::File;
use std::io::{BufRead, BufReader};
use lib::get_total_fuel_requirement;


fn main() {
    let mut masses: Vec<u32> = Vec::new();

    let file = File::open("../../data/day1_input.txt").expect("Could not find or read file!");
    let reader = BufReader::new(file);

    for line in reader.lines() {
        masses.push(line.unwrap().parse::<u32>().unwrap());
    }

    println!("Part 1:  {}", get_total_fuel_requirement(&masses, false));
    println!("Part 2:  {}", get_total_fuel_requirement(&masses, true));
}
