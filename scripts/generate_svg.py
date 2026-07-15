import random
from pathlib import Path
from xml.sax.saxutils import escape

QUOTES = Path("data/quotes.txt")
SVG = Path("assets/repository-thought.svg")
STATE = Path("data/.quote_state")

# Read quotes
quotes = [
    q.strip()
    for q in QUOTES.read_text(encoding="utf-8").split("\n\n")
    if q.strip()
]

# Create a shuffled order that cycles through every quote once
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

svg = f"""<svg width="850" height="110" xmlns="http://www.w3.org/2000/svg">

<style>
.title {{
    font: 600 16px Inter, Arial, sans-serif;
    fill: #C8A03D;
}}

.quote {{
    font: 500 22px Inter, Arial, sans-serif;
    fill: #ffffff;
}}
</style>

<rect width="850" height="110" rx="12" fill="#0d1117"/>

<text x="35" y="35" class="title">
💭 Today's Repository Thought
</text>

<text x="35" y="75" class="quote">
{quote}
</text>

</svg>
"""

SVG.write_text(svg, encoding="utf-8")
