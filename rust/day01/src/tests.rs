#[cfg(test)]
mod tests {
    use crate::lib::get_required_fuel_amt_from_mass;

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
