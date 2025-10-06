#!/usr/bin/env python3
"""Development environment setup script."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def install_ruff():
    """Install ruff for linting and formatting."""
    try:
        run_command([sys.executable, "-m", "pip", "install", "ruff"])
        print("✅ Ruff installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install ruff: {e}")
        return False
    return True


def setup_pre_commit():
    """Set up pre-commit hooks."""
    pre_commit_hook = Path(".git/hooks/pre-commit")
    
    if not Path(".git").exists():
        print("⚠️  Not a git repository, skipping pre-commit setup")
        return
    
    hook_content = """#!/bin/sh
# Pre-commit hook to run ruff checks

echo "Running ruff checks..."

# Check formatting
ruff format --check .
if [ $? -ne 0 ]; then
    echo "❌ Code is not properly formatted. Run 'make format' to fix."
    exit 1
fi

# Check linting
ruff check .
if [ $? -ne 0 ]; then
    echo "❌ Linting errors found. Run 'make fix' to auto-fix or manually fix the issues."
    exit 1
fi

echo "✅ All checks passed!"
"""
    
    try:
        pre_commit_hook.write_text(hook_content)
        pre_commit_hook.chmod(0o755)
        print("✅ Pre-commit hook installed")
    except Exception as e:
        print(f"❌ Failed to setup pre-commit hook: {e}")


def create_vscode_settings():
    """Create VS Code settings for ruff integration."""
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)
    
    settings = {
        "python.linting.enabled": True,
        "python.linting.ruffEnabled": True,
        "python.formatting.provider": "none",
        "[python]": {
            "editor.defaultFormatter": "charliermarsh.ruff",
            "editor.formatOnSave": True,
            "editor.codeActionsOnSave": {
                "source.organizeImports": True,
                "source.fixAll": True
            }
        },
        "ruff.organizeImports": True,
        "ruff.fixAll": True
    }
    
    import json
    settings_file = vscode_dir / "settings.json"
    
    try:
        with settings_file.open("w") as f:
            json.dump(settings, f, indent=2)
        print("✅ VS Code settings created")
    except Exception as e:
        print(f"❌ Failed to create VS Code settings: {e}")


def main():
    """Main setup function."""
    print("🚀 Setting up development environment...")
    
    # Install ruff
    if not install_ruff():
        sys.exit(1)
    
    # Setup pre-commit hooks
    setup_pre_commit()
    
    # Create VS Code settings
    create_vscode_settings()
    
    print("\n🎉 Development environment setup complete!")
    print("\nNext steps:")
    print("  1. Run 'make check' to verify everything is working")
    print("  2. Run 'make fix' to format and fix any issues")
    print("  3. Install the Ruff VS Code extension for better integration")


if __name__ == "__main__":
    main() 