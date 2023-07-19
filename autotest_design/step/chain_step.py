from typing import Optional


class Step:

    def __init__(self):
        self.current_step = None
        self.step_map = {}

    def _add_step_info(self, func_name, step_to, step_need):
        self.step_map[func_name] = {'to': step_to, 'need': step_need}

    def step(self, this: str, need: Optional[str] = None):
        def registry_step(func):
            func_name = func.__name__
            self._add_step_info(func_name=func_name, step_to=this, step_need=need)

            def wrap(*args, **kwargs):
                if self.current_step != need:
                    raise ValueError('Unexpected step!')
                result = func(*args, *kwargs)
                self.current_step = this
                return result

            return wrap

        return registry_step
