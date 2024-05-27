from TP4.config import config


def constant(i):
    return config.get("kohonen").get("radius")


def decreasing(i):
    return int(config.get("kohonen").get("max_radius") - (i / config.get("kohonen").get("limit")) * (
                config.get("kohonen").get("max_radius") - config.get("kohonen").get("min_radius")))
