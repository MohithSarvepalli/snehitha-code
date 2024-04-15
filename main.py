import time
import random

class MapColoringSolver:
    def __init__(self, states, adjacency):
        self.states = states
        self.adjacency = adjacency
        self.colors = {}

    def is_valid_color(self, state, color):
        for neighbor in self.adjacency[state]:
            if neighbor in self.colors and self.colors[neighbor] == color:
                return False
        return True

    def dfs_without_heuristics(self):
        self.colors = {}
        start_time = time.time()
        result, backtracks = self.dfs()
        end_time = time.time()
        return result, backtracks, end_time - start_time

    def dfs_forward_checking(self):
        self.colors = {}
        start_time = time.time()
        result, backtracks = self.dfs_forward_checking_recursive()
        end_time = time.time()
        return result, backtracks, end_time - start_time

    def dfs_singleton_domains(self):
        self.colors = {}
        start_time = time.time()
        result, backtracks = self.dfs_singleton_domains_recursive()
        end_time = time.time()
        return result, backtracks, end_time - start_time

    def dfs(self):
        return self.dfs_recursive(0)

    def dfs_recursive(self, index):
        if index == len(self.states):
            return True, 0

        state = self.states[index]
        backtracks = 0
        for color in range(1, len(self.states) + 1):
            if self.is_valid_color(state, color):
                self.colors[state] = color
                result, b = self.dfs_recursive(index + 1)
                backtracks += b
                if result:
                    return True, backtracks
                del self.colors[state]
            backtracks += 1
        return False, backtracks

    def dfs_forward_checking_recursive(self):
        return self.dfs_forward_checking_recursive_impl(0)

    def dfs_forward_checking_recursive_impl(self, index):
        if index == len(self.states):
            return True, 0

        state = self.states[index]
        backtracks = 0
        for color in range(1, len(self.states) + 1):
            if self.is_valid_color(state, color):
                self.colors[state] = color
                result, b = self.dfs_forward_checking_recursive_impl(index + 1)
                backtracks += b
                if result:
                    return True, backtracks
                del self.colors[state]
            backtracks += 1
        return False, backtracks

    def dfs_singleton_domains_recursive(self):
        return self.dfs_singleton_domains_recursive_impl(0)

    def dfs_singleton_domains_recursive_impl(self, index):
        if index == len(self.states):
            return True, 0

        state = self.states[index]
        backtracks = 0
        for color in range(1, len(self.states) + 1):
            if self.is_valid_color(state, color):
                self.colors[state] = color
                result, b = self.dfs_singleton_domains_recursive_impl(index + 1)
                backtracks += b
                if result:
                    return True, backtracks
                del self.colors[state]
            backtracks += 1
        return False, backtracks


