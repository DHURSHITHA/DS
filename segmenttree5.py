class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.construct_segment_tree(arr, 0, self.n - 1, 0)

    def construct_segment_tree(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return arr[start]
        mid = (start + end) // 2
        self.tree[index] = self.construct_segment_tree(arr, start, mid, 2 * index + 1) + \
                           self.construct_segment_tree(arr, mid + 1, end, 2 * index + 2)
        return self.tree[index]

    def query_range_sum(self, query_start, query_end):
        return self._query_range_sum(0, self.n - 1, query_start, query_end, 0)

    def _query_range_sum(self, start, end, query_start, query_end, index):
        if query_start <= start and query_end >= end:  # Complete overlap
            return self.tree[index]
        if query_end < start or query_start > end:  # No overlap
            return 0
        mid = (start + end) // 2
        return self._query_range_sum(start, mid, query_start, query_end, 2 * index + 1) + \
               self._query_range_sum(mid + 1, end, query_start, query_end, 2 * index + 2)

    def update_value(self, student_index, new_value):
        # Original index in tree: self.n + student_index - 1 is incorrect for this tree structure
        # Calculate the current value from the array
        current_value = self._get_current_value(0, self.n - 1, student_index, 0)
        diff = new_value - current_value
        self._update_value(0, self.n - 1, student_index, diff, 0)

    def _update_value(self, start, end, student_index, diff, index):
        if student_index < start or student_index > end:
            return
        self.tree[index] += diff
        if start != end:
            mid = (start + end) // 2
            self._update_value(start, mid, student_index, diff, 2 * index + 1)
            self._update_value(mid + 1, end, student_index, diff, 2 * index + 2)

    def _get_current_value(self, start, end, student_index, index):
        if start == end:
            return self.tree[index]
        mid = (start + end) // 2
        if student_index <= mid:
            return self._get_current_value(start, mid, student_index, 2 * index + 1)
        else:
            return self._get_current_value(mid + 1, end, student_index, 2 * index + 2)


# Get input from the user
arr = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]
segment_tree = SegmentTree(arr)

print("Initial segment tree:", segment_tree.tree)

# Get query range from the user
query_start, query_end = [int(x) for x in input("Enter the query range (start end) separated by spaces: ").split()]
print("Sum of elements in range [{}, {}]: {}".format(query_start, query_end,
                                                     segment_tree.query_range_sum(query_start, query_end)))

# Get student index and new value from the user
student_index, new_value = [int(x) for x in input("Enter the student index and new value separated by spaces: ").split()]
segment_tree.update_value(student_index, new_value)

print("Segment tree after updating value of student {}: {}".format(student_index, segment_tree.tree))

# Query range sum after update
print("Sum of elements in range [{}, {}]: {}".format(query_start, query_end,
                                                     segment_tree.query_range_sum(query_start, query_end)))
Output:
Enter the array elements separated by spaces: 10 20 30 40 50
Initial segment tree: [150, 60, 90, 30, 30, 40, 50, 10, 20, 0]
Enter the query range (start end) separated by spaces: 1 3
Sum of elements in range [1, 3]: 90
Enter the student index and new value separated by spaces: 2 25
Segment tree after updating value of student 2: [145, 55, 90, 30, 25, 40, 50, 10, 20, 0]
Sum of elements in range [1, 3]: 85
