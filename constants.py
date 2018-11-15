import vector3d


def cube_indices():
    return (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)


def gravitational_acceleration():
    return vector3d.Vector3D(0, -9800, 0)
