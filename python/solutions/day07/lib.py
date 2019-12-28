import itertools
from ..intcode_computer.core import IntcodeProgramRunner


def get_max_pipeline_output(program):
    phase_setting_permutations = itertools.permutations(range(5))

    max_output, max_output_phase_settings = None, None
    for phase_settings in phase_setting_permutations:
        output_val = _run_amplifier_pipeline(program, phase_settings)

        if max_output is None or output_val > max_output:
            max_output = output_val
            max_output_phase_settings = phase_settings

    return max_output, max_output_phase_settings


def _run_amplifier_pipeline(program, phase_settings):
    input_val = 0
    for phase_setting in phase_settings:
        runner = IntcodeProgramRunner.from_str(program)
        output_val = runner.run([phase_setting, input_val])
        input_val = output_val

    return output_val
