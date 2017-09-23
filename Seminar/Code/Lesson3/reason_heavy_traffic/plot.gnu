set terminal png font "/Library/Fonts/Times New Roman.ttf,14" size 1080,720 
set xlabel "distance" 
set ylabel "time" 
set output "traffic.png"
set xrange[0:8000] 
plot "data" using 2:1 with dots title "traffic"
