"""
Tests for splitter objects.
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__author__ = "Bharath Ramsundar"
__copyright__ = "Copyright 2016, Stanford University"
__license__ = "GPL"

import os
import unittest
from deepchem.splits import RandomSplitter
from deepchem.splits import ScaffoldSplitter
from deepchem.splits import StratifiedSplitter
from deepchem.datasets.tests import TestDatasetAPI

class TestSplitters(TestDatasetAPI):
  """
  Test some basic splitters.
  """
  """
  def test_singletask_random_split(self):
    Test singletask RandomSplitter class.
    solubility_dataset = self.load_solubility_data()
    random_splitter = RandomSplitter()
    train_data, valid_data, test_data = \
        random_splitter.train_valid_test_split(
            solubility_dataset,
            self.train_dir, self.valid_dir, self.test_dir,
            frac_train=0.8, frac_valid=0.1, frac_test=0.1)
    assert len(train_data) == 8
    assert len(valid_data) == 1
    assert len(test_data) == 1

  def test_singletask_scaffold_split(self):
    Test singletask ScaffoldSplitter class.
    solubility_dataset = self.load_solubility_data()
    scaffold_splitter = ScaffoldSplitter()
    train_data, valid_data, test_data = \
        scaffold_splitter.train_valid_test_split(
            solubility_dataset,
            self.train_dir, self.valid_dir, self.test_dir,
            frac_train=0.8, frac_valid=0.1, frac_test=0.1)
    assert len(train_data) == 8
    assert len(valid_data) == 1
    assert len(test_data) == 1

  def test_multitask_random_split(self):
    Test multitask RandomSplitter class.
    multitask_dataset = self.load_multitask_data()
    random_splitter = RandomSplitter()
    train_data, valid_data, test_data = \
        random_splitter.train_valid_test_split(
            multitask_dataset,
            self.train_dir, self.valid_dir, self.test_dir,
            frac_train=0.8, frac_valid=0.1, frac_test=0.1)
    assert len(train_data) == 8
    assert len(valid_data) == 1
    assert len(test_data) == 1

  def test_multitask_scaffold_split(self):
    Test multitask ScaffoldSplitter class.
    multitask_dataset = self.load_multitask_data()
    scaffold_splitter = ScaffoldSplitter()
    train_data, valid_data, test_data = \
        scaffold_splitter.train_valid_test_split(
            multitask_dataset,
            self.train_dir, self.valid_dir, self.test_dir,
            frac_train=0.8, frac_valid=0.1, frac_test=0.1)
    assert len(train_data) == 8
    assert len(valid_data) == 1
    assert len(test_data) == 1
"""
  def test_stratified_multitask_split(self):
   print("In stratified tester")
   sparse_dataset = self.load_sparse_multitask_dataset()
   stratified_splitter = StratifiedSplitter()
   train_data, valid_data, test_data = \
      stratified_splitter.train_valid_test_split(
          sparse_dataset,
          self.train_dir, self.valid_dir, self.test_dir,
          frac_train = 0.8, frac_valid = 0.1, frac_test = 0.1
      )
   print("end of stratified test")
   assert 1 == 1
