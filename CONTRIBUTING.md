# Contributing to NWF Stock Screener

First off, thank you for considering contributing! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, browser, Python version)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- **Clear description** of the feature
- **Use case** - why it would be useful
- **Possible implementation** approach

### 🔧 Pull Requests

1. Fork the repo
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open Pull Request

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Add docstrings
- Maximum line length: 88 characters (Black formatter)

**JavaScript:**
- Use ES6+ features
- Consistent indentation (2 spaces)
- Add comments for complex logic

**HTML/CSS:**
- Semantic HTML5
- Mobile-first responsive design
- Use CSS variables for theming

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/nwf-stock-screener.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies (if any)
pip install -r requirements.txt

# Run updater script
python update_nwf_metrics.py
```

## Testing

Before submitting PR:

1. Test with sample data
2. Verify all filters work correctly
3. Check mobile responsiveness
4. Ensure no console errors
5. Update documentation if needed

## Project Roadmap

Check [Issues](https://github.com/yourusername/nwf-stock-screener/issues) for:
- 🏷️ `good first issue` - Perfect for beginners
- 🏷️ `help wanted` - Need community input
- 🏷️ `enhancement` - New features
- 🏷️ `bug` - Bug fixes needed

## Community

- 💬 [Discord Server](https://discord.gg/xxx)
- 📧 Email: your.email@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🙏**
