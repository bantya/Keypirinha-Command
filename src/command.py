import os
import re
import subprocess
import keypirinha as kp
import keypirinha_util as kpu

class Command(kp.Plugin):

    SECTION_MAIN = 'main'

    REGEX_INPUT = r'^(>{1,2})\s(.+)'

    ITEM_COMMAND = kp.ItemCategory.USER_BASE + 1

    def __init__(self):
        super().__init__()

    def on_start(self):
        self._load_settings()

        actions = []

        actions.append(self._set_action('keep_open', 'Keep Open', 'Run the command and keep CMD open.'))
        actions.append(self._set_action('close_cmd', 'Close CMD', 'Close CMD after running the command.'))

        self.set_actions(self.ITEM_COMMAND, actions)

    def on_catalog(self):
        self.on_start()

    def on_suggest(self, user_input, items_chain):
        input = re.search(self.REGEX_INPUT, user_input)

        if input is None:
            return None

        if len(input.groups()) != 2:
            pass
        else:
            operator = input.group(1)
            command = input.group(2)

        suggestion = [self._set_suggestion(operator + '@' + command)]

        self.set_suggestions(suggestion)

    def on_execute(self, item, action):
        if item.category() != self.ITEM_COMMAND:
            return

        prompt = 'C:\\Windows\\System32\\cmd.exe'

        [operator, command] = self._split_target(item.target())

        if operator == '>':
            close = '/k'
        elif operator == '>>':
            close = '/c'

        if action and action.name() == "keep_open":
            close = '/k'
        elif action and action.name() == "close_cmd":
            close = '/c'

        if os.path.isfile(prompt):
            try:
                cmd = [prompt]
                cmd.append(close)
                cmd.append(command)
                subprocess.Popen(cmd, cwd = os.path.dirname(prompt))
            except Exception as e:
                print('Exception: CMD - (%s)' % (e))
        else:
            print('Error: Could not find your %s executable.\n\nPlease edit path' % (prompt))

    def on_activated(self):
        pass

    def on_deactivated(self):
        pass

    def on_events(self, flags):
        pass

    def _set_action(self, name, label, desc):
        return self.create_action(
            name = name,
            label = label,
            short_desc = desc
        )

    def _set_suggestion(self, target):
        [operator, command] = self._split_target(target)

        if operator == '>':
            close_msg = ''
        elif operator == '>>':
            close_msg = ' and close CMD.'

        return self.create_item(
            category = self.ITEM_COMMAND,
            label = operator + ' ' + command,
            short_desc = 'Run \'' + command + '\' command' + close_msg,
            target = target,
            args_hint = kp.ItemArgsHint.FORBIDDEN,
            hit_hint = kp.ItemHitHint.IGNORE
        )

    def _load_settings(self):
        self.settings = self.load_settings()

    def _split_target(self, target):
        return target.split('@')
