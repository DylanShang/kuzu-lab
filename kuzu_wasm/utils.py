from typing import Any
import networkx as nx

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
def toNetworkx(data,directed: bool = True) -> nx.MultiGraph | nx.MultiDiGraph:
    import pandas as pd
    #convert to df
    if not isinstance(data, pd.DataFrame):
        data = toDf(data)
        
    nx_graph = nx.MultiDiGraph() if directed else nx.MultiGraph()
    nodes = {}
    rels = []
    table_to_label_dict = {}
    table_primary_key_dict = {}
    
    
    def determine_type(cell):
        cell_type = "NODE"
        if "_SRC" in cell and "_DST" in cell:
            cell_type = "REL"
        elif "_nodes" in cell and "_rels" in cell:
            cell_type = "RECURSIVE_REL"
        return cell_type
    column_names = data.columns
    
    for column in  column_names:
        first_cell = data[column][0]
        column_type = determine_type(first_cell)
        #iterate
        for i in range(len(data[column])):
            cell = data[column][i]
            if column_type == "NODE":
                _id = cell["_ID"]
                nodes[(_id["table"], _id["offset"])] = cell
                table_to_label_dict[_id["table"]] = cell["_LABEL"]
            elif column_type == "REL":
                rels.append(cell)
            elif column_type == "RECURSIVE_REL":
                for node in cell["_nodes"]:
                    _id = node["_ID"]
                    nodes[(_id["table"], _id["offset"])] = node
                    table_to_label_dict[_id["table"]] = node["_LABEL"]
                for rel in cell["_rels"]:
                    for key in list(rel.keys()):
                        if rel[key] is None:
                            del rel[key]
                    rels.append(rel)
    # Add nodes
    for node in nodes.values():
        _id = node["_ID"]
        node_id = node["_LABEL"] + "_" + str(_id["offset"])
        node[node["_LABEL"]] = True
        nx_graph.add_node(node_id, **node)

    # Add rels
    for rel in rels:
        _src = rel["_SRC"]
        _dst = rel["_DST"]
        src_node = nodes[(_src["table"], _src["offset"])]
        dst_node = nodes[(_dst["table"], _dst["offset"])]
        src_id = src_node["_LABEL"] + "_" + str(src_node["_ID"]["offset"])
        dst_id = dst_node["_LABEL"] + "_" + str(dst_node["_ID"]["offset"])
        nx_graph.add_edge(src_id, dst_id, **rel)
    return nx_graph
            

        