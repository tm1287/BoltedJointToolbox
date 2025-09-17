from ..utils.lookup_table import LookupTable
from pathlib import Path
from pint import Quantity
from .bolt import Bolt, BoltConfig


class BoltMetric(Bolt):
    current_dir = Path(__file__).parent

    class_props = LookupTable.from_csv(current_dir / "class.csv", index_col="class")
    dimensional_props = LookupTable.from_csv(current_dir / "dimensional.csv", index_col="dia_basic")
    material_props = LookupTable.from_csv(current_dir / "material.csv", index_col="material")

    def __init__(self, config: BoltConfig):
        super().__init__(config)
        # instances don’t need to reload CSVs, just reuse class-level props
        self.class_props = BoltMetric.class_props
        self.dimensional_props = BoltMetric.dimensional_props
        self.material_props = BoltMetric.material_props
