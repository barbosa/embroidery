def default_output(input_path):
    parts = input_path.split(".")
    parts[-2] = parts[-2] + "_embroidered"
    return ".".join(parts)
