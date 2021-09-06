# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

# flake8: noqa
"""
    Submarine Experiment API

    The Submarine REST API allows you to create, list, and get experiments. The API is hosted under the /v1/experiment route on the Submarine server. For example, to list experiments on a server hosted at http://localhost:8080, access http://localhost:8080/api/v1/experiment/  # noqa: E501

    The version of the OpenAPI document: 0.6.0-SNAPSHOT
    Contact: dev@submarine.apache.org
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

# import apis into sdk package
from submarine.experiment.api.experiment_api import ExperimentApi

# import ApiClient
from submarine.experiment.api_client import ApiClient
from submarine.experiment.configuration import Configuration
from submarine.experiment.exceptions import (
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from submarine.experiment.models.code_spec import CodeSpec
from submarine.experiment.models.environment_spec import EnvironmentSpec
from submarine.experiment.models.experiment_meta import ExperimentMeta
from submarine.experiment.models.experiment_spec import ExperimentSpec
from submarine.experiment.models.experiment_task_spec import ExperimentTaskSpec
from submarine.experiment.models.json_response import JsonResponse
from submarine.experiment.models.kernel_spec import KernelSpec

__version__ = "0.6.0-SNAPSHOT"
