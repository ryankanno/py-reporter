#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose.tools import raises
import os
from py_reporter.utilities import get_named_range
from py_reporter.utilities import get_workbook
import unittest


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.test_excel_file = os.path.join(self.cwd, 'data', 'test.xlsx')

    def test_get_workbook_with_valid_excel_file(self):
        workbook = get_workbook(self.test_excel_file)
        ok_(workbook is not None)

    @raises(IOError)
    def test_get_workbook_with_invalid_excel_file(self):
        get_workbook('/v/a/b/x/c/d')

    def test_get_named_range_with_valid_workbook(self):
        workbook = get_workbook(self.test_excel_file)
        ok_(len(get_named_range(workbook, 'test')) > 0)


# vim: filetype=python
