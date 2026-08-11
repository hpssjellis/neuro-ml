import bpy

# ---------- Clear scene ----------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ---------- Parameters ----------
mySpacing = 0.35
myRadius = 0.07
myThickness = 0.01

myRowWidths = [6,8,8,8,8,8,8,6]
myRefRow = 4
myRefCol = 0

# ---------- Create substrate ----------
bpy.ops.mesh.primitive_plane_add(size=3.2, location=(0,0,0))
mySubstrate = bpy.context.object
mySubstrate.name = "MEA_Substrate"
mySubstrate.scale.z = 0.02

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
myCollection = bpy.data.collections.new("MEA_Layer")
bpy.context.scene.collection.children.link(myCollection)

myMaxWidth = max(myRowWidths)

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
            myObj.name = f"E_{myRow}_{myCol}"
            myObj.data.materials.append(myGold)

        myCollection.objects.link(myObj)
        bpy.context.scene.collection.objects.unlink(myObj)

print("Created MEA layer with 59 electrodes + reference electrode.")
