'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')

    def test_h1(self):
        self.assertEqual(
                run_markdown('#This Should Be An H1'),
                '<p><h1>This Should Be An H1</h1></p>')

    def test_h2(self):
        self.assertEqual(
                run_markdown('##This Should Be An H2'),
                '<p><h2>This Should Be An H2</h2></p>')

    def test_h3(self):
        self.assertEqual(
                run_markdown('###This Should Be An H3'),
                '<p><h3>This Should Be An H3</h3></p>')

    def test_blockquote(self):
        self.assertEqual(
                run_markdown('>line1\n>line2\n>line3\nnot blockquote'),
                '<p><blockquote><p>line1</p><p>line2</p><p>line3</p></blockquote>not blockquote</p>')


if __name__ == '__main__':
    unittest.main()
