#!/usr/bin/env bash
# install_deps.sh - Install dependencies for video-notes-generator skill
# Idempotent: safe to run multiple times.

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_ok()   { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $1"; }

ERRORS=()
WARNINGS=()

# --- Check Python 3.10+ ---
echo "=== Checking Python ==="
if command -v python3 &>/dev/null; then
    PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PY_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
    PY_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
    if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 10 ]; then
        log_ok "Python $PY_VERSION found"
    else
        log_fail "Python 3.10+ required, found $PY_VERSION"
        ERRORS+=("Python version too old: $PY_VERSION")
    fi
else
    log_fail "Python3 not found"
    ERRORS+=("Python3 not installed")
fi

# --- Check ffmpeg ---
echo ""
echo "=== Checking ffmpeg ==="
if command -v ffmpeg &>/dev/null; then
    FF_VERSION=$(ffmpeg -version 2>&1 | head -1)
    log_ok "ffmpeg found: $FF_VERSION"
else
    log_fail "ffmpeg not found"
    ERRORS+=("ffmpeg not installed")
    echo "  Install instructions:"
    echo "    Ubuntu/Debian: sudo apt install ffmpeg"
    echo "    macOS:         brew install ffmpeg"
    echo "    Windows:       choco install ffmpeg"
    echo "    Conda:         conda install -c conda-forge ffmpeg"
fi

# --- Install pip packages ---
echo ""
echo "=== Installing Python packages ==="
PIP_PACKAGES=(
    "yt-dlp"
    "openai"
    "requests"
    "python-dotenv"
    "faster-whisper"
    "pydantic"
)

for pkg in "${PIP_PACKAGES[@]}"; do
    if python3 -c "import ${pkg//-/_}" 2>/dev/null || pip show "$pkg" &>/dev/null; then
        log_ok "$pkg already installed"
    else
        echo "  Installing $pkg..."
        if pip install "$pkg" -q; then
            log_ok "$pkg installed"
        else
            log_fail "Failed to install $pkg"
            ERRORS+=("pip install $pkg failed")
        fi
    fi
done

# --- Summary ---
echo ""
echo "========================================="
echo "  Installation Summary"
echo "========================================="

if [ ${#ERRORS[@]} -eq 0 ]; then
    log_ok "All dependencies installed successfully!"
    echo ""
    echo "You can now use the video-notes-generator skill."
    echo "Copy templates/.env.example to .env and fill in your API keys."
else
    log_fail "${#ERRORS[@]} error(s) encountered:"
    for err in "${ERRORS[@]}"; do
        echo "  - $err"
    done
    exit 1
fi
