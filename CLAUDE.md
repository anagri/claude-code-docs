# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based documentation scraper that downloads Claude Code documentation from the Anthropic website, converts it to Markdown, and serves it locally. The primary purpose is to maintain a local copy of Claude Code documentation for offline reference and context provision.

## Architecture

### Core Component: DocumentationScraper Class

The entire scraper is implemented as a single class (`DocumentationScraper` in `main.py`) with the following responsibilities:

1. **HTML Downloading** (`scrape_documentation`, `download_html`)
   - Crawls Claude Code docs starting from base URL
   - Discovers links recursively within the documentation
   - Maintains URL tracking in `html/db.yaml` to avoid duplicate downloads
   - Preserves directory structure when saving HTML files

2. **Link Rewriting** (`rewrite_all_links`, `rewrite_links_in_html`)
   - Converts absolute URLs to relative paths for local serving
   - Processes links, CSS, and JavaScript references
   - Enables offline browsing of downloaded documentation

3. **HTML to Markdown Conversion** (`convert_html_to_markdown`)
   - Extracts main content using multiple fallback strategies
   - Prioritizes mdx-content divs (Anthropic-specific)
   - Falls back to semantic HTML5 elements (main, article)
   - Removes navigation, headers, footers, and sidebar elements
   - Uses html2text library for conversion with custom configuration

4. **Content Cleaning** (`extract_main_content`, `clean_html_content`, `clean_markdown`)
   - Removes navigation and layout elements before conversion
   - Fixes header formatting and table structures
   - Cleans up invisible characters and excessive whitespace
   - Adds original URL header to each Markdown file

5. **Local Web Server** (`create_web_server`)
   - Flask-based server for browsing downloaded HTML documentation
   - Handles routing with directory structure support
   - Serves on port 8000 by default

### Directory Structure

```
/
├── main.py              # Single-file implementation
├── pyproject.toml       # UV package configuration
├── downloads/          # Current download (git-ignored)
│   ├── meta.json      # Tracks download date for idempotency
│   ├── html/          # Downloaded HTML files
│   │   ├── db.yaml   # URL tracking database
│   │   └── *.html    # Documentation pages (preserves site structure)
│   └── md/           # Converted Markdown files
│       └── *.md      # Mirrors html/ structure
└── archive/           # Historical downloads (git-ignored)
    └── YYYYMMDD/     # Date-based archive folders
        ├── html/     # Archived HTML files
        └── md/       # Archived Markdown files
```

### Data Flow

1. **Archive Check**: Compare `meta.json` date with current date
   - Same date → Continue (idempotent)
   - Different date → Move downloads to `archive/YYYYMMDD/` and start fresh
2. **Download**: URL → HTML (saved to `downloads/html/` + tracked in `db.yaml`)
3. **Rewrite**: HTML links converted from absolute to relative paths
4. **Convert**: HTML → Markdown (extracted content saved to `downloads/md/`)
5. **Serve**: Flask serves HTML files locally (optional)

## Commands

### Running the Scraper

The tool uses UV for dependency management. All commands use the Click CLI framework:

```bash
# Download HTML documentation
python main.py --html

# Convert HTML to Markdown
python main.py --md

# Serve documentation locally on port 8000
python main.py --serve

# Serve on custom port
python main.py --serve --port 8080

# Download from custom URL
python main.py --html --url https://docs.anthropic.com/en/docs/claude-code/

# Full workflow: download, convert, serve
python main.py --html --md --serve
```

### Development Setup

```bash
# Install dependencies (UV will create/activate .venv automatically)
uv sync

# Run the scraper
uv run python main.py --html --md
```

## Key Implementation Details

### Content Extraction Strategy

The scraper uses a cascading fallback approach for extracting main content:

1. Look for Anthropic-specific `mdx-content` div
2. Try `content-area` div (with header removal)
3. Try `prose` class divs
4. Fall back to semantic `<main>` element
5. Try `<article>` element
6. Last resort: body with aggressive navigation removal

### HTML2Text Configuration

The converter is configured with specific settings (main.py:38-46):
- No line wrapping (`body_width = 0`)
- Unicode characters preserved (`unicode_snob = True`)
- Proper code block marking (`mark_code = True`)
- Links and images retained

### URL to Path Mapping

URLs are converted to file paths by:
- Stripping base URL prefix
- Extracting path after `/claude-code/`
- Cleaning protocol and domain artifacts
- Appending `.html` extension
- Creating parent directories as needed

### Database Format

`downloads/html/db.yaml` tracks downloaded files:
```yaml
- url: https://docs.anthropic.com/en/docs/claude-code/setup
  filepath: setup.html
```

### Meta Format

`downloads/meta.json` tracks download date for idempotency:
```json
{
  "download_date": "20251005"
}
```

## Idempotency & Archiving Behavior

### Same-Date Re-runs (Idempotent)
- If you run the scraper multiple times on the same date, it continues where it left off
- Uses `db.yaml` to skip already-downloaded URLs
- Perfect for crash recovery or interrupted downloads

### Different-Date Re-runs (Archiving)
- When running on a new date, the system automatically:
  1. Moves `downloads/html/` and `downloads/md/` to `archive/YYYYMMDD/`
  2. Updates `meta.json` with the new date
  3. Starts a fresh download
- This preserves historical snapshots of documentation

### Example Flow
```bash
# Day 1 (Oct 4): First download
python main.py --html --md
# Creates: downloads/html/, downloads/md/, downloads/meta.json {"download_date": "20251004"}

# Day 1 (Oct 4): Script crashes, re-run
python main.py --html --md
# Output: "Continuing download for 20251004 (idempotent)"
# Resumes using existing db.yaml

# Day 2 (Oct 5): New download
python main.py --html --md
# Output: "Archiving previous download to archive/20251004/"
# Creates: archive/20251004/html/, archive/20251004/md/
# Starts fresh in downloads/ with new date
```

## Typical Workflow

### Local Development

When updating documentation locally:

1. Run `make run` (or `python main.py --html --md`)
   - On first run of the day: Archives previous download, starts fresh
   - On subsequent runs same day: Continues existing download
2. Markdown files in `downloads/md/` serve as reference material for understanding Claude Code capabilities
3. Historical versions are preserved in `archive/YYYYMMDD/` folders

### Automated Daily Releases (GitHub Actions)

The repository includes `.github/workflows/daily-docs-release.yml` that:

1. **Triggers:** Daily at midnight UTC (cron: `0 0 * * *`) + manual via workflow_dispatch
2. **Process:**
   - Sets up uv and Python environment
   - Runs `make setup && make run`
   - Extracts date from `downloads/meta.json`
   - Creates GitHub Release with tag `docs-YYYYMMDD`
3. **Release Assets:**
   - `claude-code-docs-YYYYMMDD.tar.gz` - Complete download
   - `html-YYYYMMDD.tar.gz` - HTML files only
   - `md-YYYYMMDD.tar.gz` - Markdown files only
4. **Release Notes:** Auto-generated with download stats and usage instructions

This provides daily snapshots of Claude Code documentation accessible via GitHub Releases, eliminating the need to run the scraper manually for most users.
