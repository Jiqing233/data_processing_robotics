# Data Preparation for Robotics Simulation

## What the scripts do:
1) FBX → NumPy Conversion: convert animation data from .fbx format into .npy arrays for downstream processing or simulation.
2) Skeleton Retargeting: normalize motion sequences by remapping joint names and hierarchies.

## Detailed steps: 

### Install simulation environment and FBX SDK: 
1) I'm using Nvidia Isaac Gym as my simulation environment, which requires Python 3.8.
2) Install AutoDesk FBX Python SDK, the latest version, which requires Python >= 3.10.

(I tried the older versions but found they didn't work, only the latest version worked, and it requires Python 3.10 while Isaac Gym requires Python 3.8, so annoying.)

### After successfully installed AutoDesk FBX Python SDK: 

1) Run fbx_check_joint_name.py to check joint names stored in the fbx file.
2) Run fbx_importer.py to convert data from .fbx to .npy.
3) Run create_T_pose_orig.py to generate a T-pose, which will be used for retargeting.
4) Create a config json file. You can check the format in my example. Basically it maps joint names, as the same joint could be named differently by different softwares.
5) Run retarget_motion.py to get the retargeted NumPy data. In my example, source: NatalieFirstFormOct30.npy, target: amp_humanoid_tpose.npy.


