"""Tests of reference publication fidelity, not philosophical assertions."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import build_site
from reference_tables import coupling_table

class ReferencePublicationTests(unittest.TestCase):
    def test_data_change_reaches_article_and_monolith(self):
        # Fixture stays inside the repository; no external workspace is accessed.
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as directory:
            root=Path(directory);(root/'content').mkdir();(root/'data').mkdir()
            (root/'content/home.md').write_text('# Home\n\n## References\n[[graph|Graph]]\n')
            (root/'content/graph.md').write_text('# Graph\n\n<!-- GENERATED:couplings -->\n')
            (root/'content/alpha.md').write_text('# Alpha\n')
            (root/'content/beta.md').write_text('# Beta\n')
            rows=[dict(source='alpha',target='beta',relation='couples-with',emergent_property='first result',evidence_pages=['alpha','beta'])]
            data=root/'data/wiki-couplings.json';data.write_text(json.dumps(rows))
            with patch.multiple(build_site,ROOT=str(root),SRC=str(root/'content')):
                before=build_site.read_pages()
                rows[0]['emergent_property']='revised result';data.write_text(json.dumps(rows))
                after=build_site.read_pages()
            self.assertIn('first result',before['graph']['raw'])
            self.assertNotIn('first result',after['graph']['raw'])
            self.assertIn('revised result',after['graph']['raw'])
            monolith=build_site.build_monolith(after,build_site.parse_nav(after['home']['raw']))
            self.assertIn('revised result',monolith)
            self.assertNotIn('GENERATED:couplings',monolith)

    def test_unresolvable_evidence_is_rejected(self):
        rows=[dict(source='alpha',target='beta',relation='couples-with',emergent_property='result',evidence_pages=['missing'])]
        with self.assertRaisesRegex(ValueError,'unknown page: missing'):
            coupling_table(rows,{'alpha':{'title':'Alpha'},'beta':{'title':'Beta'}})

class SourceExportTests(unittest.TestCase):
    def test_frontmatter_quotes_and_block_lists(self):
        from source_metadata import metadata
        raw = '\n'.join(['---','slug: sample','formal_status:','  tier: CV','regulates: ["scope, evidence", other]','regulated_by:','  - first','  - "second regulator"','valid_attack: "Show a mismatch."','---','# Sample'])
        result=metadata(raw)
        self.assertEqual(result['regulates'],['scope, evidence','other'])
        self.assertEqual(result['regulated_by'],['first','second regulator'])

    def test_source_change_reaches_export_and_reconstruction(self):
        from source_metadata import derived
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as directory:
            root=Path(directory);(root/'content').mkdir();(root/'data').mkdir()
            (root/'content/home.md').write_text('# Home\n## Index\n[[index|Index]]\n')
            (root/'content/index.md').write_text('# Index\n<!-- GENERATED:attacks -->\n')
            source=root/'content/sample.md'
            source.write_text('---\nslug: sample\nformal_status:\n  tier: CV\nvalid_attack: "Old criterion"\nkill_condition: "Mismatch"\n---\n# Sample\n')
            before=derived(root)['wiki-attack-surfaces.json']
            source.write_text(source.read_text().replace('Old criterion','Revised criterion'))
            after=derived(root)['wiki-attack-surfaces.json']
            self.assertNotEqual(before,after)
            (root/'data/wiki-attack-surfaces.json').write_text(json.dumps(after))
            with patch.multiple(build_site,ROOT=str(root),SRC=str(root/'content')):
                pages=build_site.read_pages()
            self.assertIn('Revised criterion',pages['index']['raw'])
            self.assertIn('Not registered',pages['index']['raw'])
            self.assertNotIn('Old criterion',pages['index']['raw'])
            mono=build_site.build_monolith(pages,build_site.parse_nav(pages['home']['raw']))
            self.assertIn('Revised criterion',mono)
            self.assertNotIn('GENERATED:attacks',mono)

if __name__=='__main__':
    unittest.main()
