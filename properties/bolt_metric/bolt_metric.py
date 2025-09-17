from ..utils.lookup_table import LookupTable
from pathlib import Path

class BoltMetric:
    def __init__(self):
        # Get the directory where this file is located
        current_dir = Path(__file__).parent
        
        self.class_table = LookupTable.from_csv(current_dir / "class.csv", index_col="class")
        self.dimensional_table = LookupTable.from_csv(current_dir / "dimensional.csv", index_col="dia_basic")
        self.material_table = LookupTable.from_csv(current_dir / "material.csv", index_col="material")