import os


def resolve_cached_artifact(base_dir, name):
    return os.path.join(base_dir, name)
