# LeetCode Summary

# Table of Contents

- [Array](#array)
- [Binary Search](#binary_search)
- [Breadth First Search](#breadth_first_search)
- [C++ Cheatsheet](#cpp_cheatsheet)
- [Depth First Search](#depth_first_search)
- [Dynamic Programming](#dynamic_programming)
- [Hash Table](#hash_table)
- [Linked List](#linked_list)
- [String](#string)
- [SQL Relevance](#sql)
- [Sweep Line](#sweep_line)
- [Two Pointers](#two_pointers)
- [Python Solutions](#python_solutions)

# <a name='array'>Array</a>

**Problems:**

- [1. Two Sum](/Array/1.%20Two%20Sum.cpp)
- [53. Maximum Subarray](/Array/53.%20Maximum%20Subarray.cpp)
- [88. Merge Sorted Array](/Array/88.%20Merge%20Sorted%20Array.cpp)
- [121. Best Time to Buy and Sell Stock](/Array/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.cpp)
- [118. Pascal's Triangle](/Array/118.%20Pascal's%20Triangle.cpp)
- [217. Contains Duplicate](/Array/217.%20Contains%20Duplicate.cpp)
- [566. Reshape the Matrix](/Array/566.%20Reshape%20the%20Matrix.cpp)
- [724. Find Pivot Index](/Array/724.%20Find%20Pivot%20Index.cpp)
- [1480. Running Sum of 1d Array](/Array/1480.%20Running%20Sum%20of%201d%20Array.cpp)

# <a name='hash_table'>Hash Table</a>

**Problems:** 

- [205. Isomorphic Strings](/String/205.%20Isomorphic%20Strings.cpp)
- [242. Valid Anagram](/Hash%20Table/242.%20Valid%20Anagram.cpp)
- [299. Bulls and Cows](/Hash%20Table/299.%20Bulls%20and%20Cows.cpp)
- [383. Ransom Note](/Hash%20Table/383.%20Ransom%20Note.cpp)
- [387. First Unique Character in a String](/Hash%20Table/387.%20First%20Unique%20Character%20in%20a%20String.cpp)
- [389. Find the Difference](/Hash%20Table/389.%20Find%20the%20Difference.cpp)

# <a name='linked_list'>Linked List</a>

**Problems:**

- [21. Merge Two Sorted Lists](/Linked%20List/21.%20Merge%20Two%20Sorted%20Lists.cpp)
- [83. Remove Duplicates from Sorted List](/Linked%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.cpp)
- [141. Linked List Cycle](/Linked%20List/141.%20Linked%20List%20Cycle.cpp)
- [203. Remove Linked List Elements](/Linked%20List/203.%20Remove%20Linked%20List%20Elements.cpp)

# <a name='binary_search'>Binary Search</a>

**Generic Notes**

The template for *binary search*:

```cpp
// Fill the spot marked with ...
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;  // initial condition

    while(...) {  // termination condition
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...  // proceed condition
        } else if (nums[mid] < target) {
            left = ...  // proceed condition
        } else if (nums[mid] > target) {
            right = ...  // proceed condition
        }
    }
    return ...; // return variable
}
```

| Scenario Label | Initial Condition | Termination Condition | Proceed Condition                                    | Return Variable | Example Problems | Scenario                                    |
|:--------------:|:-----------------:|:---------------------:|:----------------------------------------------------:|:---------------:|:----------------:|:-------------------------------------------:|
| 1              | [0, len-1]        | left<=right           | return mid;<br/>left=mid+1;<br/>right=mid-1;         | -1              | 704              | Find a single number in a sorted array      |
| 2              | [0, len)          | left < right          | right=mid;<br/>left = mid + 1;<br/>right = mid       | left            |                  | Find the 1st occurence of a certain number  |
| 3              | [0, len)          | left < right          | left = mid + 1;<br/>left = mid + 1;<br/>right = mid; | left - 1        |                  | Find the last occurence of a certain number |
| 4              | [0, len]          | left < right          | pass;<br/>left = mid + 1;<br/>right = mid            | right           | 852              | Find the peak in a mountain array           |

**Problems:**

- [33. Search in Rotated Sorted Array](/Binary%20Search/33.%20Search%20in%20Rotated%20Sorted%20Array.cpp)
- [34. Find First and Last Position of Element in Sorted Array.cpp](/Binary%20Search/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.cpp)
- [35. Search Insert Position](/Binary%20Search/35.%20Search%20Insert%20Position.cpp)
- [69. Sqrt(x)](/Binary%20Search/69.%20Sqrt(x).cpp)
- [74. Search a 2D Matrix](/Binary%20Search/74.%20Search%20a%202D%20Matrix.cpp)
- [153. Find Minimum in Rotated Sorted Array](/Binary%20Search/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.cpp)
- [167. Two Sum II - Input Array Is Sorted](/Binary%20Search/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.cpp)
- [209. Minimum Size Subarray Sum](/Binary%20Search/209.%20Minimum%20Size%20Subarray%20Sum.cpp)
- [278. First Bad Version](/Binary%20Search/278.%20First%20Bad%20Version.cpp)
- [350. Intersection of Two Arrays II](/Binary%20Search/350.%20Intersection%20of%20Two%20Arrays%20II.cpp)
- [367. Valid Perfect Square](/Binary%20Search/367.%20Valid%20Perfect%20Square.cpp)
- [374. Guess Number Higher or Lower](/Binary%20Search/374.%20Guess%20Number%20Higher%20or%20Lower.cpp)
- [441. Arranging Coins](/Binary%20Search/441.%20Arranging%20Coins.cpp)
- [611. Valid Triangle Number](/Binary%20Search/611.%20Valid%20Triangle%20Number.cpp)
- [633. Sum of Square Numbers](/Binary%20Search/633.%20Sum%20of%20Square%20Numbers.cpp)
- [704. Binary Search](/Binary%20Search/704%20Binary%20Search.cpp)
- [744. Find Smallest Letter Greater Than Target](/Binary%20Search/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target.cpp)
- [852. Peak Index in a Mountain Array](/Binary%20Search/852.%20Peak%20Index%20in%20a%20Mountain%20Array.cpp)
- [1337. The K Weakest Rows in a Matrix](/Binary%20Search/1337.%20The%20K%20Weakest%20Rows%20in%20a%20Matrix.cpp)
- [1346. Check If N and Its Double Exist](/Binary%20Search/1346.%20Check%20If%20N%20and%20Its%20Double%20Exist.cpp)
- [1351. Count Negative Numbers in a Sorted Matrix](/Binary%20Search/1351.%20Count%20Negative%20Numbers%20in%20a%20Sorted%20Matrix.cpp)
- [1385. Find the Distance Value Between Two Arrays](/Binary%20Search/1385.%20Find%20the%20Distance%20Value%20Between%20Two%20Arrays.cpp)
- [1539. Kth Missing Positive Number](/Binary%20Search/1539.%20Kth%20Missing%20Positive%20Number.cpp)
- [1608. Special Array With X Elements Greater Than or Equal X](/Binary%20Search/1608.%20Special%20Array%20With%20X%20Elements%20Greater%20Than%20or%20Equal%20X.cpp)
- [1855. Maximum Distance Between a Pair of Values](/Binary%20Search/1855.%20Maximum%20Distance%20Between%20a%20Pair%20of%20Values.cpp)

# <a name='sql'>SQL Relevance</a>

**Generic Notes**:

Order of Statements When Writing a Query:

\<SELECT\>  \<FROM\>  \<JOINs\> \<WHERE\> \<GROUP BY\> \<HAVING\> \<ORDER BY\> \<LIMIT\> \<OFFSET\>

Order of Execution:

\<FROM\> \<ON\> \<JOIN\> \<WHERE\> \<GROUP BY\> \<HAVING\> \<SELECT\> \<DISTINCT\> \<ORDER BY\>

**Problems:**

- [175. Combine Two Tables](/SQL%20Practice/175.%20Combine%20Two%20Tables.sql)
- [176. Second Highest Salary](/SQL%20Practice/176.%20Second%20Highest%20Salary.sql)
- [182. Duplicate Emails](/SQL%20Practice/182.%20Duplicate%20Emails.sql)
- [183. Customers Who Never Order](/SQL%20Practice/183.%20Customers%20Who%20Never%20Order.sql)
- [196. Delete Duplicate Emails](/SQL%20Practice/196.%20Delete%20Duplicate%20Emails.sql)
- [197. Rising Temperature](/SQL%20Practice/197.%20Rising%20Temperature.sql)
- [511. Game Play Analysis I](/SQL%20Practice/511.%20Game%20Play%20Analysis%20I.sql)
- [584. Find Customer Referee](/SQL%20Practice/584.%20Find%20Customer%20Referee.sql)
- [586. Customer Placing the Largest Number of Orders](/SQL%20Practice/586.%20Customer%20Placing%20the%20Largest%20Number%20of%20Orders.sql)
- [595. Big Countries](/SQL%20Practice/595.%20Big%20Countries.sql)
- [607. Sales Person](/SQL%20Practice/607.%20Sales%20Person.sql)
- [608. Tree Node](/SQL%20Practice/608.%20Tree%20Node.sql)
- [627. Swap Salary](/SQL%20Practice/627.%20Swap%20Salary.sql)
- [1050. Actors and Directors Who Cooperated At Least](/SQL%20Practice/1050.%20Actors%20and%20Directors%20Who%20Cooperated%20At%20Least%20Three%20Times.sql)
- [1084. Sales Analysis III](/SQL%20Practice/1084.%20Sales%20Analysis%20III.sql)
- [1141. User Activity for the Past 30 Days I](/SQL%20Practice/1141.%20User%20Activity%20for%20the%20Past%2030%20Days%20I.sql)
- [1148. Article Views I](/SQL%20Practice/1148.%20Article%20Views%20I.sql)
- [1158. Market Analysis I](/SQL%20Practice/1158.%20Market%20Analysis%20I.sql)
- [1393. Capital GainLoss](/SQL%20Practice/1393.%20Capital%20GainLoss.sql)
- [1407. Top Travellers](/SQL%20Practice/1407.%20Top%20Travellers.sql)
- [1484. Group Sold Products By The Date](/SQL%20Practice/1484.%20Group%20Sold%20Products%20By%20The%20Date.sql)
- [1527. Patients With a Condition](/SQL%20Practice/1527.%20Patients%20With%20a%20Condition.sql)
- [1587. Bank Account Summary II](/SQL%20Practice/1587.%20Bank%20Account%20Summary%20II.sql)
- [1581. Customer Who Visited but Did Not Make Any Transactions](/SQL%20Practice/1581.%20Customer%20Who%20Visited%20but%20Did%20Not%20Make%20Any%20Transactions.sql)
- [1667. Fix Names in a Table](/SQL%20Practice/1667.%20Fix%20Names%20in%20a%20Table.sql)
- [1693. Daily Leads and Partners](/SQL%20Practice/1693.%20Daily%20Leads%20and%20Partners.sql)
- [1741. Find Total Time Spent by Each Employee](/SQL%20Practice/1741.%20Find%20Total%20Time%20Spent%20by%20Each%20Employee.sql)
- [1729. Find Followers Count](/SQL%20Practice/1729.%20Find%20Followers%20Count.sql)
- [1757. Recyclable and Low Fat Products](/SQL%20Practice/1757.%20Recyclable%20and%20Low%20Fat%20Products.sql)
- [1795. Rearrange Products Table](/SQL%20Practice/1795.%20Rearrange%20Products%20Table.sql)
- [1873. Calculate Special Bonus](/SQL%20Practice/1873.%20Calculate%20Special%20Bonus.sql)
- [1890. The Latest Login in 2020](/SQL%20Practice/1890.%20The%20Latest%20Login%20in%202020.sql)
- [1965. Employees With Missing Information](/SQL%20Practice/1965.%20Employees%20With%20Missing%20Information.sql)

# <a name='sweep_line'>Sweep Line</a>

- [56. Merge Intervals](/Sweep%20Line/56.%20Merge%20Intervals.cpp)
- [57. Insert Interval](/Sweep%20Line/57.%20Insert%20Interval.cpp)
- [218. The Skyline Problem](/Sweep%20Line/218.%20The%20Skyline%20Problem.cpp)
- [252. Meeting Rooms](/Sweep%20Line/252.%20Meeting%20Rooms.cpp)
- [253. Meeting Rooms II](/Sweep%20Line/253.%20Meeting%20Rooms%20II.cpp)
- [352. Data Stream as Disjoint Intervals](/Sweep%20Line/352.%20Data%20Stream%20as%20Disjoint%20Intervals.cpp)
- [435. Non-overlapping Intervals](/Sweep%20Line/435.%20Non-overlapping%20Intervals.cpp)
- [759. Employee Free Time](/Sweep%20Line/759.%20Employee%20Free%20Time.cpp)
- [986. Interval List Intersections](/Sweep%20Line/986.%20Interval%20List%20Intersections.cpp)
- [1229. Meeting Scheduler](/Sweep%20Line/1229.%20Meeting%20Scheduler.cpp)
- [1272. Remove Interval](/Sweep%20Line/1272.%20Remove%20Interval.cpp)
- [1288. Remove Covered Intervals](/Sweep%20Line/1288.%20Remove%20Covered%20Intervals.cpp)

# <a name='breadth_first_searchh'>Breadth First Search</a>

- [102. Binary Tree Level Order Traversal](/Breadth%20First%20Search/102.%20Binary%20Tree%20Level%20Order%20Traversal.cpp)
- [103. Binary Tree Zigzag Level Order Traversal](/Breadth%20First%20Search/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal.cpp)
- [104. Maximum Depth of Binary Tree](/Breadth%20First%20Search/104.%20Maximum%20Depth%20of%20Binary%20Tree.cpp)
- [111. Minimum Depth of Binary Tree](/Breadth%20First%20Search/111.%20Minimum%20Depth%20of%20Binary%20Tree.cpp)
- [127. Word Ladder](/Breadth%20First%20Search/127.%20Word%20Ladder.cpp)
- [207. Course Schedule](/Breadth%20First%20Search/207.%20Course%20Schedule.cpp)
- [210. Course Schedule II](/Breadth%20First%20Search/210.%20Course%20Schedule%20II.cpp)
- [490. The Maze](/Breadth%20First%20Search/490.%20The%20Maze.cpp)
- [505. The Maze II](/Breadth%20First%20Search/505.%20The%20Maze%20II.cpp)

# <a name='depth_first_search'>Depth First Search</a>

- [37. Sudoku Solver](/Depth%20First%20Search/37.%20Sudoku%20Solver.cpp)
- [46. Permutations](/Depth%20First%20Search/46.%20Permutations.cpp)
- [47. Permutations II](/Depth%20First%20Search/47.%20Permutations%20II.cpp)
- [51. N-Queens](/Depth%20First%20Search/51.%20N-Queens.cpp)
- [78. Subsets](/Depth%20First%20Search/78.%20Subsets.cpp)
- [90. Subsets II](/Depth%20First%20Search/90.%20Subsets%20II.cpp)
- [94. Binary Tree Inorder Traversal](/Depth%20First%20Search/94.%20Binary%20Tree%20Inorder%20Traversal.cpp)

# <a name='dynamic_programming'><Dynamic Programming></a>
- [392. Is Subsequence](/Dynamic%20Programming/392.%20Is%20Subsequence.cpp)

# <a name='two_pointers'>Two Pointers</a>

- [905. Sort Array By Parity](/Two%20Pointers/905.%20Sort%20Array%20By%20Parity.cpp)

# <a name='divide_and_conquer'>Divide Conquer</a>
- [111. Minimum Depth of Binary Tree](/Divide%20and%20Conquer/)

# <a name='cpp_cheatsheet'>C++ Cheatsheet</a>

- [STL string](/Cpp%20Cheatsheet/string.cpp)
- [STL unordered_map](/Cpp%20Cheatsheet/unordered_map.cpp)
- [STL unordered_set](/Cpp%20Cheatsheet/unordered_set.cpp)
- [STL vector](/Cpp%20Cheatsheet/vector.cpp)
- [STL algorithm](/Cpp%20Cheatsheet/algorithm.cpp)
- [STL priority_queue](/Cpp%20Cheatsheet/priority_queue.cpp)
- [STL queue](/Cpp%20Cheatsheet/queue.cpp)
- [Dijkstra algorithm](/Cpp%20Cheatsheet/dijkstra_algorithm.cpp)

# <a name='python_solutions'>Python Solutions</a>

- [111. Minimum Depth of Binary Tree](/Python%20Solutions/111.%20Minimum%20Depth%20of%20Binary%20Tree.py)
- [114. Flatten Binary Tree to Linked List](/Python%20Solutions/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List.py)
- [173. Binary Search Tree Iterator](/Python%20Solutions/173.%20Binary%20Search%20Tree%20Iterator.py)
- [235. Lowest Common Ancestor of a Binary Search Tree](/Python%20Solutions/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.py)
- [236. Lowest Common Ancestor of a Binary Tree](/Python%20Solutions/236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.py)
- [257. Binary Tree Paths](/Python%20Solutions/257.%20Binary%20Tree%20Paths.py)
- [269. Alien Dictionary](./Python%20Solutions/269.%20Alien%20Dictionary.py)
- [270. Closest Binary Search Tree Value](/Python%20Solutions/270.%20Closest%20Binary%20Search%20Tree%20Value.py)
- [297. Serialize and Deserialize Binary Tree](/Python%20Solutions/297.%20Serialize%20and%20Deserialize%20Binary%20Tree.py)
- [450. Delete Node in a BST](/Python%20Solutions/450.%20Delete%20Node%20in%20a%20BST.py)
- [501. Find Mode in Binary Search Tree](/Python%20Solutions/501.%20Find%20Mode%20in%20Binary%20Search%20Tree.py)
- [701. Insert into a Binary Search Tree](/Python%20Solutions/701.%20Insert%20into%20a%20Binary%20Search%20Tree.py)
- [1644. Lowest Common Ancestor of a Binary Tree II](/Python%20Solutions/1644.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II.py)
- [1650. Lowest Common Ancestor of a Binary Tree III](/Python%20Solutions/1650.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III.py)
- [1676. Lowest Common Ancestor of a Binary Tree IV](/Python%20Solutions/1676.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20IV.py)