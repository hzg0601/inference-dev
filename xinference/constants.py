# Copyright 2022-2023 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path

XINFERENCE_ENV_ENDPOINT = "XINFERENCE_ENDPOINT"
XINFERENCE_ENV_MODEL_SRC = "XINFERENCE_MODEL_SRC"
XINFERENCE_ENV_HOME_PATH = "XINFERENCE_HOME"
XINFERENCE_ENV_HEALTH_CHECK_ATTEMPTS = "XINFERENCE_HEALTH_CHECK_ATTEMPTS"
XINFERENCE_ENV_HEALTH_CHECK_INTERVAL = "XINFERENCE_HEALTH_CHECK_INTERVAL"
XINFERENCE_ENV_DISABLE_VLLM = "XINFERENCE_DISABLE_VLLM"


def get_xinference_home():
    return os.environ.get(XINFERENCE_ENV_HOME_PATH, str(Path.home() / ".xinference"))


XINFERENCE_HOME = get_xinference_home()
XINFERENCE_CACHE_DIR = os.path.join(XINFERENCE_HOME, "cache")
XINFERENCE_MODEL_DIR = os.path.join(XINFERENCE_HOME, "model")
XINFERENCE_LOG_DIR = os.path.join(XINFERENCE_HOME, "logs")
XINFERENCE_IMAGE_DIR = os.path.join(XINFERENCE_HOME, "image")

XINFERENCE_DEFAULT_LOCAL_HOST = "127.0.0.1"
XINFERENCE_DEFAULT_DISTRIBUTED_HOST = "0.0.0.0"
XINFERENCE_DEFAULT_ENDPOINT_PORT = 9997
XINFERENCE_DEFAULT_LOG_FILE_NAME = "xinference.log"
XINFERENCE_LOG_MAX_BYTES = 100 * 1024 * 1024
XINFERENCE_LOG_BACKUP_COUNT = 30
XINFERENCE_HEALTH_CHECK_ATTEMPTS = int(
    os.environ.get(XINFERENCE_ENV_HEALTH_CHECK_ATTEMPTS, 3)
)
XINFERENCE_HEALTH_CHECK_INTERVAL = int(
    os.environ.get(XINFERENCE_ENV_HEALTH_CHECK_INTERVAL, 3)
)
XINFERENCE_DISABLE_VLLM = bool(int(os.environ.get(XINFERENCE_ENV_DISABLE_VLLM, 0)))
