#!/usr/bin/env python3
import re, os, json

FILES_DIR = "."
EM = "\u2014"

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Fixed: {path}")

FIXES = {
    "percentage-increase-calculator.html": {
        "title_old": f"Percentage Increase Calculator {EM} Calculate % Increase Instantly",
        "title_new": f"Percentage Increase Calculator {EM} Free Online Tool | Australia",
        "desc_old":  "Free percentage increase calculator. Instantly find the percentage increase between two numbers. See the formula, step-by-step examples, and use cases for salary, price &amp; more.",
        "desc_new":  "Free percentage increase calculator for Australians. Find salary increases, price rises &amp; more instantly. Includes formula, step-by-step working &amp; examples.",
        "ogt_old":   f"Percentage Increase Calculator {EM} Calculate % Increase Instantly",
        "ogt_new":   f"Percentage Increase Calculator {EM} Free Online Tool | Australia",
    },
    "percentage-decrease-calculator.html": {
        "title_old": f"Percentage Decrease Calculator {EM} Calculate % Decrease Instantly",
        "title_new": f"Percentage Decrease Calculator {EM} Free Online Tool | Australia",
        "desc_old":  "Free percentage decrease calculator. Instantly find the percentage decrease between two numbers. Includes formula, step-by-step working, reverse calculator &amp; real-world examples.",
        "desc_new":  "Free percentage decrease calculator for Australians. Find price drops, salary cuts &amp; more instantly. Includes formula, step-by-step working &amp; real examples.",
        "ogt_old":   f"Percentage Decrease Calculator {EM} Calculate % Decrease Instantly",
        "ogt_new":   f"Percentage Decrease Calculator {EM} Free Online Tool | Australia",
    },
    "discount-calculator.html": {
        "title_old": f"Discount Calculator {EM} Find Sale Price &amp; Savings Instantly",
        "title_new": f"Discount &amp; GST Calculator Australia {EM} Sale Price &amp; Savings",
        "desc_old":  "Free discount calculator. Find the sale price, amount saved, original price before discount, or what discount % was applied. Supports double discounts, bulk tables, and all currencies. Full step-by-step working.",
        "desc_new":  "Free discount &amp; GST calculator for Australia. Find sale price, amount saved, GST-inclusive prices &amp; more. Supports AUD, step-by-step working &amp; bulk tables.",
        "ogt_old":   f"Discount Calculator {EM} Find Sale Price &amp; Savings Instantly",
        "ogt_new":   f"Discount &amp; GST Calculator Australia {EM} Sale Price &amp; Savings",
    },
    "how-to-calculate-percentage.html": {
        "title_old": f"How to Calculate Percentage {EM} Step-by-Step Guide with Examples",
        "title_new": f"How to Calculate Percentage {EM} Step-by-Step Guide | Australia",
        "desc_old":  "Learn how to calculate percentage step by step. Covers all 3 percentage formulas, percentage increase, decrease, change, reverse percentage, mental math shortcuts, and real-world examples.",
        "desc_new":  "Learn how to calculate percentage step by step for Australian students, shoppers &amp; professionals. Covers all formulas, GST, discounts, salary &amp; real-world examples.",
        "ogt_old":   f"How to Calculate Percentage {EM} Step-by-Step Guide with Examples",
        "ogt_new":   f"How to Calculate Percentage {EM} Step-by-Step Guide | Australia",
    },
    "percent-off-calculator.html": {
        "title_old": f"Percent Off Calculator {EM} Calculate Discount Price Instantly",
        "title_new": f"Percent Off Calculator {EM} Sale Price &amp; Discounts | Australia",
        "desc_old":  "Free percent off calculator. Find the discounted price, amount saved, and final price after any percentage discount. Includes reverse calculator, bulk discounts, and real shopping examples.",
        "desc_new":  "Free percent off calculator for Australian shoppers. Find discounted prices, savings &amp; sale prices instantly. Great for retail, Boxing Day sales &amp; everyday shopping.",
        "ogt_old":   f"Percent Off Calculator {EM} Calculate Discount Price Instantly",
        "ogt_new":   f"Percent Off Calculator {EM} Sale Price &amp; Discounts | Australia",
    },
    "money-percentage-calculator.html": {
        "title_old": f"Money Percentage Calculator {EM} Calculate Percentages of Dollar Amounts",
        "title_new": f"Money Percentage Calculator {EM} AUD &amp; Dollar Amounts | Australia",
        "desc_old":  "Free money percentage calculator. Find percentages of dollar amounts — tip calculator, sales tax, discount, salary raise, percentage of a money amount, and more. Instant results with step-by-step working.",
        "desc_new":  "Free money percentage calculator for Australians. Calculate percentages of AUD amounts — GST, tips, salary raises, discounts &amp; more. Instant results with step-by-step working.",
        "ogt_old":   f"Money Percentage Calculator {EM} Calculate Percentages of Dollar Amounts",
        "ogt_new":   f"Money Percentage Calculator {EM} AUD &amp; Dollar Amounts | Australia",
    },
    "percentage-formula.html": {
        "title_old": f"Percentage Formula {EM} All Percentage Formulas Explained with Examples",
        "title_new": f"Percentage Formula {EM} All Formulas Explained with Examples | Australia",
        "desc_old":  "All percentage formulas in one place — find the part, find the percentage, find the whole, percentage increase, decrease, change, difference, error, reverse percentage, and compound interest. Each formula with step-by-step examples.",
        "desc_new":  "All percentage formulas for Australian students &amp; professionals — find the part, whole, percentage increase, GST, discount, reverse percentage &amp; more. Step-by-step examples.",
        "ogt_old":   f"Percentage Formula {EM} All Percentage Formulas Explained with Examples",
        "ogt_new":   f"Percentage Formula {EM} All Formulas Explained with Examples | Australia",
    },
}

print("\nStarting Australia SEO fixes...\n")

for filename, fix in FIXES.items():
    filepath = os.path.join(FILES_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  NOT FOUND: {filename}")
        continue
    html = read(filepath)
    original = html
    html = html.replace(f"<title>{fix['title_old']}</title>", f"<title>{fix['title_new']}</title>")
    html = html.replace(f'<meta name="description" content="{fix["desc_old"]}">', f'<meta name="description" content="{fix["desc_new"]}">')
    html = html.replace(f'<meta property="og:title" content="{fix["ogt_old"]}">', f'<meta property="og:title" content="{fix["ogt_new"]}">')
    if html != original:
        write(filepath, html)
    else:
        print(f"  No changes: {filename}")

# Fix vercel.json
print("\nFixing vercel.json...\n")
vercel_path = os.path.join(FILES_DIR, "vercel.json")
with open(vercel_path) as f:
    vercel = json.load(f)

missing = [
    "contact","discount-calculator","fraction-to-percentage",
    "how-to-calculate-percentage","money-percentage-calculator",
    "percentage-formula","privacy-policy","what-percentage-of",
    "what-is-percentage","sales-percentage-calculator","percentage-of-number"
]

existing = {r["source"] for r in vercel.get("redirects", [])}
added = 0
for page in missing:
    src = f"/{page}/"
    if src not in existing:
        vercel["redirects"].append({"source": src, "destination": f"/{page}", "permanent": True})
        existing.add(src)
        print(f"  Added: {src}")
        added += 1

if added:
    with open(vercel_path, "w") as f:
        json.dump(vercel, f, indent=2)
    print(f"\n  vercel.json — {added} redirects added")

print("\nAll done!")
