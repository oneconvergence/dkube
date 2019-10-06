from dkube.sdk import dkube
import os

if __name__ == "__main__":
    print(dkube.Environment().internal.url)
    print(os.getenv("DKUBE_STORE_ACCESS_KEY"))
