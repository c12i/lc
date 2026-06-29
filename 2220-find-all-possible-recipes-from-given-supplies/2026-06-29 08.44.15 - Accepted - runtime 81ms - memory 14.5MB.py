class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        deps = []
        n = len(recipes)
        recipe_set = set(recipes)

        for i in range(n):
            ri = ingredients[i]
            for j in range(len(ri)):
                if ri[j] in recipe_set:
                    deps.append((recipes[i], ri[j]))

        hm = {recipes[i]: ingredients[i] for i in range(n)}

        graph = defaultdict(list)
        indegree = {recipes[i]: 0 for i in range(n)}

        for dest, src in deps:
            graph[src].append(dest) 
            indegree[dest] += 1

        queue = deque([recipes[i] for i in range(n) if indegree[recipes[i]] == 0])
        available = set(supplies)

        order = []

        while queue:
            recipe = queue.popleft()
            ings = hm[recipe]

            if all(ing in available for ing in ings):
                order.append(recipe)
                available.add(recipe)

            neighbors = graph[recipe] 

            for neigh in neighbors:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        return order
                    