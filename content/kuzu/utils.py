def toArrow(result):
    import pyarrow as pa
    serialized_table = result.table.toIPC().to_bytes()
    reader = pa.ipc.open_stream(serialized_table)
    table = reader.read_all()
    return table
def toDf(result):
    import pandas as pd
    import pyarrow as pa
    serialized_table = result.table.toIPC().to_bytes()
    reader = pa.ipc.open_stream(serialized_table)
    table = reader.read_all().to_pandas()
    return table