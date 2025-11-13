import torch
from poselib.core.rotation3d import quat_from_angle_axis, quat_mul
from poselib.skeleton.skeleton3d import SkeletonMotion, SkeletonState
from poselib.visualization.common import plot_skeleton_state

# Load your motion
motion = SkeletonMotion.from_file("data/NatalieFirstFormOct30.npy")
skeleton = motion.skeleton_tree

tpose = SkeletonState.zero_pose(skeleton)
local_rotation = tpose.local_rotation


left_arm = skeleton.index("Motta_Oct30_LeftArm")
right_arm = skeleton.index("Motta_Oct30_RightArm")

raise_arm = quat_from_angle_axis(
    angle=torch.tensor([90.0]),  # adjust sign if arms rotate the wrong way
    axis=torch.tensor([1.0, 0.0, 0.0]),  # pick the correct axis for your rig
    degree=True,
)
lower_arm = quat_from_angle_axis(
    angle=torch.tensor([-90.0]),
    axis=torch.tensor([1.0, 0.0, 0.0]),
    degree=True,
)

local_rotation[left_arm] = quat_mul(raise_arm, local_rotation[left_arm])
local_rotation[right_arm] = quat_mul(lower_arm, local_rotation[right_arm])

# optional wrist/elbow adjustments here
# translation = tpose.root_translation
# translation += torch.tensor([0, 0, 0.9])    # adjust as needed

tpose.to_file("data/natalie_tpose.npy")

plot_skeleton_state(tpose)