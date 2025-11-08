A, B, C, X = map(int, input().split())

cuboid_volume = A * B * C
cube_volume = X ** 3

if cuboid_volume > cube_volume:
    print("Cuboid")
elif cube_volume > cuboid_volume:
    print("Cube")
else:
    print("Equal")
