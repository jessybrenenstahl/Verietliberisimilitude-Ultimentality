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

if __name__=='__main__':
    unittest.main()
