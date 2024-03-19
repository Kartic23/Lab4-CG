"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.garfo import Garfo
from core.matrix import Matrix
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from math import radians


class Example(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        self.geometry = Garfo()
        # material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        self.material = SurfaceMaterial(property_dict={"useVertexColors": True})
        # material = SurfaceMaterial(
        #     property_dict= {
        #         "useVertexColors": True,
        #         "wireframe": True,
        #         "lineWidth": 8
        #     }
        # )
        self.mesh = Mesh(self.geometry, self.material)
        self.scene.add(self.mesh)
        self.angle_step = radians(1)  # define o ângulo de rotação para 10 graus

    def update(self):

        if self.input.is_key_pressed('w'):
            self.camera.rotate_x(-self.angle_step)
            self.camera.update_view_matrix()
        if self.input.is_key_pressed('s'):
            self.camera.rotate_x(self.angle_step)
            self.camera.update_view_matrix()

        if self.input.is_key_pressed('e'):
            self.camera.rotate_y(-self.angle_step)
            self.camera.update_view_matrix()
        if self.input.is_key_pressed('d'):
            self.camera.rotate_y(self.angle_step)
            self.camera.update_view_matrix()

        if self.input.is_key_pressed('r'):
            self.camera.rotate_z(-self.angle_step)
            self.camera.update_view_matrix()
        if self.input.is_key_pressed('f'):
            self.camera.rotate_z(self.angle_step)
            self.camera.update_view_matrix()
        
        if self.input.is_key_pressed('u'):
            self.mesh.rotate_x(0.02514)
        if self.input.is_key_pressed('j'):
            self.mesh.rotate_x(-0.02514)
        
        if self.input.is_key_pressed('i'):
            self.mesh.rotate_y(0.02514)
        if self.input.is_key_pressed('k'):
            self.mesh.rotate_y(-0.02514)

        if self.input.is_key_pressed('o'):
            self.mesh.rotate_z(0.02514)
        if self.input.is_key_pressed('l'):
            self.mesh.rotate_z(-0.02514)

        if self.input.is_key_pressed('z'):
            self.mesh.scale(1.01, True)
        if self.input.is_key_pressed('x'):
            self.mesh.scale(0.99, True)


        if self.input.is_key_pressed('n'):
            self.camera = Camera(aspect_ratio=800/600)
            self.camera.set_position([0, 0, 4])

        if self.input.is_key_pressed('m'):
            self.scene.remove(self.mesh)
            self.geometry = Garfo()
            self.material = SurfaceMaterial(property_dict={"useVertexColors": True})
            self.mesh = Mesh(self.geometry, self.material)
            self.scene.add(self.mesh)

        


 


           
       
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
