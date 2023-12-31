
import dijkstra as dk
import bellmanford as bf

if __name__ == '__main__':
    start_v = 0
    files = ["ds/src/ds_2023-main/fsp/graph_pos.txt", "ds/src/ds_2023-main/fsp/graph_neg.txt"]

    # Find shortest path with Dijkstra algorithm
    print("------------------------------------------")
    print("Find shortest path with Dijkstra algorithm")
    print("------------------------------------------")
    for file in files:
        print("input_data: ", file)
        fsp = dk.FindShortestPath()
        fsp.load_data(file)
        fsp.initialize()
        fsp.find_path(start_v)
        fsp.print_path(start_v)
        print()

    # Find shortest path with Bellman-Ford algorithm
    print("---------------------------------------------")
    print("Find shortest path with BellmanFord algorithm")
    print("---------------------------------------------")


    for file in files:
        print("input_data: ", file)
        fsp = bf.FindShortestPath()
        fsp.load_data(file)
        fsp.initialize()
        fsp.find_path(start_v)
        fsp.print_path(start_v)
        print()