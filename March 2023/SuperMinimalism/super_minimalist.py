def reward_function(params):
    if params['all_wheels_on_track']:
        return float(params['progress'] / params['steps'])
    else:
        return(1e-3)
