# Main Script for an example experiment
import sys

# sys.path.append('../../../MultiTaskBattery/')
sys.path.insert(0,
                '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML/Projects/BrainGaitProject/MultiTaskBattery/')

import MultiTaskBattery.experiment_block as exp_block
import constants as const


def main(subj_id):
    """ Main experiment function.
    Ensure the constants.py file is updated before running the experiment
    (e.g., experiment name, eye tracker, screen settings, etc.).

    Args:
        subj_id (str): Subject ID
    """
    # sys.path.insert(0,
    # '/Users/mac/Library/CloudStorage/OneDrive-UniversityofPittsburgh/SML
    # /Projects/BrainGaitProject/MultiTaskBattery')
    my_Exp = exp_block.Experiment(const, subj_id=subj_id)
    #while True:
    my_Exp.confirm_run_info()#when run_info window is up, click cancel in
    # the dialog or press ESC will quit the program
    my_Exp.init_run()
    my_Exp.run()

    #no gradeful of existing the run half-way, have to force close the
    # program or use task manager. There is no also no way to start the run
    # from the middle. If something is wrong in the middle, quit,
    # then restart the current run, or restart but with a different
    # randomization number (3 or 4). This is consistent with the scanner,
    # no way to savage data halfway, the full run has to be repeated.
    return


if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
