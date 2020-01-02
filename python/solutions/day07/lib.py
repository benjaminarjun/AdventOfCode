import itertools
from ..intcode_computer.core import IntcodeProgramRunner, RunnerState


def get_max_pipeline_output(program, pipeline_in_feedback_mode):
    phase_settings_options = pipeline_in_feedback_mode and range(5, 10) or range(5)
    phase_setting_permutations = itertools.permutations(phase_settings_options)

    max_output, max_output_phase_settings = None, None
    for phase_settings in phase_setting_permutations:
        output_val = _run_amplifier_pipeline(program, phase_settings, pipeline_in_feedback_mode)

        if max_output is None or output_val > max_output:
            max_output = output_val
            max_output_phase_settings = phase_settings

    return max_output, max_output_phase_settings


def _run_amplifier_pipeline(program, phase_settings, pipeline_in_feedback_mode):
    input_val = 0

    pipeline = [IntcodeProgramRunner.from_str(program, pause_at_first_output=pipeline_in_feedback_mode)
        for _ in range(5)]
    iteration = 0

    while any([runner.run_state != RunnerState.Complete for runner in pipeline]):
        pipeline_ix = iteration % len(pipeline)
        runner = pipeline[pipeline_ix]

        # Build input list for each iteration; phase setting only passed on the initial run for each computer.
        input_vals = []
        if iteration < len(pipeline):
            input_vals.append(phase_settings[pipeline_ix])
        input_vals.append(input_val)

        output_val = runner.run(input_vals, debug=False)
        input_val = output_val

        iteration += 1

    return output_val
