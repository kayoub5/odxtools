# SPDX-License-Identifier: MIT
# Copyright (c) 2022 MBition GmbH

from dataclasses import dataclass
from typing import Optional

from .odxlink import OdxLinkId, OdxDocFragment

@dataclass()
class StateTransition:
    """
    Corresponds to STATE.
    """
    id: OdxLinkId
    short_name: str
    long_name: Optional[str] = None
    source_short_name: Optional[str] = None
    target_short_name: Optional[str] = None


def read_state_transition_from_odx(et_element, doc_frag):
    short_name = et_element.find("SHORT-NAME").text
    id = OdxLinkId.from_et(et_element, doc_frag)

    long_name = et_element.find(
        "LONG-NAME").text if et_element.find("LONG-NAME") is not None else None
    source_short_name = et_element.find("SOURCE-SNREF").attrib["SHORT-NAME"] if et_element.find("SOURCE-SNREF") is not None else None
    target_short_name = et_element.find("TARGET-SNREF").attrib["SHORT-NAME"] if et_element.find("TARGET-SNREF") is not None else None

    return StateTransition(id=id,
                           short_name=short_name,
                           long_name=long_name,
                           source_short_name=source_short_name,
                           target_short_name=target_short_name)
