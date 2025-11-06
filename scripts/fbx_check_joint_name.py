# Create a file: list_fbx_joints.py
import sys
import os
import fbx
import FbxCommon

fbx_file = "../data/NatalieFirstFormOct30.fbx"  # Update with your path

# Create the fbx scene object and load the .fbx file
fbx_sdk_manager, fbx_scene = FbxCommon.InitializeSdkObjects()
result = FbxCommon.LoadScene(fbx_sdk_manager, fbx_scene, fbx_file)
if not result:
    print(f"ERROR: Failed to load FBX file: {fbx_file}")
    sys.exit(1)

print("=" * 80)
print("All nodes in FBX file:")
print("=" * 80)

def print_all_nodes(node, indent=0, parent_name=""):
    """Recursively print all nodes in the FBX scene"""
    name = node.GetName()
    prefix = "  " * indent
    
    # Check node type
    node_type = ""
    if node.GetSkeleton():
        node_type = "[SKELETON/JOINT]"
    elif node.GetNodeAttribute():
        # Just check if it's a valid attribute, don't check specific types
        node_type = "[NODE]"
    
    print(f"{prefix}{name} (parent: {parent_name}) {node_type}")
    
    for child_index in range(node.GetChildCount()):
        child = node.GetChild(child_index)
        print_all_nodes(child, indent + 1, name)

root_node = fbx_scene.GetRootNode()
print_all_nodes(root_node)

print("\n" + "=" * 80)
print("All skeleton joints (for use as root_joint parameter):")
print("=" * 80)

def find_skeleton_nodes(node, skeleton_nodes=[]):
    """Find all skeleton/joint nodes"""
    if node.GetSkeleton():
        skeleton_nodes.append(node.GetName())
    
    for child_index in range(node.GetChildCount()):
        child = node.GetChild(child_index)
        find_skeleton_nodes(child, skeleton_nodes)
    
    return skeleton_nodes

skeletons = find_skeleton_nodes(root_node)
if len(skeletons) == 0:
    print("  No skeleton joints found.")
    print("  Note: If the file has joints but they're not detected as skeletons,")
    print("  they may be stored as regular nodes. Check the full node list above.")
else:
    for name in skeletons:
        print(f"  {name}")