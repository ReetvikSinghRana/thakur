import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import thakur64enc
elif bit == '32bit':
    import thakur32enc
