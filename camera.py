import vector3d


class Camera(object):
    def __init__(self):
        self.translation = vector3d.Vector3D(0.0, 0.0, 1.0)

        self.rotation_magnitude = vector3d.Vector3D(0.0, 0.0, 0.0)
        self.rotation_direction = vector3d.Vector3D(0.0, 0.0, 0.0)

        self.translation_bool = False
        self.rotation_bool = False

        self.speed = 1.0

    def reset_translation(self):
        self.translation = vector3d.Vector3D(0.0, 0.0, 1.0)

        self.translation_bool = False

    def reset_rotation(self):
        self.rotation_magnitude = vector3d.Vector3D(0.0, 0.0, 0.0)
        self.rotation_direction = vector3d.Vector3D(0.0, 0.0, 0.0)

        self.rotation_bool = False
