import os

from pdm.backend.hooks.version import SCMVersion  # type: ignore[import-not-found]


def format_version(version: SCMVersion) -> str:
    if version.distance is None and not version.dirty:
        # Official version
        return str(version.version)
    elif os.getenv("PYPI_PUBLISH"):
        # Published version
        return f"{version.version}.dev{version.distance or ''}"
    else:
        # Local version
        return f"{version.version}.dev{version.distance or ''}+{version.node}"
