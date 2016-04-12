setwd=("~/Documents/Research/2016/4April/anova/")
data <- read.table("~/Documents/Research/2016/4April/anova/anova_input.txt",header=TRUE)

colnames(data) <- c("otu","type","value")
sum = summarySE(data, measurevar="value", groupvars=c("otu","type"))

model = lm(value ~ otu + type + otu:type,data=data)
anova(model)  
