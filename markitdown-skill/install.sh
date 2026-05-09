#!/usr/bin/env bash
# ==============================================================================
# MarkItDown Skill — One-Click Installer
# Auto-initializes all dependencies for the DeepSeek Agent self-contained skill.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="markitdown-skill"
VENV_DIR="$SCRIPT_DIR/.venv"
MIN_PYTHON="3.10"

# ── Colors ──────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

log()  { echo -e "${GREEN}[✓]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
err()  { echo -e "${RED}[✗]${NC} $*"; }

# ── Find Python ─────────────────────────────────────────────────────────
find_python() {
    for candidate in python3 python3.12 python3.11 python3.10 python; do
        if command -v "$candidate" &>/dev/null; then
            ver=$("$candidate" -c 'import sys; print(".".join(map(str, sys.version_info[:2])))' 2>/dev/null || true)
            if [ -n "$ver" ]; then
                major=$(echo "$ver" | cut -d. -f1)
                minor=$(echo "$ver" | cut -d. -f2)
                if [ "$major" -gt 3 ] || ([ "$major" -eq 3 ] && [ "$minor" -ge 10 ]); then
                    echo "$candidate"
                    return 0
                fi
            fi
        fi
    done
    return 1
}

PYTHON_BIN=$(find_python) || {
    err "Python >= ${MIN_PYTHON} is required. Please install Python ${MIN_PYTHON}+ first."
    exit 1
}
log "Using Python: $($PYTHON_BIN --version)"

# ── Create Virtual Environment ──────────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    log "Creating virtual environment: $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
else
    log "Virtual environment already exists: $VENV_DIR"
fi

# Activate
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate" 2>/dev/null || source "$VENV_DIR/Scripts/activate" 2>/dev/null || {
    err "Failed to activate virtual environment"
    exit 1
}
log "Virtual environment activated"

# ── Upgrade pip ─────────────────────────────────────────────────────────
log "Upgrading pip..."
pip install --upgrade pip -q

# ── Install Core Dependencies ──────────────────────────────────────────
log "Installing core dependencies..."
pip install -r "$SCRIPT_DIR/requirements.txt" -q
log "Core dependencies installed"

# ── Check exiftool (optional: image/audio metadata extraction) ──────────
if command -v exiftool &>/dev/null; then
    log "exiftool is available: $(which exiftool)"
else
    warn "exiftool not found (optional). Image/audio metadata extraction will be unavailable."
    warn "  Install: apt install exiftool / brew install exiftool / download from https://exiftool.org"
fi

# ── Verify ──────────────────────────────────────────────────────────────
log "Verifying installation..."
python -c "
from markitdown_skill import MarkItDown, __version__
md = MarkItDown()
print(f'MarkItDown Skill v{__version__} initialized successfully')
print(f'{len(md._converters)} converters registered')
" || {
    err "Installation verification failed. Check the error output above."
    exit 1
}

# ── Done ────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}══════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${GREEN}  MarkItDown Skill installed successfully!${NC}"
echo -e "${BOLD}${GREEN}══════════════════════════════════════════════════════════${NC}"
echo ""
echo "  Usage:"
echo "    source $VENV_DIR/bin/activate"
echo "    python -m markitdown_skill <file_path>"
echo ""
echo "  Or in Python:"
echo "    from markitdown_skill import MarkItDown"
echo "    md = MarkItDown()"
echo "    result = md.convert('example.pdf')"
echo "    print(result.markdown)"
echo ""
echo -e "  ${YELLOW}Note: This skill does NOT require any external LLM / API Key."
echo -e "  Image descriptions are handled by the DeepSeek Agent itself.${NC}"
echo ""
