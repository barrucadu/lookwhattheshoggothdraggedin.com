import markdown
import re
import xml.etree.ElementTree as ET

# #############################################################################
# Inline Processors

ABBREVIATIONS = {
    "adnd": { "display": "AD&D", "title": "Advanced Dungeons & Dragons" },
    "bxdnd": { "display": "B/X D&D", "title": "Basic / Expert Dungeons & Dragons" },
    "dnd": { "display": "D&D", "title": "Dungeons & Dragons" },
    "gm": { "display": "GM", "title": "Game Master" },
    "npc": { "display": "NPC", "title": "Non-player Character" },
    "ose": { "display": "OSE", "title": "Old School Essentials" },
    "osr": { "display": "OSR", "title": "Old School Renaissance" },
    "osric": { "display": "OSRIC", "title": "Old School Reference and Index Compilation" },
    "pc": { "display": "PC", "title": "Player Character" },
    "vtt": { "display": "VTT", "title": "Virtual Tabletop" },
}

class AbbreviationProcessor(markdown.inlinepatterns.InlineProcessor):
    """Abbreviations.

    Syntax:

        [abbr:key]         - show name
        [abbr:key "title"] - show title

    The optional title can include other inline markdown.
    """

    def handleMatch(self, m, data):
        key = m.group(1)
        override_title = m.group(3)
        item = ABBREVIATIONS[key]

        el = ET.Element("abbr")
        el.set("title", item["title"])
        el.text = override_title or item["display"]

        return el, m.start(0), m.end(0)


class AbbreviationExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(
            AbbreviationProcessor(r"\[abbr?:([a-z-]+)(\s*\"([^\"]+)\")?\]", md),
            "abbreviation",
            -99999,
        )


# #############################################################################
# Block Processors


def subElement(parent, ty, text=None, **attrs):
    el = ET.SubElement(parent, ty)
    if text:
        el.text = text
    for k, v in attrs.items():
        el.set(k.removesuffix("_"), v)
    return el


class ProbabilityTableProcessor(markdown.blockprocessors.BlockProcessor):
    """Probability Tables.

    Syntax:

        !!!probability-table
        <value>,<prob1>[,<prob2>...]

    Each row should have the same number of probabilities.
    Probabilities are printed to two decimal places.  Rendered next to
    each column of probabilities is a column of bars, which are scaled
    to take up the available space well (for example, if the largest
    probability in the table is 9%, then all bars will have their size
    multiplied by 11).
    """

    RE_START = r"!!!probability-table\n"

    def test(self, parent, block):
        return re.match(self.RE_START, block)

    def run(self, parent, blocks):
        entries = [
            [entry.strip() for entry in line.strip().split(",")]
            for line in re.sub(self.RE_START, "", blocks[0]).splitlines()
            if line.strip()
        ]

        scale = 100
        for entry in entries:
            _, *entryPs = entry
            for p in entryPs:
                fp = float(p)
                while fp * scale > 100:
                    scale -= 1

        table = subElement(parent, "table", class_="probability-table")

        thead = subElement(table, "thead")
        theadTr = subElement(thead, "tr")
        subElement(theadTr, "th", text="#", class_="num")
        for i in range(len(entries[0]) - 1):
            subElement(theadTr, "th", text="%", class_="num")
            subElement(theadTr, "th")

        tbody = subElement(table, "tbody")
        for entry in entries:
            entryN, *entryPs = entry
            tr = subElement(tbody, "tr")
            subElement(tr, "th", text=entryN, class_="num")
            for p in entryPs:
                subElement(tr, "td", text=f"{float(p):.2f}%", class_="num")
                td = subElement(tr, "td")
                subElement(
                    td, "div", text="&nbsp;", class_="bar", style=f"width:calc({scale}*{p}%)"
                )

        blocks.pop(0)


class ProbabilityTableExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            ProbabilityTableProcessor(md.parser),
            "probability-table",
            175,
        )


class RollTableProcessor(markdown.blockprocessors.BlockProcessor):
    """Roll Tables.

    Syntax:

        !!!roll-table
         <value>,<description>

    The description must be a single line of text.  It can include
    inline markdown.  For example:

        !!!roll-table
        1,**Purple Spiral Tea.**  Fatally toxic.
    """

    RE_START = r"!!!roll-table\n"

    def test(self, parent, block):
        return re.match(self.RE_START, block)

    def run(self, parent, blocks):
        title, *rows = [
            line.strip()
            for line in re.sub(self.RE_START, "", blocks[0]).splitlines()
            if line.strip()
        ]
        entries = [[entry.strip() for entry in row.split(",", 1)] for row in rows]

        table = subElement(parent, "table", class_="roll-table")

        thead = subElement(table, "thead")
        theadTr = subElement(thead, "tr")
        subElement(theadTr, "th", text="#", class_="num")
        subElement(theadTr, "th", text=title)

        tbody = subElement(table, "tbody")
        for entry in entries:
            entryN, entryT = entry
            tr = subElement(tbody, "tr")
            subElement(tr, "th", text=entryN, class_="num")
            subElement(tr, "td", text=entryT)

        blocks.pop(0)


class RollTableExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            RollTableProcessor(md.parser),
            "roll-table",
            175,
        )


# #############################################################################


def setup():
    return [AbbreviationExtension, ProbabilityTableExtension, RollTableExtension]
