df <- read.csv("mt_cars.csv")

pdf("cars_r.pdf")
plot(x = df$wt,
     y = df$mpg,
     xlab = "Weight",
     ylab = "Milage")
dev.off()