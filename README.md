# Static Site Generator

A lightweight static site generator written in Python that converts Markdown files into a complete HTML website. Supports custom templates, recursive content directories, static asset copying, and configurable base paths for deployment.

## Features

- **Markdown to HTML** — Converts Markdown content with full inline formatting support (bold, italic, code, links, images)
- **Block-level parsing** — Handles headings, paragraphs, code blocks, blockquotes, ordered/unordered lists
- **Template system** — Simple `{{ Title }}` and `{{ Content }}` placeholder replacement
- **Recursive content generation** — Processes nested directories of Markdown files automatically
- **Static asset copying** — Copies CSS, images, JS, and other static files to output
- **Configurable base path** — Deploy to subdirectories (e.g., `/blog/`) or root (`/`)
- **Zero dependencies** — Pure Python standard library

## Project Structure

```
static-site-generator/
├── content/              # Markdown source files
│   ├── index.md          # Homepage
│   ├── blog/             # Blog posts
│   └── contact/          # Contact page
├── static/               # Static assets (CSS, JS, images)
│   └── index.css
├── template.html         # HTML template with {{ Title }} and {{ Content }}
├── src/                  # Source code
│   ├── main.py           # Entry point
│   ├── copystatic.py     # Static file copying
│   ├── gencontent.py     # Markdown → HTML generation
│   ├── markdown_blocks.py # Block-level Markdown parsing
│   ├── htmlnode.py       # HTML node representation
│   ├── textnode.py       # Text node representation
│   └── utils/            # Inline Markdown parsing utilities
├── docs/                 # Generated output (gitignored)
├── build.sh              # Build script
├── main.sh               # Build + serve script
└── test.sh               # Test runner
```

## Quick Start

### Prerequisites
- Python 3.8+

### Build the site

```bash
./build.sh
# or
python3 -m src.main
```

Output is generated to `docs/` (configured in `src/main.py`).

### Build with custom base path (for subdirectory deployment)

```bash
python3 -m src.main /my-blog/
```

### Serve locally

```bash
./main.sh
# or
cd docs && python3 -m http.server 8888
```

Then visit `http://localhost:8888`

## Content Authoring

Create `.md` files in `content/`. Each file must start with an H1 heading (`# Title`) which becomes the page title.

**Example `content/blog/my-post.md`:**
```markdown
# My Blog Post

This is a paragraph with **bold**, _italic_, and `inline code`.

## Subheading

- List item 1
- List item 2

```python
def hello():
    print("Code blocks work too!")
```

![Alt text](/images/photo.jpg)
[Link text](/blog/another-post)
```

## Template Customization

Edit `template.html` to change the site layout. Available placeholders:

| Placeholder | Description |
|-------------|-------------|
| `{{ Title }}` | Page title (from first `# Heading`) |
| `{{ Content }}` | Rendered HTML content |

The template also supports automatic base path rewriting for `href="/..."` and `src="/..."` attributes.

## Running Tests

```bash
./test.sh
# or
python3 -m unittest discover -s src -p "test_*.py"
```

Test modules:
- `test_htmlnode.py` — HTML node rendering
- `test_textnode.py` — Text node conversions
- `test_utils.py` — Inline Markdown parsing (images, links, delimiters)
- `test_markdown_blocks.py` — Block-level Markdown parsing

## Configuration

Key paths in `src/main.py`:

```python
dir_path_static = "./static"      # Static assets source
dir_path_public = "./docs"        # Output directory
dir_path_content = "./content"    # Markdown source
template_path = "./template.html" # Template file
default_basepath = "/"            # Default deployment base path
```

## How It Works

1. **Clean output** — Deletes `docs/` directory
2. **Copy static** — Recursively copies `static/` → `docs/`
3. **Process content** — Walks `content/` recursively:
   - Reads each `.md` file
   - Extracts title from first `# Heading`
   - Parses Markdown blocks (headings, paragraphs, lists, code, quotes)
   - Parses inline Markdown (bold, italic, code, links, images)
   - Generates HTML nodes
   - Applies template with title and content
   - Rewrites absolute paths using `basepath`
   - Writes `.html` file to `docs/` preserving directory structure

## License

MIT