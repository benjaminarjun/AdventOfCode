use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() {
    let mut masses: Vec<u32> = Vec::new();

    let file = File::open("../../data/day1_input.txt").expect("Could not find or read file!");
    let reader = BufReader::new(file);

    for line in reader.lines() {
        masses.push(line.unwrap().parse::<u32>().unwrap());
    }

    println!("Part 1:  {}", get_total_fuel_requirement(masses));
}


fn get_required_fuel_amt_from_mass(mass: u32) -> u32 {
    if mass < 6 {
        0
    }
    else {
        mass / 3 - 2
    }
}


fn get_total_fuel_requirement(masses: Vec<u32>) -> u32 {
    masses.into_iter().map(|x| get_required_fuel_amt_from_mass(x)).sum()
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_required_fuel_amt_from_mass_12() {
        assert_eq!(get_required_fuel_amt_from_mass(12), 2);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_14() {
        assert_eq!(get_required_fuel_amt_from_mass(14), 2);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_1969() {
        assert_eq!(get_required_fuel_amt_from_mass(1969), 654);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_100756() {
        assert_eq!(get_required_fuel_amt_from_mass(100756), 33583);
    }

    #[test]
    fn test_negligible_mass_requires_0_fuel() {
        assert_eq!(get_required_fuel_amt_from_mass(1), 0);
    }
}
