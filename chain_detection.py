import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

# Generate random points that are uniform
realx = np.random.uniform(-250, 250, 500)
realy = np.random.uniform(-250, 250, 500)
realrad = np.random.rand(500) * 20

# Put them together
realpoints = np.column_stack((realx, realy, realrad))

plt.hist(realrad, bins=100)
plt.grid()
plt.title("Frequency of Crater Radii")
plt.ylabel("Count")
plt.xlabel("Radius (Pixels)")
plt.show()

# SET UP KD-Tree (only use x, y for spatial queries)
point_tree = cKDTree(realpoints[:, :2])

plt.figure(figsize=(5, 5))
plt.title("Pre-Scan Identified Craters")
plt.xlabel("Longitude (º)")
plt.ylabel("Latitude (º)")
plt.scatter(realx, realy)
plt.show()

def craters_in_line(origpoint, theta, distance_lim):
    # Direction of line
    dirvec = np.array([np.cos(np.radians(theta)), np.sin(np.radians(theta))])
    # Possible craters in chain
    chain = [origpoint.copy()]
    indices = point_tree.query_ball_point(origpoint[:2], distance_lim)
    for idx in indices:
        point = realpoints[idx]
        if np.array_equal(point, origpoint):
            continue
        crater_vect = point[:2] - origpoint[:2]
        l_proj = np.dot(crater_vect, dirvec)
        proj_vect = l_proj * dirvec
        orth_dist = np.linalg.norm(crater_vect - proj_vect)
        if orth_dist <= distance_lim:
            chain.append(point)
    return chain

# Parameter and creation of all chains array
distlimval = 12
allchains = set()
dthet = 150  # Number of steps in theta
thetas = np.linspace(0, 360, dthet)

for origpoint in realpoints:
    for t in thetas:
        chain = craters_in_line(origpoint, t, distlimval)
        if len(chain) > 2:
            allchains.add(tuple(map(tuple, chain)))

print("CRATER CHAIN DETECTION INFO:")
print("AMOUNT OF DETECTED CHAINS:", len(allchains))
listofchains = list(allchains)
print(listofchains[0])
print(np.array(listofchains[0]).shape)

colors = ['red', 'black', 'green', 'orange', 'purple']
plt.figure(figsize=(15, 15))
plt.title("Post-Scan Identified Chains")
plt.xlabel("Longitude (º)")
plt.ylabel("Latitude (º)")
plt.scatter(realx, realy, s=realrad**2)

for i in range(len(allchains)):
    chain_points = np.array(listofchains[i])
    plt.scatter(chain_points[:, 0], chain_points[:, 1], s=chain_points[:, 2]**2, c=colors[i % len(colors)])

plt.show()
