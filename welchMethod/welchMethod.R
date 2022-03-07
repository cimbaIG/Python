#Load libraries
library("gsignal")
library("here")

#Set current directory as working directory
setwd(here())

#Read moment signal data and create moment and sample vectors
moment_data <- as.matrix(read.table("moment_signal.txt", sep = ""))
moment <- moment_data[, 1]
samples <- moment_data[, 2]

#Set window for plotting
op <- par(mfrow = c(2, 1))

#Sampling frequency
fs <- 2000

#Create time vector from sample number and frequency
time <- samples / fs

nsecs <- time[length(time)] #Get maximum time from time vector
lx <- fs * nsecs #Get window length

#Opening the graphical device
pdf("welch.pdf")

#Plot velocity signal
plot(time, moment, type = "l", xlab = "Time (s)", ylab = "",
    main = "Moment signal")

#Calculate and plot PSD using Welch method
pw <- pwelch(moment, window = lx, fs = fs, detrend = "none")
plot(pw, main = "PSD estimate using FFT", log = "y")

#Closing the graphical device
dev.off()