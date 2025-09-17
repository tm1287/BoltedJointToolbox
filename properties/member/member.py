from ..utils.lookup_table import LookupTable
from pathlib import Path

class Member:
    current_dir = Path(__file__).parent
    material_props = LookupTable.from_csv(current_dir / "material.csv", index_col="material")

    def __init__(self):
        # instances don’t need to reload CSVs, just reuse class-level props
        self.material_props = Member.material_props
