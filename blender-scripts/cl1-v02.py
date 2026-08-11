import bpy

# ---------- Clear scene ----------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ---------- Parameters ----------
mySpacing = 0.35
myRadius = 0.07
myThickness = 0.02

myRowWidths = [6,8,8,8,8,8,8,6]
myRefRow = 4
myRefCol = 0

# ---------- Create substrate ----------
bpy.ops.mesh.primitive_plane_add(size=3.4, location=(0,0,0))
mySubstrate = bpy.context.object
mySubstrate.name = "MEA_Substrate"

# ---------- Materials ----------
def myMakeMaterial(myName, myColor, myMetal=0.0, myRough=0.3):
    myMat = bpy.data.materials.new(myName)
    myMat.use_nodes = True
    myBSDF = myMat.node_tree.nodes["Principled BSDF"]
    myBSDF.inputs["Base Color"].default_value = myColor
    myBSDF.inputs["Metallic"].default_value = myMetal
    myBSDF.inputs["Roughness"].default_value = myRough
    return myMat

myGold = myMakeMaterial(
    "GoldElectrode",
    (1.0, 0.78, 0.15, 1.0),
    myMetal=1.0,
    myRough=0.15
)

myWhite = myMakeMaterial(
    "ReferenceElectrode",
    (0.95, 0.95, 0.95, 1.0),
    myMetal=0.0,
    myRough=0.2
)

# ---------- Create electrodes ----------
myCount = 0

for myRow, myWidth in enumerate(myRowWidths):

    myY = (len(myRowWidths)-1)/2 * mySpacing - myRow * mySpacing
    myXOffset = -(myWidth-1)/2 * mySpacing

    for myCol in range(myWidth):

        myX = myXOffset + myCol * mySpacing

        myIsRef = (myRow == myRefRow and myCol == myRefCol)
        myR = myRadius * (1.5 if myIsRef else 1.0)

        bpy.ops.mesh.primitive_cylinder_add(
            vertices=32,
            radius=myR,
            depth=myThickness,
            location=(myX, myY, myThickness/2)
        )

        myObj = bpy.context.object

        if myIsRef:
            myObj.name = "Reference_Electrode"
            myObj.data.materials.append(myWhite)
        else:
            myObj.name = f"Electrode_{myCount+1:02d}"
            myObj.data.materials.append(myGold)
            myCount += 1

print(f"Created {myCount} active electrodes plus one reference electrode.")
