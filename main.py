from unityparser import UnityDocument
import os

def run():
    default_path = os.getenv("GITHUB_WORKSPACE")
    print(default_path)
    return


run()