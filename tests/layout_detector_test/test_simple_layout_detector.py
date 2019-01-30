import unittest
import numpy as np
from cell_classifier.simple_tag import SimpleTag
from block_extractor.simple_block import SimpleBlock
from layout_detector.simple_layout_detector import SimpleLayoutDetector


class TestSimpleLayoutDetector(unittest.TestCase):
    def testLayoutDetectionForSimpleTableWithTwoColumns(self):

        sheet = np.array([['date', 'value'], ['2001', '10.0'], ['2002', '11.0'], ['2003', '12.0']])
        tags = np.array([[SimpleTag('META'), SimpleTag('META')], [SimpleTag('DATE'), SimpleTag('_DATA_')],
                                  [SimpleTag('DATE'), SimpleTag('_DATA_')], [SimpleTag('DATE'), SimpleTag('_DATA_')]])

        b1 = SimpleBlock("META", 0, 1, 0, 0)
        b2 = SimpleBlock("DATE", 0, 0, 1, 3)
        b3 = SimpleBlock("_DATA_", 1, 1, 1, 3)

        blocks = [b1, b2, b3]

        sld = SimpleLayoutDetector()
        layout = sld.detect_layout(sheet, tags, blocks)

        assert layout[0] == {2}
        assert layout[1] == {2}
        assert layout[2] == {0, 1}

