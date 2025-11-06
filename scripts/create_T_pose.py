from poselib.skeleton.skeleton3d import SkeletonMotion, SkeletonState

# Load your motion
motion = SkeletonMotion.from_file("../data/NatalieFirstFormOct30.npy")

# Extract first frame (or a specific T-pose frame if you know the index)
tpose_frame = SkeletonState.from_rotation_and_root_translation(
    skeleton_tree=motion.skeleton_tree,
    r=motion.local_rotation[0:1],  # First frame
    t=motion.root_translation[0:1],
    is_local=True
)

# Save T-pose
tpose_frame.to_file("../data/natalie_tpose.npy")