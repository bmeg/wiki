from datetime import datetime
import click
import hashlib


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


def sha1(text):
    return hashlib.sha1(str.encode(text)).hexdigest()

def page(title, text, ns=0):
    return f"""
    <page>
        <title>{title}</title>
        <revision><timestamp>{datetime.utcnow().isoformat()}</timestamp><contributor><username>ImportBot</username></contributor><minor />
            <text><![CDATA[{text}]]></text>
        </revision>
    </page>
    """
    # xml:space="preserve" bytes="{len(text)}"
    # <sha1>{sha1(text)}</sha1>


main_page = page('Main_Page', """
<strong>Welcome to [https://bmeg.io BMEG]</strong>

{{#categorytree:BMEG}}

== Getting started ==
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Configuration_settings Configuration settings list]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:FAQ MediaWiki FAQ]
* [https://lists.wikimedia.org/mailman/listinfo/mediawiki-announce MediaWiki release mailing list]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Localisation#Translation_resources Localise MediaWiki for your language]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Combating_spam Learn how to combat spam on your wiki]
""")

category_BMEG = page('Category:BMEG', 'Root category for BMEG concepts.')
category_Ontology = page('Category:Ontology', '[[Category:BMEG]] Root Ontology.')
category_Synonym = page('Category:Synonym', '[[Category:BMEG]] Root Synonym.')

category_Compound = page('Category:Compound', '[[Category:BMEG]] Root Compound.')
category_CompoundSynonym = page('Category:CompoundSynonym', '[[Category:Synonym]]')

category_Phenotype = page('Category:Phenotype', '[[Category:BMEG]] Root Phenotype.')
category_PhenotypeSynonym = page('Category:PhenotypeSynonym', '[[Category:Synonym]]')

property_Term = page('Property:Term', '[[Has type::Text]]')
property_GID = page('Property:GID', '[[Has type::Text]]')
property_TermId = page('Property:TermId', '[[Has type::URL]]')
property_Ontology = page('Property:Ontology', '[[Has type::Page]]')
property_SelectedOntology = page('Property:SelectedOntology', '[[Has type::Page]]')

property_CompoundSynonym = page('Property:CompoundSynonym', '[[Has type::Page]]')
property_Compound = page('Property:Compound', '[[Has type::Page]]')

property_PhenotypeSynonym = page('Property:PhenotypeSynonym', '[[Has type::Page]]')
property_Phenotype = page('Property:Phenotype', '[[Has type::Page]]')

category_PUBCHEM = page('Category:PUBCHEM', '[[Category:Ontology]]')
category_CHEBI = page('Category:CHEBI', '[[Category:Ontology]]')
category_DRUGBANK = page('Category:DRUGBANK', '[[Category:Ontology]]')
category_INCHI = page('Category:INCHI', '[[Category:Ontology]]')
category_NO_ONTOLOGY= page('Category:NO_ONTOLOGY', '[[Category:Ontology]]')
category_CHEMBL= page('Category:CHEMBL', '[[Category:Ontology]]')

category_MONDO= page('Category:MONDO', '[[Category:Ontology]]')
category_OMIA= page('Category:OMIA', '[[Category:Ontology]]')

compound_Aspirin = page('Aspirin', '[[Category:Compound]]\n*  term [[Term::aspirin]]\n*  ontology [[Ontology::PUBCHEM-CID2244]]\n*  synonym: [[CompoundSynonym::ACETYLSALICYLIC-ACID]]')
ontology_CID2244 = page('PUBCHEM-CID2244', '[[Category:PUBCHEM]]\n*  term [[Term::aspirin]]\n*  [[Compound::Aspirin]]')
synonym_ACETYLSALICYLIC_ACID = page('ACETYLSALICYLIC-ACID', '[[Category:CompoundSynonym]] [[Term::ACETYLSALICYLIC ACID]] [[Compound::Aspirin]]')


phenotype_Cold = page('Cold', '[[Category:Phenotype]]\n*  term [[Term::aspirin]]\n*  ontology [[Ontology::PUBCHEM-CID2244]]\n*  synonym: [[PhenotypeSynonym::sniffles]]')
synonym_Sniffles = page('Sniffles', '[[Category:PhenotypeSynonym]] [[Term::sniffles]] [[Phenotype::Cold]]')
ontology_MONDO_0005709 = page('MONDO_0005709', '[[Category:MONDO]]\n*  term [[Term::common cold]]\n* termId [[TermId::http://purl.obolibrary.org/obo/MONDO_0005709]]\n*  phenotype[[Phenotype::Cold]]')


xml = f"""
<mediawiki xml:lang="en">
    {site_info()}
    {main_page}
    {category_BMEG}
    {category_Ontology}
    {category_Synonym}
    {category_Compound}
    {category_CompoundSynonym}
    {category_Phenotype}
    {category_PhenotypeSynonym}
    {property_Term}
    {property_TermId}
    {property_GID}
    {property_Ontology}
    {property_SelectedOntology}
    {property_CompoundSynonym}
    {property_Compound}
    {property_PhenotypeSynonym}
    {property_Phenotype}
    {category_PUBCHEM}
    {category_CHEBI}
    {category_DRUGBANK}
    {category_INCHI}
    {category_NO_ONTOLOGY}
    {category_CHEMBL}
    {category_MONDO}
    {category_OMIA}
    {compound_Aspirin}
    {ontology_CID2244}
    {synonym_ACETYLSALICYLIC_ACID}
    {phenotype_Cold}
    {synonym_Sniffles}
    {ontology_MONDO_0005709}
</mediawiki>
"""


@click.command()
@click.option('--output', default='data/imports/special_pages.xml', help='XML output file.')
# @click.option('--input', default='data/Compound.wiki.json.gz', help='gz input file.')
def transform(output):
    with open(output, 'w') as out_fh:
        out_fh.write(xml)

if __name__ == '__main__':
    transform()
