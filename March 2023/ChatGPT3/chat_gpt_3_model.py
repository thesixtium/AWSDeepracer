import math

def reward_function(params):
    
    # Read input variables
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    heading = params['heading']
    progress = params['progress']
    steps = params['steps']
    all_wheels_on_track = params['all_wheels_on_track']
    closest_waypoints = params['closest_waypoints']
    waypoints = params['waypoints']
    
    # Set base reward
    reward = 1e-3

    # Give a higher reward if the car stays on the track
    if all_wheels_on_track:
        reward += 1.0
    
    # Give a higher reward if the car is closer to the center of the track
    if distance_from_center <= 0.1 * track_width:
        reward += 0.5
    
    # Give a higher reward if the car is moving at a faster speed
    if speed > 0.9:
        reward += 0.5

    # Calculate the optimal racing line based on the two closest waypoints
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    # Penalize the car for deviating from the optimal racing line
    if direction_diff > 30:
        reward -= 0.5
        
    # Give a higher reward if the car is making progress towards the finish line
    reward += (progress / steps) * 100
        
    # Give a higher reward if the car completes the track in the allotted time
    if progress == 100:
        reward += 2.0

    return float(reward)
