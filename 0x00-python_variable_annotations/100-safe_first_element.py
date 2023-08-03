#!/usr/bin/env python3
'''Augmented the code below'''

from typing import Sequence, Any, Union
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augmented Code """
    if lst:
        return lst[0]
    else:
        return None