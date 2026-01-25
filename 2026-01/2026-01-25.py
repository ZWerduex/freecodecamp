def scale_image(size, scale):
    return 'x'.join(str(int(int(n) * scale)) for n in size.split('x'))