from ..utils.lookup_table import LookupTable
from pathlib import Path
from dataclasses import dataclass
from pint import Quantity

@dataclass
class MemberConfig:
    thickness: Quantity
    elastic_modulus: Quantity
    yield_strength: Quantity

class Member:
    current_dir = Path(__file__).parent
    material_props = LookupTable.from_csv(current_dir / "material.csv", index_col="material")

    def __init__(self, config: MemberConfig):
        self.config = config
        # instances don’t need to reload CSVs, just reuse class-level props
        self.material_props = Member.material_props