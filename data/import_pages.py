import json
import gzip
from slugify import slugify
from datetime import datetime
from collections import defaultdict
import click


def site_info():
    return """
  <siteinfo>
   <sitename>BMEGWiki</sitename>
    <dbname>wikidb</dbname>
    <base>https://gen3.compbio.ohsu.edu/wiki/Main_Page</base>
    <generator>MediaWiki 1.34.0</generator>
    <case>first-letter</case>
    <namespaces>
      <namespace key="-2" case="first-letter">Media</namespace>
      <namespace key="-1" case="first-letter">Special</namespace>
      <namespace key="0" case="first-letter" />
      <namespace key="1" case="first-letter">Talk</namespace>
      <namespace key="2" case="first-letter">User</namespace>
      <namespace key="3" case="first-letter">User talk</namespace>
      <namespace key="4" case="first-letter">BMEGWiki</namespace>
      <namespace key="5" case="first-letter">BMEGWiki talk</namespace>
      <namespace key="6" case="first-letter">File</namespace>
      <namespace key="7" case="first-letter">File talk</namespace>
      <namespace key="8" case="first-letter">MediaWiki</namespace>
      <namespace key="9" case="first-letter">MediaWiki talk</namespace>
      <namespace key="10" case="first-letter">Template</namespace>
      <namespace key="11" case="first-letter">Template talk</namespace>
      <namespace key="12" case="first-letter">Help</namespace>
      <namespace key="13" case="first-letter">Help talk</namespace>
      <namespace key="14" case="first-letter">Category</namespace>
      <namespace key="15" case="first-letter">Category talk</namespace>
      <namespace key="102" case="first-letter">Property</namespace>
      <namespace key="103" case="first-letter">Property talk</namespace>
      <namespace key="108" case="first-letter">Concept</namespace>
      <namespace key="109" case="first-letter">Concept talk</namespace>
      <namespace key="112" case="first-letter">smw/schema</namespace>
      <namespace key="113" case="first-letter">smw/schema talk</namespace>
      <namespace key="114" case="first-letter">Rule</namespace>
      <namespace key="115" case="first-letter">Rule talk</namespace>
      <namespace key="2300" case="first-letter">Gadget</namespace>
      <namespace key="2301" case="first-letter">Gadget talk</namespace>
      <namespace key="2302" case="case-sensitive">Gadget definition</namespace>
      <namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
    </namespaces>
  </siteinfo>
    """


@click.command()
@click.option('--output', default='data/imports/pages', help='directory path for XML output files.')
@click.option('--input',  help='gz input file.')
@click.option('--batch_size', default=100, help='Number of compounds per batch')
def transform(input, output, batch_size):
    print(input, output, batch_size)
    c = 0
    batch = 0
    with gzip.open(input, 'r') as in_fh:
        for line in in_fh:
            line = json.loads(line)
            if c == 0:
                path = f"{output}-{batch}.xml"
                out_fh = open(path, 'w')
                out_fh.write(f'<mediawiki xml:lang="en">\n{site_info()}\n')
            text = line['text']
            title = line['title']
            revision = f"<revision><timestamp>{datetime.now().isoformat()}</timestamp> <contributor><username>ImportBot</username></contributor><text><![CDATA[{text}]]></text> <minor /> </revision>"
            page = f"  <page><title>{title}</title>{revision}</page>\n"
            out_fh.write(page)
            c += 1
            if c == batch_size:
                c = 0
                batch += 1
                out_fh.write('</mediawiki>')
        out_fh.write('</mediawiki>')
        out_fh.close()


"""
  <page>
    <title>TEST</title>
    <ns>0</ns>
    <id>19</id>
    <revision>
      <id>19</id>
      <timestamp>2020-03-12T00:26:53Z</timestamp>
      <contributor>
        <username>Walsbr</username>
        <id>2</id>
      </contributor>
      <comment>Created page with "This is a TEST"</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve" bytes="14">This is a TEST</text>
      <sha1>o6c8ersv5g56hg72qdyv1skazc7psly</sha1>
    </revision>
  </page>
  """


if __name__ == '__main__':
    transform()
