from behave._types import Unknown as Unknown
from behave.formatter.base import StreamOpener as StreamOpener
from behave.model import ScenarioOutline as ScenarioOutline
from behave.model_core import FileLocation as FileLocation
from behave.reporter.junit import JUnitReporter as JUnitReporter
from behave.reporter.summary import SummaryReporter as SummaryReporter
from behave.tag_expression import TagExpression as TagExpression
from behave.textutil import select_best_encoding as select_best_encoding, to_texts as to_texts
from behave.userdata import UserData as UserData, parse_user_define as parse_user_define
from six.moves import configparser
from typing import Any, Optional

ConfigParser = configparser.ConfigParser

class LogLevel:
    names: Any = ...
    @staticmethod
    def parse(levelname: Any, unknown_level: Optional[Any] = ...): ...
    @classmethod
    def parse_type(cls, levelname: Any): ...
    @staticmethod
    def to_string(level: Any): ...

class ConfigError(Exception): ...

options: Any
raw_value_options: Any

def read_configuration(path: Any): ...
def config_filenames() -> None: ...
def load_configuration(defaults: Any, verbose: bool = ...) -> None: ...
def setup_parser(): ...

class Configuration:
    defaults: Any = ...
    cmdline_only_options: Any = ...
    version: Any = ...
    tags_help: Any = ...
    lang_list: Any = ...
    lang_help: Any = ...
    default_tags: Any = ...
    junit: Any = ...
    logging_format: Any = ...
    logging_datefmt: Any = ...
    name: Any = ...
    scope: Any = ...
    steps_catalog: Any = ...
    userdata: Any = ...
    wip: Any = ...
    formatters: Any = ...
    reporters: Any = ...
    name_re: Any = ...
    outputs: Any = ...
    include_re: Any = ...
    exclude_re: Any = ...
    scenario_outline_annotation_schema: Any = ...
    steps_dir: str = ...
    environment_file: str = ...
    userdata_defines: Any = ...
    more_formatters: Any = ...
    paths: Any = ...
    default_format: str = ...
    format: Any = ...
    dry_run: bool = ...
    summary: bool = ...
    show_skipped: bool = ...
    quiet: bool = ...
    tags: Any = ...
    color: bool = ...
    stop: bool = ...
    log_capture: bool = ...
    stdout_capture: bool = ...
    show_source: bool = ...
    show_snippets: bool = ...
    stage: Any = ...
    stderr_capture: bool = ...
    def __init__(self, command_args: Optional[Any] = ..., load_config: bool = ..., verbose: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def setup_outputs(self, args_outfiles: Optional[Any] = ...) -> None: ...
    def setup_formats(self) -> None: ...
    def collect_unknown_formats(self): ...
    @staticmethod
    def build_name_re(names: Any): ...
    def exclude(self, filename: Any): ...
    def setup_logging(self, level: Optional[Any] = ..., configfile: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def setup_model(self) -> None: ...
    def setup_stage(self, stage: Optional[Any] = ...) -> None: ...
    def setup_userdata(self) -> None: ...
    def update_userdata(self, data: Any) -> None: ...