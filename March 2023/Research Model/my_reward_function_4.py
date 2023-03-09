def reward_function(params):
    if not params['all_wheels_on_track']:
        return float(0.001)

    track_width_half = params['track_width'] / 2
    quadratic_center = (params['distance_from_center'] / track_width_half) ** 4

    distance_from_center_reward = 1 - quadratic_center
    normalized_distance_from_center_reward = 0.5 + (distance_from_center_reward / 2)

    fast_around_track = (params['progress'] / params['steps']) * 100

    reward = (normalized_distance_from_center_reward * (fast_around_track ** 2)) * params['speed']

    return float(reward)
