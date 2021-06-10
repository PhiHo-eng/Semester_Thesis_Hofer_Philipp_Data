import pyvista as pv
from pyvista import examples
import numpy as np

pv.set_plot_theme("document")
mesh = pv.UnstructuredGrid("Viertel_model.vtu")

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh.copy(),  show_edges=False,  color="#1F77B4")
plotter.add_mesh(mesh.copy(), color="k",  style='wireframe')
plotter.show(screenshot="FeMesh.png", interactive=0, 
             auto_close=1)
res = np.logspace(1, 10, 10)
for resi in res: 
    plotter = pv.Plotter(window_size=[int(resi/2), int(resi)], 
                         off_screen=True, lighting="three_lights")
    print([int(resi/2), int(resi)])
    plotter.add_mesh(mesh.copy(),  show_edges=False,  color="#1F77B4")
    plotter.add_mesh(mesh.copy(), color="k",  style='wireframe')
    plotter.show(screenshot="FeMesh"+str(int(resi))+".png", interactive=0, 
                 auto_close=1)
