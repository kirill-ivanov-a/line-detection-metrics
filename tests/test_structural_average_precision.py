# Copyright (c) 2022, Kirill Ivanov, Anastasiia Kornilova and Dmitrii Iarosh
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

import numpy as np
import pytest

from pathlib import Path

from common import DATA_PATH
from src.metrics.detection.structural import structural_average_precision\


def test_sap():
    pred_lines = np.genfromtxt(DATA_PATH / "pred.csv", delimiter=",")
    gt_lines = np.genfromtxt(DATA_PATH / "gt.csv", delimiter=",")
    line_scores = np.genfromtxt(DATA_PATH / "score.csv", delimiter=",")
    actual = structural_average_precision([pred_lines], [gt_lines], [line_scores])
    expected = 0.3835
    eps = 0.001
    assert np.abs(actual - expected) < eps
