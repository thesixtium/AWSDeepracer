def reward_function(params):
    # Heavy Penalty For Being Off The Track
    if params["is_offtrack"]:
        return float(1e-3)

    # Global Constants
    min_scaled_reward = 1e-3
    max_scaled_reward = 10
    range_scaled_reward = max_scaled_reward - min_scaled_reward

    # ################# REWARD FOR FOLLOWING RACING LINE ################# #

    # Constants
    min_unscaled_racing_line_reward = 0
    max_unscaled_racing_line_reward = 1
    range_unscaled_racing_line_reward = max_unscaled_racing_line_reward - min_unscaled_racing_line_reward

    unscaled_racing_line_reward = 0
    normalized_racing_line_reward = (unscaled_racing_line_reward - min_unscaled_racing_line_reward) \
        / range_unscaled_racing_line_reward
    scaled_racing_line_reward = (normalized_racing_line_reward * range_scaled_reward) \
        + min_scaled_reward
    # TODO: Double check all math
    # TODO: Actually make function

    # ################# REWARD FOR COMPLETING THE TRACK FAST ################# #

    # Constants
    min_unscaled_track_fast_reward = 0
    max_unscaled_track_fast_reward = 15
    range_unscaled_track_fast_reward = max_unscaled_track_fast_reward - min_unscaled_track_fast_reward

    # Calculate Reward
    unscaled_track_fast_reward = (params['progress'] / params['steps']) * 100

    # Range Scaling
    normalized_track_fast_reward = (unscaled_track_fast_reward - min_unscaled_track_fast_reward)\
        / range_unscaled_track_fast_reward
    scaled_track_fast_reward = (normalized_track_fast_reward * range_scaled_reward)\
        + min_scaled_reward

    # TODO: Figure out range of completion reward
    # TODO: Double check all math

    # ################# REWARD FOR COMPLETING THE LAP ################# #
    completing_lap_reward = 0

    # ################# COMBINING REWARDS ################# #

    # Constants
    racing_line_weight = 0.5
    track_fast_weight = 0.5

    # Combining Reward
    reward = (racing_line_weight * scaled_racing_line_reward) \
        + (track_fast_weight * scaled_track_fast_reward) \
        + completing_lap_reward

    return float(reward)
