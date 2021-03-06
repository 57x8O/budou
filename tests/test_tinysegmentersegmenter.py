# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .context import budou
import unittest

class TestTinysegmenterSegmenter(unittest.TestCase):

  def setUp(self):
    self.segmenter = budou.tinysegmentersegmenter.TinysegmenterSegmenter()

  def test_segment(self):
    chunks = self.segmenter.segment(u'これは Android です。')
    expected = [u'これは', '\n', u'Android です。']
    self.assertListEqual(expected, [chunk.word for chunk in chunks],
        'Chunks should be generated as intended.')


if __name__ == '__main__':
  unittest.main()



