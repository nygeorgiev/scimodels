import types
from dataclasses import dataclass

from scimodels.exceptions import DependencyError

@dataclass(frozen=True)
class DependencyResult:
    name: str
    module: types.ModuleType | None = None
    loaded: bool = False
    exception: DependencyError | None = None

    def __post_init__(self):
        if self.loaded:
            if self.module is None:
                raise ValueError("'module' cannot be None when 'loaded' is True")
            if self.exception is not None:
                raise ValueError("'error' must be None when 'loaded' is True")
        else:
            if self.module is not None:
                raise ValueError("'loaded' must the True when 'module' is not None")
            if self.exception is None:
                raise ValueError("'loaded' must be True, when 'error' is None")
            

class DepedencyLoader:
    @staticmethod
    def load(
        dependency_name: str
    ) -> DependencyResult:
        try:
            return DependencyResult(
                name=dependency_name,
                module=__import__(dependency_name),
                loaded=True,
                exception=None
            )
        except:
            return DependencyResult(
                name=dependency_name,
                module=None,
                loaded=False,
                exception=DependencyError(dependency_name)
            )