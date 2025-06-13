import os
import platform

def get_the_driver_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if platform.system() == "Darwin":
        # macOS için
        driver_path = os.path.join(base_dir, "../chromedriver-mac/chromedriver")
    elif platform.system() == "Windows":
        # Windows için
        driver_path = os.path.join(base_dir, "../chromedriver-win/chromedriver.exe")
    else:
        raise Exception("Desteklenmeyen işletim sistemi")

    return os.path.abspath(driver_path)