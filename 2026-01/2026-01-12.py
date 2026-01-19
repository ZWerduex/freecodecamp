def get_number_of_plants(field_size, unit, crop):
    crops = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }
    units = {
        "acres": 4046.86,
        "hectares": 10000
    }
    return int(field_size * units[unit] / crops[crop])