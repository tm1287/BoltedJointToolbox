from properties import BoltMetric

if __name__ == "__main__":
    print(BoltMetric.class_props.df)
    print(BoltMetric.class_props.get(4.6, field="min_tensile_yield_strength"))
