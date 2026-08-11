import bpy
import math

# ==========================================================
# CL1 Single-Layer MEA Generator & Animator v04
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
# Animation Settings
# -----------------------------
myFps = 30
bpy.context.scene.render.fps = myFps
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 300  # 10-second loop[cite: 1]

# -----------------------------
# Materials
# -----------------------------
def myCreateGlassMaterial():
    myMat = bpy.data.materials.new("Glass")
    myMat.use_nodes = True
    myNodes = myMat.node_tree.nodes
    myBSDF = myNodes["Principled BSDF"]

    myBSDF.inputs["Base Color"].default_value = (0.92, 0.96, 1.0, 1)
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
myGoldColor = (1.0, 0.78, 0.15, 1.0)
myRefColor = (0.95, 0.95, 0.95, 1.0)

myReference = myCreateElectrodeMaterial("ReferenceElectrode", myRefColor)

# -----------------------------
# Parent object
# -----------------------------
myParent = bpy.data.objects.new("MEA_Layer", None)
bpy.context.collection.objects.link(myParent)

# -----------------------------
# Substrate
# -----------------------------
bpy.ops.mesh.primitive_cube_add(location=(0, 0, -mySubstrateThickness/2))
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

for myRow, myWidth in enumerate(myRowWidths):
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
            location=(myX, myY, myThickness/2)
        )

        myObj = bpy.context.object

        myBevel = myObj.modifiers.new(name="Bevel", type='BEVEL')
        myBevel.width = 0.005
        myBevel.segments = 3

        bpy.ops.object.shade_smooth()

        # Unique material per electrode instance for independent emission animation
        myMatInstance = myCreateElectrodeMaterial(f"ElectrodeMat_{myRow}_{myCol}", myGoldColor)
        myObj.data.materials.append(myMatInstance)

        if myIsRef:
            myObj.name = "Reference_Electrode"
            myObj.data.materials[0] = myReference
        else:
            myObj.name = f"Electrode_{myCount+1:02d}"
            myCount += 1

        myObj.parent = myParent
        myElectrodeObjects.append((myRow, myCol, myObj, myMatInstance))

# -----------------------------
# Camera & Lighting
# -----------------------------
bpy.ops.object.camera_add(location=(3.2, -3.6, 2.4))
myCamera = bpy.context.object
myCamera.rotation_euler = (
    math.radians(62),
    0,
    math.radians(42)
)
bpy.context.scene.camera = myCamera

bpy.ops.object.light_add(type='AREA', location=(0, -2.5, 3.5))
myLight = bpy.context.object
myLight.data.energy = 3000
myLight.data.shape = 'RECTANGLE'
myLight.data.size = 4.0
myLight.data.size_y = 4.0

bpy.ops.object.light_add(type='AREA', location=(2, 2, 1.5))
myFill = bpy.context.object
myFill.data.energy = 800
myFill.data.size = 2.5

myWorld = bpy.context.scene.world
myWorld.use_nodes = True
myBackground = myWorld.node_tree.nodes["Background"]
myBackground.inputs["Color"].default_value = (0.02, 0.02, 0.025, 1)
myBackground.inputs["Strength"].default_value = 0.8

myScene = bpy.context.scene
myScene.render.engine = 'CYCLES'
myScene.cycles.samples = 128
myScene.render.resolution_x = 1920
myScene.render.resolution_y = 1080

# ==========================================================
# Automated Animation Sequence (v04)[cite: 1, 2]
# ==========================================================

# Canonical CL1 Color Language[cite: 1]
myColorRed = (1.0, 0.05, 0.05, 1.0)       # Neuron firing / spike event[cite: 1]
myColorGreen = (0.1, 0.9, 0.2, 1.0)     # Stimulating electrode[cite: 1]
myColorLightBlue = (0.4, 0.8, 1.0, 1.0) # Positive reinforcement[cite: 1]
myColorMedBlue = (0.1, 0.4, 0.9, 1.0)   # Sensory electrode[cite: 1]
myColorGold = (1.0, 0.78, 0.15, 1.0)    # Idle electrode[cite: 1]

