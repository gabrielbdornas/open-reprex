# Another alternative https://www.pdfforge.org/online/en/markdown-to-pdf

from markdown_pdf import MarkdownPdf, Section
from pathlib import Path

markdown_content = Path('gabriel_game.md').read_text()
pdf = MarkdownPdf(toc_level=2)
pdf.add_section(Section(markdown_content, toc=True),
                user_css="body {text-align:justify;}")
pdf.save("gabriel_game.pdf")
