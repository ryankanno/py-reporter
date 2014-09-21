#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class FillerProvider(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        super(FillerProvider, self).__init__(*args, **kwargs)

# vim: filetype=python
