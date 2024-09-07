"""
Get the version from Git - PDM hook
"""

# ruff: noqa: I001
import os

from pdm.backend.hooks.version import SCMVersion  # type: ignore[import-not-found,unused-ignore] # pylint: disable=import-error


def format_version(version: SCMVersion) -> str:
    """Format Git version"""
    if version.distance is None and not version.dirty:
        # Official version
        return str(version.version)
    if os.getenv("PYPI_PUBLISH"):
        # Published version
        return f"{version.version}.dev{version.distance or ''}"
    # Local version
    return f"{version.version}.dev{version.distance or ''}+{version.node}"
