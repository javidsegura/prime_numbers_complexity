
import matplotlib.pyplot as plt

# Provided data
data = {
1: 9.5367431640625e-07,
2: 1.1920928955078125e-06,
3: 2.1457672119140625e-06,
4: 1.9073486328125e-06,
5: 3.0994415283203125e-06,
6: 2.86102294921875e-06,
7: 4.0531158447265625e-06,
8: 5.0067901611328125e-06,
9: 5.9604644775390625e-06,
10: 5.245208740234375e-06,
11: 6.9141387939453125e-06,
12: 7.867813110351562e-06,
13: 8.106231689453125e-06,
14: 8.106231689453125e-06,
15: 7.867813110351562e-06,
16: 9.059906005859375e-06,
17: 1.0013580322265625e-05,
18: 1.0967254638671875e-05,
19: 1.1205673217773438e-05,
20: 1.1920928955078125e-05,
21: 1.2159347534179688e-05,
22: 1.3113021850585938e-05,
23: 1.2636184692382812e-05,
24: 1.4066696166992188e-05,
25: 1.4781951904296875e-05,
26: 1.5735626220703125e-05,
27: 1.5974044799804688e-05,
28: 1.6927719116210938e-05,
29: 1.811981201171875e-05,
}

# Splitting the data into x (primes) and y (time in )
x = list(data.keys())
y = list(data.values())

# Creating the plot
plt.figure(figsize=(12, 6))
plt.plot(x, y, marker='o', color='m', linestyle='-')
plt.title('Time Complexity of bestallprime Function')
plt.xlabel('Prime Number')
plt.ylabel('Time ()')
plt.grid(True)
plt.show()
