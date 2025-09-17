from dataclasses import dataclass
from pint import Quantity

@dataclass
class BoltConfig:
    min_tensile_yield_strength: Quantity
    min_proof_strength: Quantity
    pitch_coarse: Quantity
    coarse_tensile_stress_area: Quantity
    nut_height: Quantity
    head_diameter: Quantity
    nominal_diameter: Quantity
    elastic_modulus: Quantity
    length: Quantity

class Bolt:
    def __init__(self, config):
        self.config = config

