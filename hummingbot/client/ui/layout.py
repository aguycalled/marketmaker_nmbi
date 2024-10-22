#!/usr/bin/env python

from os.path import join, realpath, dirname
import sys; sys.path.insert(0, realpath(join(__file__, "../../../")))

from prompt_toolkit.layout.containers import (
    VSplit,
    HSplit,
    Window,
    FloatContainer,
    Float,
    WindowAlign,
)
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer
from prompt_toolkit.utils import is_windows
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import SearchToolbar

from hummingbot.client.ui.custom_widgets import CustomTextArea as TextArea
from hummingbot.client.settings import (
    MAXIMUM_OUTPUT_PANE_LINE_COUNT,
    MAXIMUM_LOG_PANE_LINE_COUNT,
)


HEADER = """
            +--------------------------------------------------------------+
            |                    XXX XXXXXXXXXXXX             XXXXXXXXXXXXX|
            |                   XXXXXXXXXXXXXXXXXXX         XXX           X|
            |                  XXX XXXXXXXXXXXXX   XX      XX            XX|
            |                 XXXXX XXXXXXXXXX X    XXX XXXX            X  |
            |                 XXXXXX XXXXXXXXX XX X   XX               XX  |
            |                XXXXXXXXX XXXXX   XX   X    X             X   |
            |               XXXXXXXXXXXX XX X XX X X  X               X    |
            |               XXXXXXXXXXXXXXX  XXX X                   XX    |
            |              XXXXXXXXXXXXXXXX   X XX     X            XX     |
            |             XXXXXXXXXXXXXXX    X  X    XX            XX      |
            |            XXXXXXXXXXXXXXXX  X XX XX    X           X        |
            |            XXXXXXXXXXXXXXXX   XX  XX               XX        |
            |           XXXXXXXXXXXXXXXX X  XXXXXX  X    X      XX         |
            |          XXXXXXXXXXXXXXX    X XX   X              X          |
            |          XXXXXXXXXXXXXXX XX     X  X             X           |
            |         XXXXXXXXXXXXXXX    X X  XX  X   X       X            |
            |        XXXXXXXXXXXXXXXXX X       X  X   X     XX             |
            |       XXXXXXXXXXXXXXXX XXX X  X XX  X   X     X              |
            |       XXXXXXXXXXXXXXX    XX  XXXX  X X        X              |
            |      XXXXXXXXXXXXXXX      XXXXXXXXXXXXX      XX              |
            |     XXXXXXXXXXXXXXX         X   XXX X XX X  XX               |
            |    XXXXXXXXXXXXXXX           XXXXXXXXXXXXX  X                |
            |    XXXXXXXXXXXXXXX            XXXXXXXXXX  XX                 |
            +-------------------------------XXXXXXXXXXXXX------------------+



               ███╗   ██╗███████╗██╗   ██╗ ██████╗ ██████╗ ██╗███╗   ██╗
               ████╗  ██║██═══██║██║   ██║██╔════╝██╔═══██╗██║████╗  ██║
               ██╔██╗ ██║███████║██║   ██║██║     ██║   ██║██║██╔██╗ ██║
               ██║╚██╗██║██╔══██║ ██║ ██║ ██║     ██║   ██║██║██║╚██╗██║
               ██║ ╚████║██║  ██║ ██████║ ╚██████╗╚██████╔╝██║██║ ╚████║
               ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝

================================================================================================
Press CTRL + C to quit at any time.
Enter "help" for a list of commands.
"""

with open(realpath(join(dirname(__file__), '../../VERSION'))) as version_file:
    version = version_file.read().strip()


def create_input_field(lexer=None, completer: Completer = None):
    return TextArea(
        height=10,
        prompt='>>> ',
        style='class:input-field',
        multiline=False,
        focus_on_click=True,
        lexer=lexer,
        auto_suggest=AutoSuggestFromHistory(),
        completer=completer,
        complete_while_typing=True,
    )


def create_output_field():
    return TextArea(
        style='class:output-field',
        focus_on_click=False,
        read_only=False,
        scrollbar=True,
        max_line_count=MAXIMUM_OUTPUT_PANE_LINE_COUNT,
        initial_text=HEADER,
    )


def create_search_field() -> SearchToolbar:
    return SearchToolbar(text_if_not_searching=[('class:primary', "[CTRL + F] to start searching.")],
                         forward_search_prompt=[('class:primary', "Search logs [Press CTRL + F to hide search] >>> ")],
                         ignore_case=True)


def create_log_field(search_field: SearchToolbar):
    return TextArea(
        style='class:log-field',
        text="Running logs\n",
        focus_on_click=False,
        read_only=False,
        scrollbar=True,
        max_line_count=MAXIMUM_LOG_PANE_LINE_COUNT,
        initial_text="Running Logs \n",
        search_field=search_field,
        preview_search=False,
    )


def get_version():
    return [("class:title", f"Version: {version}")]


def get_bounty_status():
    from hummingbot.client.liquidity_bounty.liquidity_bounty_config_map import liquidity_bounty_config_map
    enabled = liquidity_bounty_config_map["liquidity_bounty_enabled"].value is True and \
        liquidity_bounty_config_map["liquidity_bounty_client_id"].value is not None
    bounty_status = "ON" if enabled else "OFF"
    style = "class:primary" if enabled else "class:warning"
    return [(style, f"bounty_status: {bounty_status}")]


def get_paper_trade_status():
    from hummingbot.client.config.global_config_map import global_config_map
    enabled = global_config_map["paper_trade_enabled"].value is True
    paper_trade_status = "ON" if enabled else "OFF"
    style = "class:primary" if enabled else "class:warning"
    return [(style, f"paper_trade_mode: {paper_trade_status}")]


def get_title_bar_right_text():
    copy_key = "CTRL + SHIFT" if is_windows() else "fn"
    return [
        ("class:title", f"[Double Ctrl + C] QUIT      "),
        ("class:title", f"[Ctrl + S] STATUS      "),
        ("class:title", f"Hold down \"{copy_key}\" for selecting and copying text"),
    ]


def generate_layout(input_field: TextArea,
                    output_field: TextArea,
                    log_field: TextArea,
                    search_field: SearchToolbar):
    root_container = HSplit([
        VSplit([
            Window(FormattedTextControl(get_version), style="class:title"),
            Window(FormattedTextControl(get_bounty_status), style="class:title"),
            Window(FormattedTextControl(get_paper_trade_status), style="class:title"),
            Window(FormattedTextControl(get_title_bar_right_text), align=WindowAlign.RIGHT, style="class:title"),
        ], height=1),
        VSplit([
            FloatContainer(
                HSplit([
                    output_field,
                    Window(height=1, char='-', style='class:primary'),
                    input_field,
                ]),
                [
                    # Completion menus.
                    Float(xcursor=True,
                          ycursor=True,
                          transparent=True,
                          content=CompletionsMenu(
                              max_height=16,
                              scroll_offset=1)),
                ]
            ),
            Window(width=1, char='|', style='class:primary'),
            HSplit([
                log_field,
                search_field,
            ]),
        ]),

    ])
    return Layout(root_container, focused_element=input_field)
