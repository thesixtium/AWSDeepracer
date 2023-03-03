def reward_function(params):

    # Heavy Penalty For Being Off The Track
    if params["is_offtrack"]:
        return float(1e-3)

    # Base Reward For Existing
    reward = 1

    # Reward For Following Racing Line
    # TODO: Figure out range of racing line reward

    # Reward For Completing The Track Fast
    # TODO: Figure out range of completion reward

    # Completing Lap

    return float(reward)
