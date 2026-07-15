import random
from pathlib import Path
from xml.sax.saxutils import escape

QUOTES = Path("data/quotes.txt")
STATE = Path("data/.quote_state")
SVG = Path("assets/repository-thought.svg")

quotes = [
    q.strip()
    for q in QUOTES.read_text(encoding="utf-8").split("\n\n")
    if q.strip()
]

if STATE.exists():
    order = STATE.read_text(encoding="utf-8").splitlines()
else:
    order = []

if not order:
    order = list(map(str, range(len(quotes))))
    random.shuffle(order)

index = int(order.pop(0))
quote = quotes[index]

STATE.write_text("\n".join(order), encoding="utf-8")

quote = escape(quote)

svg = f"""<svg width="850" height="120" xmlns="http://www.w3.org/2000/svg">

<style>

.background{{fill:#0d1117;}}

.title{{
fill:#C8A03D;
font:600 16px Arial,sans-serif;
}}

.quote{{
fill:white;
font:600 22px Arial,sans-serif;
}}

.footer{{
fill:#8b949e;
font:500 12px Arial,sans-serif;
}}

</style>

<rect class="background" width="850" height="120" rx="14"/>

<rect
x="25"
y="25"
width="5"
height="70"
fill="#C8A03D"
/>

<text
x="45"
y="42"
class="title">

💭 Repository Thought

</text>

<text
x="45"
y="78"
class="quote">

{quote}

</text>

<text
x="45"
y="102"
class="footer">

Updates automatically every day

</text>

</svg>
"""

SVG.write_text(svg, encoding="utf-8")
