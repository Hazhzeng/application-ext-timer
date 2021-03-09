from typing import Dict

from logging import Logger
from time import time
from azure.functions import AppExtensionBase, Context


class TimerExtension(AppExtensionBase):
    invocations: Dict[str, float] = {}

    @classmethod
    def before_invocation_global(cls, logger: Logger, context: Context, *args, **kwargs) -> None:
        cls.invocations[context.invocation_id] = time()

    @classmethod
    def after_invocation_global(cls, logger: Logger, context: Context, *args, **kwargs) -> None:
        elapsed_sec = time() - cls.invocations.pop(context.invocation_id)
        logger.warn(f'{context.function_name} Elapsed: {elapsed_sec} seconds')