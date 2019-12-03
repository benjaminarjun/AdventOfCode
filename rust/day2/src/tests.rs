#[cfg(test)]
mod tests {
    use crate::lib::IntCodeComputer;

    #[test]
    fn test_int_code_computer_1() {
        let input = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];

        let mut computer = IntCodeComputer::new(&input);
        assert_eq!(computer.get_result(), 3500);
    }

    #[test]
    fn test_int_code_computer_2() {
        let input = vec![1, 0, 0, 0, 99];

        let mut computer = IntCodeComputer::new(&input);
        assert_eq!(computer.get_result(), 2);
    }

    #[test]
    fn test_int_code_computer_3() {
        let input = vec![2, 3, 0, 3, 99];

        let mut computer = IntCodeComputer::new(&input);
        assert_eq!(computer.get_result(), 2);
    }

    #[test]
    fn test_int_code_computer_4() {
        let input = vec![2, 4, 4, 5, 99, 0];

        let mut computer = IntCodeComputer::new(&input);
        assert_eq!(computer.get_result(), 2);
    }

    #[test]
    fn test_int_code_computer_5() {
        let input = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];

        let mut computer = IntCodeComputer::new(&input);
        assert_eq!(computer.get_result(), 30);
    }
}
