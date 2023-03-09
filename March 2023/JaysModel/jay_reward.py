import math

def reward_function(params):

    # Read input parameters
    speed = params['speed']
    steering = abs(params['steering_angle'])
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    progress = params['progress']

    # Set the reward based on speed
    if speed < 1.0:
        reward = 1e-3
    else:
        reward = speed + 1

    # Penalize the agent for leaving the track or zig-zagging
    if distance_from_center > 0.5 * track_width:
        reward = 0.5
    elif abs(steering) > 15.0:
        reward= 0.8
    elif abs(steering) > 20.0:
        reward = 0.5

    # Compute the distance to the next waypoint
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # Penalize the agent for deviating from the centerline
    heading = params['heading']
    direction_diff = abs(track_direction - heading)
    if direction_diff > 15.0:
        reward= 0.8
    elif direction_diff > 20.0:
        reward *= 0.5

    # Reward the agent for making progress
    if progress >= 99.0:
        reward += 1000.0

    # Make the reward proportional to the time taken to complete 3 laps
    if progress >= 300.0:
        time_factor = (progress / 3.0) / 60.0
        reward /= time_factor

    return float(reward)
