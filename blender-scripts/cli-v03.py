import bpy
import math

# ==========================================================
# CL1 Single-Layer MEA Generator v03
# Blender 4.2.0
# ==========================================================

# -----------------------------
# Clear scene
# -----------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Remove unused materials
for myMat in list(bpy.data.materials):
    bpy.data.materials.remove(myMat)

# -----------------------------
# Parameters
# -----------------------------
mySpacing = 0.35
myRadius = 0.065
myThickness = 0.025

mySubstrateSize = 3.6
mySubstrateThickness = 0.03

myRowWidths = [6,8,8,8,8,8,8,6]
myRefRow = 4
myRefCol = 0

# -----------------------------
# Materials
# -----------------------------
def myCreateGlassMaterial():
    myMat = bpy.data.materials.new("Glass")
    myMat.use_nodes = True
    myNodes = myMat.node_tree.nodes
    myBSDF = myNodes["Principled BSDF"]

    myBSDF.inputs["Base Color"].default_value = (0.92,0.96,1.0,1)
    myBSDF.inputs["Transmission Weight"].default_value = 1.0
    myBSDF.inputs["Roughness"].default_value = 0.05
    myBSDF.inputs["IOR"].default_value = 1.45

    return myMat


def myCreateElectrodeMaterial(myName, myBaseColor):
    myMat = bpy.data.materials.new(myName)
    myMat.use_nodes = True
    myNodes = myMat.node_tree.nodes

    myBSDF = myNodes["Principled BSDF"]
    myEmission = myNodes.new("ShaderNodeEmission")
    myMix = myNodes.new("ShaderNodeAddShader")
    myOutput = myNodes["Material Output"]

    myBSDF.inputs["Base Color"].default_value = myBaseColor
    myBSDF.inputs["Metallic"].default_value = 1.0
    myBSDF.inputs["Roughness"].default_value = 0.15

    myEmission.inputs["Color"].default_value = myBaseColor
    myEmission.inputs["Strength"].default_value = 0.0

    myMat.node_tree.links.new(myBSDF.outputs["BSDF"], myMix.inputs[0])
    myMat.node_tree.links.new(myEmission.outputs["Emission"], myMix.inputs[1])
    myMat.node_tree.links.new(myMix.outputs[0], myOutput.inputs["Surface"])

    return myMat


myGlass = myCreateGlassMaterial()
myGold = myCreateElectrodeMaterial(
    "GoldElectrode",
    (1.0,0.78,0.15,1)
)

myReference = myCreateElectrodeMaterial(
    "ReferenceElectrode",
    (0.95,0.95,0.95,1)
)

# -----------------------------
# Parent object
# -----------------------------
myParent = bpy.data.objects.new("MEA_Layer", None)
bpy.context.collection.objects.link(myParent)

# -----------------------------
# Substrate
# -----------------------------
bpy.ops.mesh.primitive_cube_add(location=(0,0,-mySubstrateThickness/2))
mySubstrate = bpy.context.object
mySubstrate.name = "MEA_Substrate"
mySubstrate.scale = (
    mySubstrateSize/2,
    mySubstrateSize/2,
    mySubstrateThickness/2
)
mySubstrate.data.materials.append(myGlass)
mySubstrate.parent = myParent

# -----------------------------
# Electrode creation
# -----------------------------
myElectrodeObjects = []
myCount = 0

for myRow,myWidth in enumerate(myRowWidths):

    myY = (len(myRowWidths)-1)/2 * mySpacing - myRow * mySpacing
    myXOffset = -(myWidth-1)/2 * mySpacing

    for myCol in range(myWidth):

        myX = myXOffset + myCol * mySpacing

        myIsRef = (
            myRow == myRefRow and
            myCol == myRefCol
        )

        myR = myRadius * (1.4 if myIsRef else 1.0)

        bpy.ops.mesh.primitive_cylinder_add(
            vertices=48,
            radius=myR,
            depth=myThickness,
            location=(myX,myY,myThickness/2)
        )

        myObj = bpy.context.object

        # Bevel for nicer highlights
        myBevel = myObj.modifiers.new(
            name="Bevel",
            type='BEVEL'
        )
        myBevel.width = 0.005
        myBevel.segments = 3

        bpy.ops.object.shade_smooth()

        if myIsRef:
            myObj.name = "Reference_Electrode"
            myObj.data.materials.append(myReference)
        else:
            myObj.name = f"Electrode_{myCount+1:02d}"
            myObj.data.materials.append(myGold)
            myCount += 1

        myObj.parent = myParent
        myElectrodeObjects.append(myObj)

# -----------------------------
# Camera
# -----------------------------
bpy.ops.object.camera_add(location=(3.2,-3.6,2.4))
myCamera = bpy.context.object
myCamera.rotation_euler = (
    math.radians(62),
    0,
    math.radians(42)
)
bpy.context.scene.camera = myCamera

# -----------------------------
# Lighting
# -----------------------------
bpy.ops.object.light_add(
    type='AREA',
    location=(0,-2.5,3.5)
)
myLight = bpy.context.object
myLight.data.energy = 3000
myLight.data.shape = 'RECTANGLE'
myLight.data.size = 4.0
myLight.data.size_y = 4.0

bpy.ops.object.light_add(
    type='AREA',
    location=(2,2,1.5)
)
myFill = bpy.context.object
myFill.data.energy = 800
myFill.data.size = 2.5

# -----------------------------
# World background
# -----------------------------
myWorld = bpy.context.scene.world
myWorld.use_nodes = True
myBackground = myWorld.node_tree.nodes["Background"]
myBackground.inputs["Color"].default_value = (0.02,0.02,0.025,1)
myBackground.inputs["Strength"].default_value = 0.8

# -----------------------------
# Render settings
# -----------------------------
myScene = bpy.context.scene
myScene.render.engine = 'CYCLES'
myScene.cycles.samples = 128
myScene.render.resolution_x = 1920
myScene.render.resolution_y = 1080

# -----------------------------
# Store electrode list for later animation
# -----------------------------
myParent["electrode_count"] = myCount

print(f"CL1 MEA created: {myCount} active electrodes + reference electrode")
