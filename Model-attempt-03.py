def reward_function(params):
    # Read input parameters
    distance_from_center = params['distance_from_center']
    is_offtrack = params['is_offtrack']
    progress = params['progress']
    steps = params['steps']
    track_width = params['track_width']

    # No going off track
    if is_offtrack:
        reward = 0.001
        return float(reward)

    # Encourage staying in the center
    track_width_half = track_width / 2
    quadratic_center = (distance_from_center / track_width_half) ** 4
    distance_from_center_reward = 1 - quadratic_center
    normalized_distance_from_center_reward = 0.5 + (distance_from_center_reward / 2)

    # Encourage going around the track fast
    fast_around_track = (progress / steps)

    # Final reward
    reward = normalized_distance_from_center_reward * fast_around_track

    return float(reward)
