#!/usr/bin/env python3
"""Portable environment discovery for the generic-agent-code-run skill.

The skill must not hardcode a machine-specific GenericAgent path. Configure one of:
- GENERIC_AGENT_ROOT: path to a GenericAgent checkout/root directory.
- GENERIC_AGENT_PYTHON: path to a Python executable with required desktop deps.

If neither is set, helpers try non-invasive discovery from the current working
folder and the skill folder ancestors, then return truthful unavailable status.
"""
import os
import sys
from pathlib import Path


def _looks_like_generic_agent_root(path: Path) -> bool:
    return any((path / marker).exists() for marker in ["ga.py", "TMWebDriver.py", "assets", "memory"])


def configured_generic_agent_root():
    raw = os.environ.get("GENERIC_AGENT_ROOT")
    if not raw:
        return None
    path = Path(raw).expanduser()
    try:
        return path.resolve()
    except Exception:
        return path


def discover_generic_agent_root(start: Path | None = None):
    configured = configured_generic_agent_root()
    if configured:
        return configured

    starts = []
    if start:
        starts.append(Path(start))
    starts.extend([Path.cwd(), Path(__file__).resolve()])

    seen = set()
    for base in starts:
        try:
            base = base.resolve()
        except Exception:
            pass
        for path in [base, *base.parents]:
            key = str(path).lower()
            if key in seen:
                continue
            seen.add(key)
            if _looks_like_generic_agent_root(path):
                return path
            sibling = path / "GenericAgent"
            if sibling.exists() and _looks_like_generic_agent_root(sibling):
                return sibling
    return None


def configured_python():
    raw = os.environ.get("GENERIC_AGENT_PYTHON")
    if not raw:
        return None
    path = Path(raw).expanduser()
    return path if path.exists() else None


def find_worker_python(root: Path | None = None):
    explicit = configured_python()
    if explicit:
        return explicit
    root = root or discover_generic_agent_root()
    if not root:
        return None
    for candidate in [root / ".venv" / "Scripts" / "python.exe", root / "venv" / "Scripts" / "python.exe", root / ".venv" / "bin" / "python", root / "venv" / "bin" / "python"]:
        if candidate.exists():
            return candidate
    return None


def add_generic_agent_paths(root: Path | None = None):
    root = root or discover_generic_agent_root()
    added = []
    if not root:
        return None, added
    candidates = [
        root,
        root / "memory",
        root / ".venv" / "Lib" / "site-packages",
        root / "venv" / "Lib" / "site-packages",
        root / ".venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages",
        root / "venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages",
    ]
    for path in candidates:
        if path.exists():
            s = str(path)
            if s not in sys.path:
                sys.path.insert(0, s)
                added.append(s)
    return root, added


def env_status(root: Path | None = None):
    root = root or discover_generic_agent_root()
    worker = find_worker_python(root)
    return {
        "generic_agent_root_configured": bool(os.environ.get("GENERIC_AGENT_ROOT")),
        "generic_agent_python_configured": bool(os.environ.get("GENERIC_AGENT_PYTHON")),
        "generic_agent_root": str(root) if root else None,
        "generic_agent_root_exists": bool(root and root.exists()),
        "worker_python": str(worker) if worker else None,
        "worker_python_exists": bool(worker and worker.exists()),
        "current_python": sys.executable,
    }
