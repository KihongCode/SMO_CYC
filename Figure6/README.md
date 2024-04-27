Scripts used to generate Figure 6 in the manuscript. 

make_input_files.py generates hole_msm_input_{i+1}.inp files for each selected 10000 frames of each system. hole_msm_input_{i+1}.inp is used to gener

output_filegen.sh runs each hole_msm_input_{i+1}.inp files using hole program to generate hole_msm_output_{i+1}.txt files.

From hole_msm_output_{i+1}.txt files, radius and z-coordinates are extracted.

tunnel_plot.py plots the diameter and z-coordinates for each system (load .npy files for each system in this code).

Trajectories are available on [*Box*](https://uofi.box.com/s/4g3xmumfmesb68y7tb0fn8wvhvycylrf)

Individual npy files used to create the figure are availble on the [*Dryad Repository*](https://doi.org/10.5061/dryad.4b8gthtmf)
