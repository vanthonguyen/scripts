set terminal pdf
set output "error.pdf"

plot 'FILE' u ($2-$3):(1-$4) w p ls 1
