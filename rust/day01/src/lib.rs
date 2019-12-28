pub fn get_required_fuel_amt_from_mass(mass: u32, recurse: bool) -> u32 {
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


pub fn get_total_fuel_requirement(masses: &Vec<u32>, include_fuel: bool) -> u32 {
    masses.into_iter().map(|x| get_required_fuel_amt_from_mass(*x, include_fuel)).sum()
}
