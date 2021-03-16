from typing import Dict

from logging import Logger
from time import time
from azure.functions import AppExtensionBase, Context


class TimerExtension(AppExtensionBase):
    invocations: Dict[str, float] = {}

    @classmethod
    def post_load_app_level(cls, fname, fdirectory, *args, **kwargs):
        print('IT IS OKOKOKOK')

    @classmethod
    def pre_invocation_app_level(cls, logger: Logger, context: Context, func_args: Dict[str, object], *args, **kwargs) -> None:
        cls.invocations[context.invocation_id] = time()

    @classmethod
    def post_invocation_app_level(cls, logger: Logger, context: Context, func_args: Dict[str, object], func_ret: object, *args, **kwargs) -> None:
        elapsed_sec = time() - cls.invocations.pop(context.invocation_id)
        logger.warn(f'{context.function_name} Elapsed: {elapsed_sec} seconds')