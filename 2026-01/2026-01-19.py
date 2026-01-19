def compare_energy(c, w):
    cj = c * 4184
    wj = w * 3600
    if cj > wj: return "Workout"
    elif cj < wj: return "Devices"
    else: return "Equal"