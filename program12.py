gps = (18.5204, 73.8567)

print("Original GPS Coordinates:", gps)

print("\n--- Indexing ---")
print("Latitude:", gps[0])
print("Longitude:", gps[1])

print("\n--- Slicing ---")
print("First coordinate:", gps[:1])
print("Second coordinate:", gps[1:])
print("Complete tuple:", gps[:])

print("\n--- Negative Indexing ---")
print("Latitude:", gps[-2])
print("Longitude:", gps[-1])

print("\n---- Tuple Unpacking ----")

latitude, longitude = gps

print("Unpacking Latitude:", latitude)
print("Unpacked Longitude:", longitude)

print("\n--- Built-in Functions ---")

print("Number of coordinates:", len(gps))
print("Smallest coordinate value:", min(gps))
print("Largest coordinate value:", max(gps))
print("Sum of coordinate values:", sum(gps))

print("\n--- Immutability ---")

gps[0] = 19.0760

print("Tuple cannot be modified!")
print("GPS coordinates remain:", gps)