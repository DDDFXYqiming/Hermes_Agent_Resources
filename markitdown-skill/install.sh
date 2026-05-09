#!/usr/bin/env bash
# ==============================================================================
# MarkItDown Skill — 一键安装脚本
# 为 DeepSeek Agent 自包含 Skill 自动初始化所有依赖
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="markitdown-skill"
VENV_DIR="$SCRIPT_DIR/.venv"
MIN_PYTHON="3.10"

# ── 颜色 ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

log()  { echo -e "${GREEN}[✓]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
err()  { echo -e "${RED}[✗]${NC} $*"; }

# ── 检查 Python ────────────────────────────────────────────────────────────
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
    err "需要 Python >= ${MIN_PYTHON}，未找到。请先安装 Python ${MIN_PYTHON}+。"
    exit 1
}
log "使用 Python: $($PYTHON_BIN --version)"

# ── 创建虚拟环境 ────────────────────────────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    log "创建虚拟环境: $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
else
    log "虚拟环境已存在: $VENV_DIR"
fi

# 激活
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate" 2>/dev/null || source "$VENV_DIR/Scripts/activate" 2>/dev/null || {
    err "无法激活虚拟环境"
    exit 1
}
log "虚拟环境已激活"

# ── 升级 pip ────────────────────────────────────────────────────────────────
log "升级 pip..."
pip install --upgrade pip -q

# ── 安装核心依赖 ────────────────────────────────────────────────────────────
log "安装核心依赖..."
pip install -r "$SCRIPT_DIR/requirements.txt" -q
log "核心依赖安装完成"

# ── 检查 exiftool (可选: 图片/音频元数据提取) ────────────────────────────────
if command -v exiftool &>/dev/null; then
    log "exiftool 已可用: $(which exiftool)"
else
    warn "exiftool 未安装（可选）。图片/音频元数据提取将不可用。"
    warn "  安装方法: apt install exiftool / brew install exiftool / 下载 https://exiftool.org"
fi

# ── 验证 ────────────────────────────────────────────────────────────────────
log "验证安装..."
python -c "
from markitdown_skill import MarkItDown, __version__
md = MarkItDown()
print(f'MarkItDown Skill v{__version__} 初始化成功')
print(f'已注册 {len(md._converters)} 个转换器')
" || {
    err "安装验证失败，请检查错误信息。"
    exit 1
}

# ── 完成 ────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${GREEN}══════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${GREEN}  MarkItDown Skill 安装完成！${NC}"
echo -e "${BOLD}${GREEN}══════════════════════════════════════════════════════════${NC}"
echo ""
echo "  使用方式:"
echo "    source $VENV_DIR/bin/activate"
echo "    python -m markitdown_skill <文件路径>"
echo ""
echo "  或直接在 Python 中:"
echo "    from markitdown_skill import MarkItDown"
echo "    md = MarkItDown()"
echo "    result = md.convert('example.pdf')"
echo "    print(result.markdown)"
echo ""
echo -e "  ${YELLOW}注意：此 Skill 不依赖外部 LLM / API Key。"
echo -e "  图片描述由 DeepSeek Agent 自身多模态能力处理。${NC}"
echo ""
