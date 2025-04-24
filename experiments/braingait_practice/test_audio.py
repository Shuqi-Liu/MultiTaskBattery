# Main Script to play a sample audio file that's similar to what they will
# hear in the real expeirment

import constants_practice as const
from psychopy import sound

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
    # use the same .wave file but shorter to preserve the sound volume,
    # voice and content similarity as much as possible. It's a shorter
    # version of what they will hear in practice, and different then what
    # they will hear during the actual task.
    practice_soundpath = const.stim_dir / 'auditory_narrative' / \
                         'narrative_05-trimmed.wav'
    practice_sound = sound.Sound(str(practice_soundpath))
    practice_sound.play()
    return


if __name__ == "__main__":
    main('subject-00') #need to have this as a default value to get us
    # started, otherwise will error out
