def reward_function(params):
    
    # Huge penalties
    if not params['all_wheels_on_track']:
        return float(1e-3)

    # Base Reward
    reward = 0
    if params['speed'] > 0.9:
        reward = 1 + (2 * params['speed'])
    else:
        reward = 1e-3
    
    # Center the car
    track_width_half = params['track_width'] / 2
    quadratic_center = (params['distance_from_center'] / track_width_half) ** 4
    distance_from_center_reward = 1 - quadratic_center
    reward += distance_from_center_reward

    # Give a higher reward if the car is making progress towards the finish line
    reward += (params['progress'] / params['steps']) * 100
        
    # Give a higher reward if the car completes the track in the allotted time
    if params['progress'] == 100:
        reward += 2
    
    return float(reward)
