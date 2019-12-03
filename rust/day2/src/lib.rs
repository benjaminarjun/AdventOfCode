use itertools::Itertools;


pub struct IntCodeComputer {
    pub program: Vec<u32>,
    _result: Option<u32>,
    _working_program: Vec<u32>,
    _index: u32,
}

impl IntCodeComputer {
    pub fn new(program: &Vec<u32>) -> Self {
        IntCodeComputer {
            program: program.clone(),
            _result: Option::None,
            _working_program: program.clone(),
            _index: 0,
        }
    }

    fn run(&mut self) {
        loop {
            let int_code_op: IntCodeOp = get_op_by_id(self._working_program[self._index as usize]);

            match int_code_op.op_action {
                // TODO: lots of duplication and ugly code, let's clean it up someday
                // At least add helper method for vector access and type conversion
                OpAction::Add => {
                    let lh_index: usize = self._working_program[(self._index + 1) as usize] as usize;
                    let rh_index: usize = self._working_program[(self._index + 2) as usize] as usize;

                    let lh_value: u32 = self._working_program[lh_index];
                    let rh_value: u32 = self._working_program[rh_index];
                    let new_val: u32 = lh_value + rh_value;

                    let target_index: usize = self._working_program[(self._index + 3) as usize] as usize;
                    self._working_program[target_index] = new_val;
                },
                OpAction::Multiply => {
                    let lh_index: usize = self._working_program[(self._index + 1) as usize] as usize;
                    let rh_index: usize = self._working_program[(self._index + 2) as usize] as usize;

                    let lh_value: u32 = self._working_program[lh_index];
                    let rh_value: u32 = self._working_program[rh_index];
                    let new_val: u32 = lh_value * rh_value;

                    let target_index: usize = self._working_program[(self._index + 3) as usize] as usize;
                    self._working_program[target_index] = new_val;
                },
                OpAction::Terminate => { break; },
            }

            self._index += int_code_op.segment_length;
        }

        self._result = Option::Some(self._working_program[0]);
    }

    pub fn get_result(&mut self) -> u32 {
        match self._result {
            Some(r) => r,
            None => {
                self.run();
                self._result.unwrap()
            },
        }
    }

    pub fn change_noun(&mut self, new_val: u32) {
        self.program[1] = new_val;
        self._working_program[1] = new_val;
    }

    pub fn change_verb(&mut self, new_val: u32) {
        self.program[2] = new_val;
        self._working_program[2] = new_val;
    }
}


// Definition of all possible int code ops. There's probably a better way to do this.
fn get_op_by_id(id: u32) -> IntCodeOp {
    match id {
        1 => IntCodeOp { segment_length: 4, op_action: OpAction::Add },
        2 => IntCodeOp { segment_length: 4, op_action: OpAction::Multiply },
        99 => IntCodeOp { segment_length: 1, op_action: OpAction::Terminate },
        _ => panic!("Received an invalid op ID; must be one of { 1, 2, 99 }")
    }
}


enum OpAction {
    Add,
    Multiply,
    Terminate,
}


struct IntCodeOp {
    segment_length: u32,
    op_action: OpAction,
}


pub fn find_noun_and_verb_resulting_in(target_output: u32, program: &Vec<u32>) -> Option<(u32, u32)> {
    let cartesian = (0..100).cartesian_product(0..100);

    let _noun: u32;
    let _verb: u32;
    for (_noun, _verb) in cartesian {
        let mut computer = IntCodeComputer::new(program)    ;
        computer.change_noun(_noun);
        computer.change_verb(_verb);

        if computer.get_result() == target_output {
            return Option::Some((_noun, _verb));
        }
    }

    Option::None
}
