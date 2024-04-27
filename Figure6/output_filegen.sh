### Use the script for CPU run
### Lines starting with "#$" are options for the SGE scheduling system
#$ -S /bin/bash
#$ -q all.q 
#$ -pe smp 24
#$ -cwd

## execute the following to compute the radius at each z_coordinate for 10000 frames.

/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_1.inp > ./hole_output_Active/hole_msm_output_1.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_2.inp > ./hole_output_Active/hole_msm_output_2.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_3.inp > ./hole_output_Active/hole_msm_output_3.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_4.inp > ./hole_output_Active/hole_msm_output_4.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_5.inp > ./hole_output_Active/hole_msm_output_5.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_6.inp > ./hole_output_Active/hole_msm_output_6.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_7.inp > ./hole_output_Active/hole_msm_output_7.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_8.inp > ./hole_output_Active/hole_msm_output_8.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_9.inp > ./hole_output_Active/hole_msm_output_9.txt
/home/kihongk2/hole/hole2/exe/hole < ./hole_input_Active/hole_msm_input_10.inp > ./hole_output_Active/hole_msm_output_10.txt

........
