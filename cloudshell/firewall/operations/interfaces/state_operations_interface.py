#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod


class StateOperationsInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def health_check(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    def reload(self):
        pass
