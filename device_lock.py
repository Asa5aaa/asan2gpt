def generate_fingerprint(device):
    return f"{device['brand']}_{device['model']}_{device['android']}_{device['screen']}"