def main():
    # Define states and adjacency for both maps
    usa_states = ["WA", "OR", "CA", "ID", "NV", "UT", "AZ", "MT", "WY", "CO", "NM", "ND", "SD", "NE", "KS", "OK", "TX", "MN", "IA", "MO", "AR", "LA", "WI", "IL", "MS", "MI", "IN", "OH", "KY", "TN", "AL", "GA", "FL", "SC", "NC", "VA", "WV", "MD", "DE", "PA", "NJ", "NY", "CT", "RI", "MA", "NH", "VT", "ME", "HI", "AK"]
    australia_states = ["WA", "NT", "SA", "QL", "NSW", "VIC", "TA"]

    # USA Map Adjacency
    usa_adjacency = {
    "WA": ["OR", "ID"],
    "OR": ["WA", "ID", "NV", "CA"],
    "CA": ["OR", "NV", "AZ"],
    "ID": ["WA", "OR", "NV", "MT", "WY", "UT"],
    "NV": ["OR", "CA", "ID", "UT", "AZ"],
    "UT": ["ID", "NV", "AZ", "CO", "WY"],
    "AZ": ["CA", "NV", "UT", "CO", "NM"],
    "MT": ["ID", "WY", "SD", "ND"],
    "WY": ["ID", "MT", "SD", "NE", "CO", "UT"],
    "CO": ["WY", "NE", "KS", "OK", "NM", "AZ", "UT"],
    "NM": ["CO", "AZ", "TX", "OK"],
    "ND": ["MT", "SD", "MN"],
    "SD": ["ND", "MT", "WY", "NE", "IA", "MN"],
    "NE": ["SD", "WY", "CO", "KS", "MO", "IA"],
    "KS": ["NE", "CO", "OK", "MO"],
    "OK": ["KS", "CO", "NM", "TX", "AR", "MO"],
    "TX": ["NM", "OK", "AR", "LA"],
    "MN": ["ND", "SD", "IA", "WI"],
    "IA": ["MN", "SD", "NE", "MO", "IL", "WI"],
    "MO": ["IA", "NE", "KS", "OK", "AR", "TN", "KY", "IL"],
    "AR": ["MO", "OK", "TX", "LA", "MS", "TN"],
    "LA": ["AR", "TX", "MS"],
    "WI": ["MN", "IA", "IL", "MI"],
    "IL": ["WI", "IA", "MO", "KY", "IN", "MI"],
    "MS": ["TN", "AR", "LA", "AL"],
    "MI": ["WI", "IL", "IN", "OH"],
    "IN": ["MI", "IL", "KY", "OH"],
    "OH": ["MI", "IN", "KY", "WV", "PA"],
    "KY": ["OH", "IN", "IL", "MO", "TN", "WV", "VA"],
    "TN": ["KY", "MO", "AR", "MS", "AL", "GA", "NC", "VA"],
    "AL": ["MS", "TN", "GA", "FL"],
    "GA": ["AL", "TN", "NC", "SC", "FL"],
    "FL": ["AL", "GA"],
    "SC": ["NC", "GA"],
    "NC": ["VA", "TN", "GA", "SC"],
    "VA": ["WV", "KY", "TN", "NC", "MD", "DC"],
    "WV": ["OH", "KY", "VA", "MD", "PA"],
    "MD": ["WV", "VA", "PA", "DE"],
    "DE": ["MD", "PA", "NJ"],
    "PA": ["OH", "WV", "MD", "DE", "NJ", "NY"],
    "NJ": ["DE", "PA", "NY"],
    "NY": ["NJ", "PA", "VT", "MA", "CT"],
    "CT": ["NY", "MA", "RI"],
    "RI": ["CT", "MA"],
    "MA": ["RI", "CT", "NY", "VT", "NH"],
    "NH": ["ME", "MA", "VT"],
    "VT": ["NY", "MA", "NH"],
    "ME": ["NH"],
    "HI": [],
    "AK": []
}

# Australia Map Adjacency
    australia_adjacency = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QL"],
    "SA": ["WA", "NT", "QL", "NSW", "VIC"],
    "QL": ["NT", "SA", "NSW"],
    "NSW": ["SA", "QL", "VIC"],
    "VIC": ["SA", "NSW"],
    "TA": []
}


    # Experiment without heuristics
    print("Without Heuristics:")
    print("USA Map:")
    print("Method\t\tBacktracks\tTime")
    for _ in range(5):
        usa_solver = MapColoringSolver(usa_states, usa_adjacency)
        result, backtracks, time_taken = usa_solver.dfs_without_heuristics()
        print("DFS\t\t{}\t\t{:.6f}".format(backtracks, time_taken))

        usa_solver = MapColoringSolver(usa_states, usa_adjacency)
        result, backtracks, time_taken = usa_solver.dfs_forward_checking()
        print("DFS + FC\t{}\t\t{:.6f}".format(backtracks, time_taken))

        usa_solver = MapColoringSolver(usa_states, usa_adjacency)
        result, backtracks, time_taken = usa_solver.dfs_singleton_domains()
        print("DFS + FC + SD\t{}\t\t{:.6f}".format(backtracks, time_taken))

    print("\nAustralia Map:")
    print("Method\t\tBacktracks\tTime")
    for _ in range(5):
        australia_solver = MapColoringSolver(australia_states, australia_adjacency)
        result, backtracks, time_taken = australia_solver.dfs_without_heuristics()
        print("DFS\t\t{}\t\t{:.6f}".format(backtracks, time_taken))

        australia_solver = MapColoringSolver(australia_states, australia_adjacency)
        result, backtracks, time_taken = australia_solver.dfs_forward_checking()
        print("DFS + FC\t{}\t\t{:.6f}".format(backtracks, time_taken))

        australia_solver = MapColoringSolver(australia_states, australia_adjacency)
        result, backtracks, time_taken = australia_solver.dfs_singleton_domains()
        print("DFS + FC + SD\t{}\t\t{:.6f}".format(backtracks, time_taken))


if __name__ == "__main__":
    main()
