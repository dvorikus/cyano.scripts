# sliding window analysis of long table with data for specific
# parts of chromosome. Mean is calculated for each stretch 
# and table is written to the file

recomb.test <- read.table("L5.chr7.txt", header = T)

library(dplyr)
library(windowscanr)

pos_win <- winScan(x = recomb.test, 
                   position = "left_snp.chr7.L5", 
                   values = "mean.chr7.L5", 
                   win_size = 50000,
                   win_step = 10000)


write.table(pos_win, file = "result")
