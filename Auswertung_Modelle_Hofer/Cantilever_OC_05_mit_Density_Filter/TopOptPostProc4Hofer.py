
from KratosTools.KratosVisualization \
    import VisualizeMesh, VisualizeModalResults, VisualizeNodalResults, \
        VisualizeElementalResults
import pyvista as pv

# "Gobal" settings
color = "#1F77B4"   # I chose my standard blue, feel free to change
ShowPlot = False    # Plot figures to screen. If false, figures will only be saved. 
WindowSize = [6000, 9000]  # Vertically oriented, for horizontally oriented models [10000, 5000]
                            # These are the maxima on my computer. 
                            # Follow here to see if solution available:
                            # https://github.com/pyvista/pyvista-support/issues/423



meshFig = VisualizeMesh()
meshFig.name = "TopOpt_Cantilever_density_iso"
meshFig.vtkFolder = "."    # in this folder
meshFig.vtkFile = "Cantilever_density.vtu"
meshFig.showPlot = ShowPlot
meshFig.showNumber = False
meshFig.showNodes = False
meshFig.showMesh = True
meshFig.showVolume = True
meshFig.VolumeColor = color
meshFig.WindowSize = WindowSize
meshFig.view =  (1, 1, 1)
meshFig.make()

meshFig.name = "TopOpt_Cantilever_density_iso2"
meshFig.view =  (1, -1, 1)
meshFig.make()

meshFig.name = "TopOpt_Cantilever_density_iso3"
meshFig.view =  (-1, -1, 1)
meshFig.make()

meshFig.name = "TopOpt_Cantilever_density_iso4"
meshFig.view =  (-1, 1, 1)
meshFig.make()


meshFig.name = "TopOpt_Cantilever_density_side1"
meshFig.view =  (1, 0, 0)
meshFig.make()

meshFig.name = "TopOpt_Cantilever_density_side2"
meshFig.view =  (0, 1, 0)
meshFig.make()

meshFig.name = "TopOpt_Cantilever_density_top"
meshFig.view =  (0, 0, 1)
meshFig.make()


# Wireframe plot of mesh
meshFig = VisualizeMesh()
meshFig.name = "TopOpt_Cantilever_density_WireFrame_iso"
meshFig.vtkFolder = "."    # in this folder
meshFig.vtkFile = "Cantilever_density.vtu"
meshFig.showPlot = ShowPlot
meshFig.showNumber = True
meshFig.showNodes = False
meshFig.WindowSize = WindowSize
meshFig.make()
       

# Density plots
densFig = VisualizeElementalResults()
densFig.name = "TopOpt_Cantilever_density_Dens_iso"
densFig.vtkFolder = "."    # in this folder
densFig.vtkFile = "Cantilever_density_VTK0028.vtu"
densFig.showPlot = ShowPlot
densFig.showNumber = False
densFig.showNodes = False
densFig.warpResponse = False
densFig.TransparentVolume = True
densFig.WindowSize = WindowSize
densFig.Responses = ["X_PHYS"]
densFig.BarTitles = ["density\n(normalized)"]
densFig.FileNameAdd = ["density"]
densFig.make()