from  utils.capture_window import WindowCapture

if __name__ == "__main__":
    # Update the window_name variable with the title of your game window
    window_name = "LDPlayer"
    interval_seconds = 2

    wincap = WindowCapture(window_name)
    wincap.generate_image_dataset(interval_seconds, 300)
