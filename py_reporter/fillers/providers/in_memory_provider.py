#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import FillerProvider


class InMemoryProvider(FillerProvider):

    def __init__(self, *args, **kwargs):
        super(InMemoryProvider, self).__init__(*args, **kwargs)

# vim: filetype=python
