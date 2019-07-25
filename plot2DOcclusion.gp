set pm3d map
set terminal pdf
set output "test.pdf"
set datafile separator "\t"
splot '/home/nguyen/work/experimentation/lvox/TerreNeuve/paperLvox/19202915/results/10cm/scanall-rz.hist' using 1:2:3
#splot 'test' matrix nonuniform with image notitle
