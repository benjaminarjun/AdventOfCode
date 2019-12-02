use std::fs::File;
use std::io::{BufRead, BufReader};


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


fn get_required_fuel_amt_from_mass(mass: u32, recurse: bool) -> u32 {
    if mass < 6 {
        0
    }
    else {
        let fuel_for_current_mass: u32 = mass / 3 - 2;

        if recurse {
            fuel_for_current_mass + get_required_fuel_amt_from_mass(fuel_for_current_mass, true)
        }
        else {
            fuel_for_current_mass
        }
    }
}


fn get_total_fuel_requirement(masses: &Vec<u32>, include_fuel: bool) -> u32 {
    masses.into_iter().map(|x| get_required_fuel_amt_from_mass(*x, include_fuel)).sum()
}


#[cfg(test)]
mod tests {
    use super::*;

    // Not accounting for extra weight of fuel
    #[test]
    fn test_required_fuel_amt_from_mass_12() {
        assert_eq!(get_required_fuel_amt_from_mass(12, false), 2);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_14() {
        assert_eq!(get_required_fuel_amt_from_mass(14, false), 2);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_1969() {
        assert_eq!(get_required_fuel_amt_from_mass(1969, false), 654);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_100756() {
        assert_eq!(get_required_fuel_amt_from_mass(100756, false), 33583);
    }

    // Make sure we handle a small value properly
    #[test]
    fn test_negligible_mass_requires_0_fuel() {
        assert_eq!(get_required_fuel_amt_from_mass(1, false), 0);
    }

    // Accounting for extra weight of fuel
    #[test]
    fn test_required_fuel_amt_from_mass_with_recurse_14() {
        assert_eq!(get_required_fuel_amt_from_mass(14, true), 2);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_with_recurse_1969() {
        assert_eq!(get_required_fuel_amt_from_mass(1969, true), 966);
    }

    #[test]
    fn test_required_fuel_amt_from_mass_with_recurse_100756() {
        assert_eq!(get_required_fuel_amt_from_mass(100756, true), 50346);
    }
}
