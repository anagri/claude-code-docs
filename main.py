#!/usr/bin/env python3
"""
Claude Code Documentation Scraper and Local Server

This tool downloads HTML documentation from Anthropic's Claude Code docs,
preserves directory structure, converts links to relative paths, and serves
the site locally.
"""

import os
import re
import sys
import yaml
import json
import click
import requests
import shutil
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import html2text
from typing import List, Dict, Optional
from flask import Flask, send_from_directory, abort, redirect


class DocumentationScraper:
  """Handles downloading, converting, and serving Claude Code documentation."""
  
  def __init__(self, base_dir: Path):
    self.base_dir = base_dir
    self.downloads_dir = base_dir / "downloads"
    self.archive_dir = base_dir / "archive"
    self.html_dir = self.downloads_dir / "html"
    self.md_dir = self.downloads_dir / "md"
    self.db_file = self.downloads_dir / "db.yaml"
    self.meta_file = self.downloads_dir / "meta.json"
    # Base URL - docs.anthropic.com redirects to docs.claude.com
    self.base_url = "https://docs.claude.com/en/docs/claude-code/"
    self.legacy_base_url = "https://docs.anthropic.com/en/docs/claude-code/"

    # Handle archiving based on date
    self._handle_archiving()

    # Ensure directories exist
    self.downloads_dir.mkdir(exist_ok=True)
    self.html_dir.mkdir(parents=True, exist_ok=True)
    self.md_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize HTML to text converter
    self.h2t = html2text.HTML2Text()
    self.h2t.ignore_links = False
    self.h2t.ignore_images = False
    self.h2t.ignore_emphasis = False
    self.h2t.body_width = 0  # Don't wrap lines
    self.h2t.unicode_snob = True  # Use unicode characters
    self.h2t.escape_snob = True  # Escape special characters properly
    self.h2t.mark_code = True  # Mark code blocks properly

  def _get_current_date(self) -> str:
    """Get current date in YYYYMMDD format."""
    return datetime.now().strftime("%Y%m%d")

  def _load_meta(self) -> Dict:
    """Load meta.json file with download date."""
    if not self.meta_file.exists():
      return {}

    try:
      with open(self.meta_file, 'r', encoding='utf-8') as f:
        return json.load(f)
    except Exception as e:
      click.echo(f"Error loading meta.json: {e}", err=True)
      return {}

  def _save_meta(self, data: Dict):
    """Save meta.json file with download date."""
    try:
      with open(self.meta_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    except Exception as e:
      click.echo(f"Error saving meta.json: {e}", err=True)

  def _mark_completed(self):
    """Mark the current download as completed in meta.json."""
    meta = self._load_meta()
    if meta:
      meta["status"] = "completed"
      self._save_meta(meta)
      click.echo(f"Marked download as completed in meta.json")

  def _handle_archiving(self):
    """Archive old downloads if date has changed."""
    current_date = self._get_current_date()

    # Check if downloads directory exists
    if not self.downloads_dir.exists():
      # First run, create meta.json with current date and processing status
      self.downloads_dir.mkdir(parents=True, exist_ok=True)
      self._save_meta({"download_date": current_date, "status": "processing"})
      click.echo(f"Starting new download for {current_date}")
      return

    # Load existing meta
    meta = self._load_meta()
    last_date = meta.get("download_date")
    last_status = meta.get("status")

    if last_date is None:
      # Meta file doesn't exist or is empty, create it
      self._save_meta({"download_date": current_date, "status": "processing"})
      click.echo(f"Starting new download for {current_date}")
      return

    if last_date == current_date:
      # Same date - check if previous run completed
      if last_status == "completed":
        # Previous download completed successfully
        click.echo(f"Download already completed for {current_date} - skipping (idempotent)")
        return
      else:
        # Previous download was interrupted or incomplete
        click.echo(f"WARNING: Previous download for {current_date} was incomplete (status: {last_status})")
        click.echo(f"Cleaning up and restarting from scratch...")

        # Clean up incomplete download
        if self.html_dir.exists():
          shutil.rmtree(self.html_dir)
        if self.md_dir.exists():
          shutil.rmtree(self.md_dir)
        if self.db_file.exists():
          self.db_file.unlink()

        # Reset meta to processing
        self._save_meta({"download_date": current_date, "status": "processing"})
        click.echo(f"Starting fresh download for {current_date}")
        return

    # Different date, archive the old download
    click.echo(f"Date changed from {last_date} to {current_date}")
    click.echo(f"Archiving previous download to archive/{last_date}/")

    # Create archive directory
    archive_date_dir = self.archive_dir / last_date
    archive_date_dir.mkdir(parents=True, exist_ok=True)

    # Move db.yaml to archive
    if self.db_file.exists():
      archive_db = archive_date_dir / "db.yaml"
      if archive_db.exists():
        archive_db.unlink()
      shutil.move(str(self.db_file), str(archive_db))
      click.echo(f"  Moved db.yaml to archive/{last_date}/db.yaml")

    # Move html and md directories to archive
    if self.html_dir.exists():
      archive_html = archive_date_dir / "html"
      if archive_html.exists():
        shutil.rmtree(archive_html)
      shutil.move(str(self.html_dir), str(archive_html))
      click.echo(f"  Moved html/ to archive/{last_date}/html/")

    if self.md_dir.exists():
      archive_md = archive_date_dir / "md"
      if archive_md.exists():
        shutil.rmtree(archive_md)
      shutil.move(str(self.md_dir), str(archive_md))
      click.echo(f"  Moved md/ to archive/{last_date}/md/")

    # Update meta.json with new date and processing status
    self._save_meta({"download_date": current_date, "status": "processing"})
    click.echo(f"Starting fresh download for {current_date}")

  def load_db(self) -> List[Dict]:
    """Load the database of downloaded files."""
    if not self.db_file.exists():
      return []
    
    try:
      with open(self.db_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data if data else []
    except Exception as e:
      click.echo(f"Error loading database: {e}", err=True)
      return []
  
  def save_db(self, data: List[Dict]):
    """Save the database of downloaded files, sorted by URL for deterministic diffs."""
    try:
      # Sort data by URL to ensure deterministic output and clean git diffs
      sorted_data = sorted(data, key=lambda x: x.get('url', ''))
      with open(self.db_file, 'w', encoding='utf-8') as f:
        yaml.dump(sorted_data, f, default_flow_style=False, sort_keys=False)
    except Exception as e:
      click.echo(f"Error saving database: {e}", err=True)
  
  def url_to_file_path(self, url: str) -> Path:
    """Convert URL to file path preserving directory structure."""
    # Parse the URL to extract just the path component
    parsed_url = urlparse(url)
    
    # Remove the base URL prefix from the full URL
    if url.startswith(self.base_url):
      path = url.replace(self.base_url, "").strip("/")
    else:
      # Handle malformed URLs or different formats
      # Extract path after /claude-code/
      if "/claude-code/" in parsed_url.path:
        path = parsed_url.path.split("/claude-code/", 1)[1].strip("/")
      else:
        # Fallback: use the last part of the path
        path = parsed_url.path.strip("/").split("/")[-1] if parsed_url.path.strip("/") else "index"
    
    # If it's the root page, use "index.html"
    if not path:
      return self.html_dir / "index.html"
    
    # Clean the path to remove any invalid characters
    # Replace any remaining protocol or domain parts
    path = re.sub(r'^https?[:/]+', '', path)
    path = re.sub(r'^[^/]*docs\.anthropic\.com[^/]*', '', path)
    path = path.strip('/')
    
    if not path:
      return self.html_dir / "index.html"
    
    # Create the file path preserving directory structure
    file_path = self.html_dir / f"{path}.html"
    
    # Ensure parent directories exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    return file_path
  
  def is_url_downloaded(self, url: str, db_data: List[Dict]) -> bool:
    """Check if URL is already in database."""
    return any(item.get('url') == url for item in db_data)
  
  def download_html(self, url: str) -> Optional[str]:
    """Download HTML content from URL."""
    try:
      headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
      }

      click.echo(f"Downloading: {url}")
      response = requests.get(url, headers=headers, timeout=30)

      # Check final URL after redirects - must be docs.anthropic.com or docs.claude.com
      final_url = response.url
      parsed_final = urlparse(final_url)
      allowed_domains = ['docs.anthropic.com', 'docs.claude.com']
      if parsed_final.netloc not in allowed_domains:
        click.echo(f"WARNING: URL redirected to different domain: {final_url}", err=True)
        click.echo(f"  Original: {url}", err=True)
        click.echo(f"  Final domain: {parsed_final.netloc} (expected: {', '.join(allowed_domains)})", err=True)
        click.echo(f"  Skipping download - file will not be saved", err=True)
        return None

      # Check for HTTP errors (4xx, 5xx)
      if response.status_code >= 400:
        click.echo(f"WARNING: HTTP {response.status_code} for {url}", err=True)
        click.echo(f"  Reason: {response.reason}", err=True)
        click.echo(f"  Skipping download - file will not be saved", err=True)
        return None

      response.raise_for_status()

      # Check for soft 404 (HTTP 200 with "Page Not Found" content)
      content = response.text
      if '<title>Page Not Found</title>' in content or '<title>404' in content:
        click.echo(f"WARNING: Soft 404 detected for {url}", err=True)
        click.echo(f"  Page returns HTTP {response.status_code} but contains '404' or 'Page Not Found'", err=True)
        click.echo(f"  Final URL: {final_url}", err=True)
        click.echo(f"  Skipping download - file will not be saved", err=True)
        return None

      return content
    except Exception as e:
      click.echo(f"Error downloading {url}: {e}", err=True)
      return None
  
  def find_documentation_links(self, html_content: str, base_url: str) -> List[str]:
    """Find all documentation links in the HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()

    # Find all links that point to Claude Code documentation
    for link in soup.find_all('a', href=True):
      href = link['href']

      # Convert relative URLs to absolute
      full_url = urljoin(base_url, href)

      # Parse the URL to validate domain
      parsed = urlparse(full_url)

      # Only include docs.anthropic.com or docs.claude.com URLs
      allowed_domains = ['docs.anthropic.com', 'docs.claude.com']
      if parsed.netloc not in allowed_domains:
        continue

      # Only include Claude Code documentation URLs (both current and legacy base URLs)
      if full_url.startswith(self.base_url) or full_url.startswith(self.legacy_base_url):
        # Remove fragments and query parameters for consistency
        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if clean_url.endswith('/'):
          clean_url = clean_url[:-1]
        links.add(clean_url)

    return list(links)
  
  def rewrite_links_in_html(self, html_content: str) -> str:
    """Rewrite links in HTML to be relative."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Rewrite all links
    for link in soup.find_all('a', href=True):
      href = link['href']
      
      # If it's a Claude Code documentation link, make it relative
      if href.startswith(self.base_url):
        # Convert to relative path
        relative_path = href.replace(self.base_url, "/").rstrip('/')
        if not relative_path:
          relative_path = "/"
        link['href'] = relative_path
      elif href.startswith('https://docs.anthropic.com/en/docs/claude-code/'):
        # Handle the full URL format
        relative_path = href.replace('https://docs.anthropic.com/en/docs/claude-code/', "/").rstrip('/')
        if not relative_path:
          relative_path = "/"
        link['href'] = relative_path
    
    # Also handle any CSS or JS links if needed
    for link in soup.find_all('link', href=True):
      href = link['href']
      if href.startswith(self.base_url):
        relative_path = href.replace(self.base_url, "/").rstrip('/')
        link['href'] = relative_path
    
    for script in soup.find_all('script', src=True):
      src = script['src']
      if src.startswith(self.base_url):
        relative_path = src.replace(self.base_url, "/").rstrip('/')
        script['src'] = relative_path
    
    return str(soup)
  
  def extract_main_content(self, soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Extract the main content area from the HTML using multiple strategies."""
    
    # Strategy 1: Anthropic-specific content extraction
    # Look for the mdx-content div which contains the actual documentation
    mdx_content = soup.find('div', class_=lambda x: x and 'mdx-content' in ' '.join(x))
    if mdx_content:
      return mdx_content
    
    # Strategy 2: Look for content-area or similar containers
    content_area = soup.find('div', id='content-area')
    if content_area:
      # Find the actual content within content-area, excluding header
      header = content_area.find('header')
      if header:
        # Create a copy and remove the header
        content_copy = BeautifulSoup(str(content_area), 'html.parser')
        header_copy = content_copy.find('header')
        if header_copy:
          header_copy.decompose()
        return content_copy
      return content_area
    
    # Strategy 3: Look for prose content specifically
    prose_content = soup.find('div', class_=lambda x: x and 'prose' in ' '.join(x))
    if prose_content:
      return prose_content
    
    # Strategy 4: Look for semantic HTML5 elements
    main_content = soup.find('main')
    if main_content:
      # Remove navigation elements from main
      main_copy = BeautifulSoup(str(main_content), 'html.parser')
      for nav in main_copy.find_all(['nav', 'aside']):
        nav.decompose()
      # Remove sidebar elements
      for sidebar in main_copy.find_all('div', id=lambda x: x and 'sidebar' in x):
        sidebar.decompose()
      return main_copy.find('main')
    
    # Strategy 5: Look for article element
    article = soup.find('article')
    if article:
      return article
    
    # Strategy 6: Anthropic-specific: Look for content after removing known layout elements
    body = soup.find('body')
    if body:
      # Clone the body to avoid modifying the original
      body_copy = BeautifulSoup(str(body), 'html.parser')
      
      # Remove Anthropic-specific navigation and layout elements
      elements_to_remove = [
        'header', 'footer', 'nav', 'aside', 'script', 'style', 'noscript',
        # Anthropic-specific elements
        {'id': 'navbar'},
        {'id': 'sidebar'},
        {'id': 'sidebar-content'},
        {'class': lambda x: x and any(cls in ' '.join(x) for cls in ['nav-', 'sidebar', 'navigation'])},
        # Remove breadcrumb and other navigation
        {'class': lambda x: x and 'breadcrumb' in ' '.join(x)},
        # Remove page context menu
        {'id': 'page-context-menu'},
      ]
      
      for element_spec in elements_to_remove:
        if isinstance(element_spec, str):
          for tag in body_copy.find_all(element_spec):
            tag.decompose()
        elif isinstance(element_spec, dict):
          for tag in body_copy.find_all('div', **element_spec):
            tag.decompose()
          for tag in body_copy.find_all('nav', **element_spec):
            tag.decompose()
          for tag in body_copy.find_all('header', **element_spec):
            tag.decompose()
          for tag in body_copy.find_all('aside', **element_spec):
            tag.decompose()
      
      # Try to find the main content area after cleanup
      cleaned_content = body_copy.find('div', class_=lambda x: x and 'mdx-content' in ' '.join(x))
      if cleaned_content:
        return cleaned_content
      
      # Look for content-area after cleanup
      content_area = body_copy.find('div', id='content-area')
      if content_area:
        return content_area
      
      # Look for prose content after cleanup
      prose_content = body_copy.find('div', class_=lambda x: x and 'prose' in ' '.join(x))
      if prose_content:
        return prose_content
      
      return body_copy.find('body')
    
    return None
  
  def clean_html_content(self, content: BeautifulSoup) -> BeautifulSoup:
    """Clean HTML content to improve Markdown conversion."""
    # Create a copy to avoid modifying the original
    cleaned = BeautifulSoup(str(content), 'html.parser')
    
    # Remove problematic elements that cause bad markdown
    for element in cleaned.find_all(['script', 'style', 'noscript']):
      element.decompose()
    
    # Fix header elements that have extra content
    for header in cleaned.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
      # Remove any nested elements that might cause issues
      for nested in header.find_all(['div', 'span', 'a']):
        # Keep the text content but remove the tags
        if nested.get_text(strip=True):
          nested.replace_with(' ' + nested.get_text(strip=True) + ' ')
        else:
          nested.decompose()
      
      # Clean up any remaining artifacts and normalize spaces
      header_text = header.get_text(strip=True)
      if header_text:
        # Normalize spaces and clean up the text
        header_text = ' '.join(header_text.split())
        # Replace the header content with clean text
        header.clear()
        header.string = header_text
    
    # Clean up table elements
    for table in cleaned.find_all('table'):
      # Ensure table has proper structure
      if not table.find('thead') and table.find('tr'):
        # Convert first row to header if no thead exists
        first_row = table.find('tr')
        if first_row:
          thead = cleaned.new_tag('thead')
          first_row.extract()
          thead.append(first_row)
          table.insert(0, thead)
          
          # Convert td to th in header row
          for td in first_row.find_all('td'):
            td.name = 'th'
    
    # Remove empty paragraphs and divs
    for element in cleaned.find_all(['p', 'div']):
      if not element.get_text(strip=True) and not element.find(['img', 'video', 'audio']):
        element.decompose()
    
    # Clean up code blocks
    for code in cleaned.find_all('code'):
      # Preserve code content as-is
      code_text = code.get_text()
      code.clear()
      code.string = code_text
    
    return cleaned
  
  def scrape_documentation(self, start_url: str):
    """Scrape all documentation starting from the given URL."""
    db_data = self.load_db()
    urls_to_process = [start_url]
    processed_urls = set()
    
    while urls_to_process:
      current_url = urls_to_process.pop(0)
      
      if current_url in processed_urls:
        continue
      
      processed_urls.add(current_url)
      
      # Skip if already downloaded
      if self.is_url_downloaded(current_url, db_data):
        click.echo(f"Already downloaded: {current_url}")
        continue
      
      # Download the page
      html_content = self.download_html(current_url)
      if not html_content:
        continue
      
      # Save HTML file with directory structure
      file_path = self.url_to_file_path(current_url)
      relative_path = file_path.relative_to(self.html_dir)
      
      try:
        with open(file_path, 'w', encoding='utf-8') as f:
          f.write(html_content)
        
        # Add to database
        db_data.append({
          'url': current_url,
          'filepath': str(relative_path)
        })
        
        click.echo(f"Saved: {relative_path}")
        
        # Find more links to process
        new_links = self.find_documentation_links(html_content, current_url)
        for link in new_links:
          if link not in processed_urls and link not in urls_to_process:
            urls_to_process.append(link)
        
      except Exception as e:
        click.echo(f"Error saving {relative_path}: {e}", err=True)
    
    # Save updated database
    self.save_db(db_data)
    click.echo(f"Downloaded {len(processed_urls)} pages")
  
  def rewrite_all_links(self):
    """Rewrite all links in downloaded HTML files to be relative."""
    click.echo("Rewriting links to be relative...")
    
    # Find all HTML files
    html_files = list(self.html_dir.rglob("*.html"))
    
    if not html_files:
      click.echo("No HTML files found to rewrite.", err=True)
      return
    
    rewritten_count = 0
    
    for html_file in html_files:
      try:
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
          html_content = f.read()
        
        # Rewrite links
        updated_content = self.rewrite_links_in_html(html_content)
        
        # Save updated content
        with open(html_file, 'w', encoding='utf-8') as f:
          f.write(updated_content)
        
        relative_path = html_file.relative_to(self.html_dir)
        click.echo(f"Rewritten links in: {relative_path}")
        rewritten_count += 1
        
      except Exception as e:
        click.echo(f"Error rewriting links in {html_file.name}: {e}", err=True)
    
    click.echo(f"Rewritten links in {rewritten_count} files")
  
  def convert_html_to_markdown(self):
    """Convert all HTML files to Markdown with relative links."""
    if not self.html_dir.exists():
      click.echo("HTML directory not found. Run with --html flag first.", err=True)
      return
    
    # Load database to get original URLs
    db_data = self.load_db()
    url_mapping = {item['filepath']: item['url'] for item in db_data}
    
    # Get all HTML files recursively
    html_files = list(self.html_dir.rglob("*.html"))
    
    if not html_files:
      click.echo("No HTML files found to convert.", err=True)
      return
    
    converted_count = 0
    
    for html_file in html_files:
      try:
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
          html_content = f.read()
        
        # Parse with BeautifulSoup to clean up
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Try to extract just the main content using multiple strategies
        main_content = self.extract_main_content(soup)
        
        if main_content:
          # Clean up the main content before conversion
          cleaned_content = self.clean_html_content(main_content)
          html_content = str(cleaned_content)
        else:
          # Fallback: Remove navigation, header, footer elements
          for tag in soup(['nav', 'header', 'footer', 'aside', 'script', 'style']):
            tag.decompose()
          html_content = str(soup)
        
        # Convert to Markdown
        markdown_content = self.h2t.handle(html_content)
        
        # Clean up the markdown
        markdown_content = self.clean_markdown(markdown_content)
        
        # Get original URL for this file
        relative_html_path = html_file.relative_to(self.html_dir)
        original_url = url_mapping.get(str(relative_html_path), "Unknown URL")
        
        # Add URL header to markdown content
        url_header = f"url: {original_url}\n\n---\n\n"
        markdown_content = url_header + markdown_content
        
        # Create corresponding MD file path
        md_path = self.md_dir / relative_html_path.with_suffix('.md')
        
        # Ensure parent directories exist
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(md_path, 'w', encoding='utf-8') as f:
          f.write(markdown_content)
        
        click.echo(f"Converted: {relative_html_path} -> {md_path.relative_to(self.md_dir)}")
        converted_count += 1
        
      except Exception as e:
        click.echo(f"Error converting {html_file.name}: {e}", err=True)
    
    click.echo(f"Converted {converted_count} files to Markdown")
  
  def clean_markdown(self, markdown: str) -> str:
    """Clean up the converted markdown."""
    # Remove excessive blank lines
    markdown = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown)
    
    # Fix common issues with links
    markdown = re.sub(r'\[([^\]]*)\]\(\s*\)', r'\1', markdown)  # Remove empty links
    
    # Fix broken headers (remove extra symbols and clean up)
    markdown = re.sub(r'^#+\s*​\s*$', '', markdown, flags=re.MULTILINE)  # Remove empty headers with invisible chars
    markdown = re.sub(r'^(#+)\s*​\s*(.+)$', r'\1 \2', markdown, flags=re.MULTILINE)  # Fix headers with invisible chars
    
    # Clean up table formatting
    markdown = re.sub(r'\|\s*\|\s*\|', '| |', markdown)  # Fix empty table cells
    
    # Remove standalone invisible characters
    markdown = re.sub(r'^\s*​\s*$', '', markdown, flags=re.MULTILINE)
    
    # Clean up code blocks
    markdown = re.sub(r'```\s*\n\s*```', '', markdown)  # Remove empty code blocks
    
    # Clean up whitespace
    lines = markdown.split('\n')
    cleaned_lines = []
    
    for line in lines:
      # Strip trailing whitespace
      line = line.rstrip()
      # Skip lines that are just invisible characters or empty
      if line and not re.match(r'^\s*​\s*$', line):
        cleaned_lines.append(line)
      elif not line:  # Keep empty lines for spacing
        cleaned_lines.append(line)
    
    # Join lines and ensure single trailing newline
    result = '\n'.join(cleaned_lines).strip()
    
    # Final cleanup - remove multiple consecutive empty lines
    result = re.sub(r'\n\n\n+', '\n\n', result)
    
    return result + '\n' if result else '\n'
  
  def create_web_server(self, port: int = 8000):
    """Create a Flask web server to serve the documentation locally."""
    app = Flask(__name__)
    
    @app.route('/')
    def serve_index():
      """Serve the index page."""
      index_path = self.html_dir / "index.html"
      if index_path.exists():
        return send_from_directory(self.html_dir, "index.html")
      else:
        abort(404)
    
    @app.route('/<path:path>')
    def serve_page(path):
      """Serve documentation pages."""
      # Try to serve the HTML file
      html_path = self.html_dir / f"{path}.html"
      
      if html_path.exists():
        # Calculate relative path from html_dir
        try:
          relative_path = html_path.relative_to(self.html_dir)
          directory = str(relative_path.parent) if relative_path.parent != Path('.') else '.'
          filename = relative_path.name
          
          if directory == '.':
            return send_from_directory(self.html_dir, filename)
          else:
            return send_from_directory(self.html_dir / directory, filename)
        except Exception:
          abort(404)
      
      # If path ends with /, try to serve index.html from that directory
      if path.endswith('/'):
        index_path = self.html_dir / path / "index.html"
        if index_path.exists():
          return send_from_directory(index_path.parent, "index.html")
      
      # Try adding trailing slash and redirect
      if not path.endswith('/'):
        redirect_path = self.html_dir / path / "index.html"
        if redirect_path.exists():
          return redirect(f"/{path}/")
      
      abort(404)
    
    @app.errorhandler(404)
    def not_found(error):
      return f"<h1>404 Not Found</h1><p>The page you're looking for doesn't exist.</p>", 404
    
    click.echo(f"Starting web server on http://localhost:{port}")
    click.echo("Press Ctrl+C to stop the server")
    
    try:
      app.run(host='0.0.0.0', port=port, debug=False)
    except KeyboardInterrupt:
      click.echo("\nServer stopped.")


@click.command()
@click.option('--html', is_flag=True, help='Download HTML documentation')
@click.option('--md', is_flag=True, help='Convert HTML files to Markdown')
@click.option('--serve', is_flag=True, help='Start local web server to serve the documentation')
@click.option('--port', default=8000, help='Port for the web server (default: 8000)')
@click.option('--url', default='https://docs.anthropic.com/en/docs/claude-code/', 
              help='Starting URL for scraping (default: Claude Code docs)')
def main(html: bool, md: bool, serve: bool, port: int, url: str):
  """Claude Code Documentation Scraper, Converter, and Local Server."""
  
  if not html and not md and not serve:
    click.echo("Please specify at least one of --html, --md, or --serve flags")
    sys.exit(1)
  
  base_dir = Path.cwd()
  scraper = DocumentationScraper(base_dir)
  
  if html:
    click.echo("Starting HTML download...")
    scraper.scrape_documentation(url)
    click.echo("HTML download completed!")

    click.echo("Rewriting links to be relative...")
    scraper.rewrite_all_links()
    click.echo("Link rewriting completed!")

  if md:
    click.echo("Starting Markdown conversion...")
    scraper.convert_html_to_markdown()
    click.echo("Markdown conversion completed!")

  # Mark as completed only if both HTML and MD were processed in this run
  if html and md:
    scraper._mark_completed()

  if serve:
    if not (scraper.html_dir / "index.html").exists():
      click.echo("No HTML files found. Please run with --html flag first.", err=True)
      sys.exit(1)
    
    scraper.create_web_server(port)


if __name__ == "__main__":
  main()