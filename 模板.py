# recursion 调用自身
def f()
{
     if(符合边界条件)
    {
       ///////
        return;
    }
    
     //某种形式的调用
     f();
}

# 遍历
def dfs(int 当前状态)
	{
	      if(当前状态为边界状态)
	      {
	        记录或输出
	        return;
	      }
	      for(i=0;i<n;i++)		//横向遍历解答树所有子节点
	     {
	           //扩展出一个子状态。
	           修改了全局变量
	           if(子状态满足约束条件)
	            {
	              dfs(子状态)
	           }
	            恢复全局变量//回溯部分
	        }
	}


# backtrack 1
ans = []
def backtrack1(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()

# backtrack 2
def backtrack2(start_index, [...additional states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [...additional states]):
        if additional states: 
            update([...additional states])
        ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
        if additional states: 
            revert([...additional states])
    return ans


# 假如参与递归的参数不是通过传参形式的方式进入递归的话，那么一定要做好数据恢复。


def mono_stack(insert_entries):
    stack = []
    for entry in insert_entries:
        while stack and stack[-1] <= entry:
            stack.pop()
            # Do something with the popped item here
        stack.append(entry)


def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans

def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window):        # update left until window is valid again
            remove input[left] from window
            left += 1
        ans = max(ans, window)        # window is guaranteed to be valid here
    return ans

def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)      # window is guaranteed to be valid here
            remove input[left] from window
            left += 1
    return ans


# Trie
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s, idx):
        # idx: index of the current character in s
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx + 1)

# Union Find
class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)

def find_indegree(graph):
    indegree = { node: 0 for node in graph }  # dict
    for node in graph:
        for neighbor in graph[node]:
            indgree[neighbor] += 1
    return indegree

#%

def topo_sort(graph):
    res = []
    q = deque()
    indegree = find_indegree(graph)
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return res if len(graph) == len(res) else None
