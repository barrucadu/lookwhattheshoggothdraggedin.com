import markdown
import re
import xml.etree.ElementTree as ET

GLOSSARY = {}


# #############################################################################
# Inline Processors


class GlossaryLinkProcessor(markdown.inlinepatterns.InlineProcessor):
    """Glossary Links.

    Syntax:

        [glo:key]         - show name/acronym & link to entry
        [glos:key]        - show name/acronym (pluralised) & link to entry
        [glo:key "title"] - show title & link to entry

    The optional title can include other inline markdown.  For example:

        [glo:dice-notation "`1d12 + 1d8`"]
    """

    def handleMatch(self, m, data):
        is_plural = m.group(1) == "s"
        key = m.group(2)
        override_title = m.group(4)
        item = GLOSSARY[key]

        el = ET.Element("a")
        el.set("class", "link--glossary")
        el.set("href", f"glossary.html#{key}")

        title = item.get("title_plural", item["title"] + "s") if is_plural else item["title"]

        if "abbr" in item and item.get("use_abbr_for_glo_link", True) and override_title is None:
            abbr = ET.Element("abbr")
            abbr.set("title", title)
            abbr.text = item.get("abbr_plural", item["abbr"] + "s") if is_plural else item["abbr"]
            el.append(abbr)
        else:
            el.text = override_title or title

        return el, m.start(0), m.end(0)


class GlossaryLinkExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(
            GlossaryLinkProcessor(r"\[glo(s)?:([a-z-]+)(\s*\"([^\"]+)\")?\]", md),
            "glossary",
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


def setup(glossary):
    global GLOSSARY
    GLOSSARY = glossary

    return [GlossaryLinkExtension, ProbabilityTableExtension, RollTableExtension]
