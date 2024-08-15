import re

text = """A typical wiki contains multiple pages for the subject's or
scope of the project's, and could be either open to the public or limited
to use within an organization for maintaining its internal knowledge base.

Wikis are enabled by wiki software, otherwise known as wiki engines. A
wiki engine, being a form of a content management system, differs from
other web-based systems such as blog software or static site generators,
in that the content is created without any defined owner or leader, and
wikis have little inherent structure, allowing structure to emerge according
to the needs of the users.[1] Wiki engines usually allow content to be written
using a simplified markup language and sometimes edited with the help of a
rich-text editor."""
tokens = re.findall("[\w]+", text)
print(tokens)
