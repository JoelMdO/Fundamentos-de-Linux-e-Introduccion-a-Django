
from typing import Any

class TemplateTitleMixin(object):
    title = None
    def get_context_data(self, *args: Any, **kwargs: Any) -> dict[str, str]:
        context = super().get_context_data(*args, **kwargs) # type: ignore
        context["title"] = self.get_title()
        return context # type: ignore
    
    def get_title(self) -> str:
        if self.title is None:
            return "Default Title"
        return self.title