#!/usr/bin/env python3
import re, os

FILES_DIR = "."

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Fixed: {path}")

def remove_trailing_slash_hrefs(html):
    return re.sub(r'href="(/[a-zA-Z0-9][a-zA-Z0-9\-]*?)/"', r'href="\1"', html)

def remove_trailing_slash_og_url(html):
    return re.sub(
        r'(property="og:url"\s+content="https://calcpercentage\.vercel\.app/[a-zA-Z0-9][a-zA-Z0-9\-]*?)/"',
        r'\1"', html
    )

def remove_trailing_slash_schema(html):
    html = re.sub(
        r'("item":\s*"https://calcpercentage\.vercel\.app/[a-zA-Z0-9][a-zA-Z0-9\-]*?)/"',
        r'\1"', html
    )
    html = re.sub(
        r'("url":\s*"https://calcpercentage\.vercel\.app/[a-zA-Z0-9][a-zA-Z0-9\-]*?)/"',
        r'\1"', html
    )
    return html

def fix_homepage_australia(html):
    html = html.replace(
        "<title>Percentage Calculator — Calculate Any Percentage Instantly</title>",
        "<title>Percentage Calculator — Free Online % Calculator | Australia</title>"
    )
    html = re.sub(
        r'<meta name="description" content="Free online percentage calculator\. Instantly calculate percentages.*?">',
        '<meta name="description" content="Free online percentage calculator for Australians. Instantly calculate percentages, percentage increase, decrease, discount &amp; more. Fast, accurate, no ads.">',
        html, flags=re.DOTALL
    )
    html = html.replace(
        '<meta property="og:title" content="Percentage Calculator — Calculate Any Percentage Instantly">',
        '<meta property="og:title" content="Percentage Calculator — Free Online % Calculator | Australia">'
    )
    return html

def fix_what_percentage_of(html):
    html = html.replace(
        'rel="canonical" href="https://calcpercentage.vercel.app/what-is-percentage/"',
        'rel="canonical" href="https://calcpercentage.vercel.app/what-percentage-of"'
    )
    html = html.replace(
        'rel="canonical" href="https://calcpercentage.vercel.app/what-is-percentage"',
        'rel="canonical" href="https://calcpercentage.vercel.app/what-percentage-of"'
    )
    html = re.sub(
        r'property="og:url"\s+content="https://calcpercentage\.vercel\.app/what-is-percentage/?"',
        'property="og:url" content="https://calcpercentage.vercel.app/what-percentage-of"',
        html
    )
    return html

HTML_FILES = [
    "index.htm", "about.html", "contact.html", "discount-calculator.html",
    "fraction-to-percentage.html", "how-to-calculate-percentage.html",
    "money-percentage-calculator.html", "percent-error-calculator.html",
    "percent-off-calculator.html", "percentage-change-calculator.html",
    "percentage-decrease-calculator.html", "percentage-difference-calculator.html",
    "percentage-formula.html", "percentage-increase-calculator.html",
    "percentage-of-number.html", "privacy-policy.html",
    "sales-percentage-calculator.html", "what-percentage-of.html",
]

print("Starting SEO fixes...\n")

for filename in HTML_FILES:
    filepath = os.path.join(FILES_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  Skipped (not found): {filename}")
        continue
    html = read(filepath)
    original = html
    html = remove_trailing_slash_hrefs(html)
    html = remove_trailing_slash_og_url(html)
    html = remove_trailing_slash_schema(html)
    if filename == "index.htm":
        html = fix_homepage_australia(html)
    if filename == "what-percentage-of.html":
        html = fix_what_percentage_of(html)
    if html != original:
        write(filepath, html)
    else:
        print(f"  No changes needed: {filename}")

# Create what-is-percentage.html
with open("what-is-percentage.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>What is a Percentage? Definition, Formula & Examples</title>
  <meta name="description" content="What is a percentage? Learn the definition, formula, and real-world examples. Free guide for students and everyday use.">
  <link rel="canonical" href="https://calcpercentage.vercel.app/what-is-percentage">
  <meta property="og:url" content="https://calcpercentage.vercel.app/what-is-percentage">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url=/what-percentage-of">
  <script>window.location.replace('/what-percentage-of');</script>
</head>
<body><p>Redirecting... <a href="/what-percentage-of">Click here</a></p></body>
</html>""")
print("  Created: what-is-percentage.html")

print("\nAll fixes done!")
