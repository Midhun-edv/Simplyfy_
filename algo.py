# Define the available tickets as a dictionary with cities as keys and destinations as values.
tickets = {
    'Paris': 'Skopje',
    'Zurich': 'Amsterdam',
    'Prague': 'Zurich',
    'Barcelona': 'Berlin',
    'Kiev': 'Prague',
    'Skopje': 'Paris',
    'Amsterdam': 'Barcelona',
    'Berlin': 'Kiev',
    'Berlin': 'Amsterdam',
}

# Function to find the route using depth-first search (DFS)
def find_route(start_city, tickets):
    visited = set()
    route = []

    def dfs(city):
        visited.add(city)
        route.append(city)

        if city not in tickets:
            return True

        destination = tickets[city]

        if destination not in visited:
            if dfs(destination):
                return True

        route.pop()
        visited.remove(city)
        return False

    if dfs(start_city):
        return route
    else:
        return None

# Start the search from Kiev (as you mentioned your son started from Kiev)
son_route = find_route('Kiev', tickets)

if son_route:
    print("Your son's route was:", son_route)
else:
    print("No valid route found.")

