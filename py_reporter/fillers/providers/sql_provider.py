#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import FillerProvider


class SqlProvider(FillerProvider):

    def __init__(self, *args, **kwargs):
        super(SqlProvider, self).__init__(*args, **kwargs)

# vim: filetype=python
