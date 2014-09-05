#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xlrd import open_workbook


def get_workbook(excel_path):
    return open_workbook(excel_path, on_demand=True)


def get_named_range(workbook, named_range):
    return workbook.name_map.get(named_range.lower())


# vim: filetype=python
