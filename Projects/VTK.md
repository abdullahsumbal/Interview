# Notes

This contains information about VTK. Copied from
https://lorensen.github.io/VTKExamples/site/Python/

## 1. VTK pipeline

### 1. Source
"Sources" are quite simply the source of data flowing through the visualization pipeline. There are basically two types of sources: Readers, which read data out of files in a wide variety of formats, and Independant Sources, which generate data flow based on input parameters.

### 2. Mapper
Mapper converts data into graphical primitives.
It "map" the data to some sort of a physical manifestation that can be rendered by the rendering engineeg. e.g VtkPolyDataMapper take geometric shapes and converts it into something that is renderable.

### 3. Actors
"Actors" are VTK components that allow for the adjustment and control of the apperarance properties of the physical manifestations of the data as rendered onto the screen. Some of the properties typically controlled via actors are transparency and color mapping. ( The term "actor" comes from analogy with the stage - The actor is a physical representation of the data, "standing" on the "stage" ( appearing in the rendering window ), whose appearance can be modified through lighting, makeup, costumes, etc. ) Another term for actors is "props"; The distinction between actors and props ( if there is any ) is not clear.

### 4. Render
Renderers and Windows represent the end of the VTK pipeline, which users actually see on the screen. In practice there is not generally a lot to do with renderers and windows, with a few notable exceptions:

All actors must be added to a rendering window before they can appear on the screen. Therefore the renderer is usually created first thing in a VTK program, even though it is the end of the data flow pipeline. Then each actor can be added to the renderer as that particular pipeline section is completed.
VTK components do not normally generate their output until requested to do so. Normally this is accomplished by requesting that the rendering window render its results. This will cause the renderer to issue an update( ) request to all if its inputs, which will in turn issue update( ) requests to all of their inputs, and so on back down the pipeline to the sources. If any parameters in the pipeline change, ( e.g. in response to user input through the user interface ), then the renderer window must be requested to re-render before the effects of the parameter adjustment can be seen.
Interactors, which allow users to grab and rotate the rendered data, are typically added along with the renderers and windows.

```
import vtk

# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# create source
source = vtk.vtkSphereSource()
source.SetCenter(0,0,0)
source.SetRadius(5.0)

# mapper
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(source.GetOutput())
else:
    mapper.SetInputConnection(source.GetOutputPort())

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# assign actor to the renderer
ren.AddActor(actor)

# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
```
