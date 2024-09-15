#!/usr/bin/env python
import json
from module_test_template.schemas import InputSchema
from module_test_template.utils import get_logger


logger = get_logger(__name__)


def run(
    inputs: InputSchema,
    worker_nodes = None,
    orchestrator_node = None,
    flow_run = None,
    cfg: dict = None
):
    logger.info(f"Running with inputs {inputs.prompt}")
    logger.info(f"cfg: {cfg}")

    prompt = inputs.prompt
    modified_prompt = f"This is a modified prompt: {prompt}"

    
    return json.dumps({"modified_prompt": modified_prompt})