def mySetElectrodeState(myMat, myColor, myCameraStrength, myStartFrame):
    myEmission = myMat.node_tree.nodes["Emission"]
    myEmission.inputs["Color"].default_value = myColor
    myEmission.inputs["Color"].keyframe_insert(data_path="default_value", frame=myStartFrame)
    myEmission.inputs["Strength"].default_value = myCameraStrength
    myEmission.inputs["Strength"].keyframe_insert(data_path="default_value", frame=myStartFrame)

# Initialize Baseline (0–2 s / Frames 1–60)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myObj.name != "Reference_Electrode":
        if myCol % 3 == 0:
            mySetElectrodeState(myMat, myColorMedBlue, 1.0, 1)
            mySetElectrodeState(myMat, myColorMedBlue, 1.0, 60)
        else:
            mySetElectrodeState(myMat, myColorGold, 0.0, 1)
            mySetElectrodeState(myMat, myColorGold, 0.0, 60)

# Stimulation (2–3 s / Frames 60–90)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myRow == 3 and myCol in [2, 3]:
        mySetElectrodeState(myMat, myColorGreen, 0.0, 55)
        mySetElectrodeState(myMat, myColorGreen, 3.0, 75)
        mySetElectrodeState(myMat, myColorGreen, 0.0, 90)

# Propagation (3–5 s / Frames 90–150)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    myDist = abs(myRow - 3) + abs(myCol - 2.5)
    myPeakFrame = 95 + int(myDist * 8)
    if myPeakFrame < 150:
        mySetElectrodeState(myMat, myColorRed, 0.0, myPeakFrame - 5)
        mySetElectrodeState(myMat, myColorRed, 5.0, myPeakFrame)
        mySetElectrodeState(myMat, myColorRed, 0.0, myPeakFrame + 15)

# Network Burst (5–6 s / Frames 150–180)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myRow in [2, 4, 5] and myCol in [3, 4, 5]:
        mySetElectrodeState(myMat, myColorRed, 0.0, 145)
        mySetElectrodeState(myMat, myColorRed, 6.0, 155)
        mySetElectrodeState(myMat, myColorRed, 0.0, 175)

# Reinforcement (6–7 s / Frames 180–210)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myCol >= 4:
        mySetElectrodeState(myMat, myColorLightBlue, 0.0, 175)
        mySetElectrodeState(myMat, myColorLightBlue, 3.5, 190)
        mySetElectrodeState(myMat, myColorLightBlue, 0.8, 210)  # v04 residual faint glow[cite: 1]

# Adaptation (7–9 s / Frames 210–270)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myRow == 3 and myCol in [2, 3]:
        mySetElectrodeState(myMat, myColorGreen, 0.0, 215)
        mySetElectrodeState(myMat, myColorGreen, 3.0, 230)
        mySetElectrodeState(myMat, myColorGreen, 0.0, 240)

for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myRow == 3 and myCol in [3, 4]:
        mySetElectrodeState(myMat, myColorRed, 0.0, 235)
        mySetElectrodeState(myMat, myColorRed, 4.5, 245)
        mySetElectrodeState(myMat, myColorRed, 0.2, 270)  # Faint residual trace[cite: 1]

# Return to baseline (9–10 s / Frames 270–300)[cite: 1]
for myRow, myCol, myObj, myMat in myElectrodeObjects:
    if myObj.name != "Reference_Electrode":
        if myCol % 3 == 0:
            mySetElectrodeState(myMat, myColorMedBlue, 1.0, 300)
        else:
            mySetElectrodeState(myMat, myColorGold, 0.0, 300)

print(f"CL1 MEA v04 automated animation generated successfully: {myCount} electrodes configured!")
