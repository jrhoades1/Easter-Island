#!/bin/bash
set -euo pipefail

# Only run dependency setup in Claude Code on the web (remote) environments.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# Install the project with dev and llm extras so tests, linters, and the
# LLM-powered agents all work. pip is used (not a locked install) so the
# resulting container state caches well across sessions.
pip install --quiet --break-system-packages -e ".[dev,llm]"
