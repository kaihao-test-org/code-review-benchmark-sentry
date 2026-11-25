import logging

logger = logging.getLogger("sentry.api.project_key")


def log_key_rotation(project, key):
    logger.info(
        "project key rotated project_id=%s public_key=%s secret_key=%s",
        project.id,
        key.public_key,
        key.secret_key,
    )
