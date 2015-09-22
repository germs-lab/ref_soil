#random forest and boruta.r

library(Boruta)

setwd("C:/Users/Erick Cardenas/Documents/github/refsoil")

#Read CAZy + AA data
data=(read.csv("words_count.csv", header=TRUE, row.names=1))

cazy.data = data[,12:231]
cazy3 = cbind(cazy.data, data$Final)
cazy_boruta =Boruta (final ~ ., data = data, doTrace=2, ntree=1000, maxRuns = 1000)

cazy_boruta_decision = t(as.data.frame(cazy_boruta$finalDecision))
cazy_boruta_score = as.data.frame(cazy_boruta$ImpHistory)
cazy_boruta_score$shadowMax = NULL
cazy_boruta_score$shadowMean = NULL
cazy_boruta_score$shadowMin = NULL
cazy_boruta_out = rbind(cazy_boruta_score, cazy_boruta_decision)
write.csv(cazy_boruta_out, "words_count_boruta.csv")


foly_boruta_layer = Boruta(Layer ~ ., data = foly3, doTrace=2, 
                           ntree=1000,maxRuns=1000)
foly_boruta_layer_decision = t(as.data.frame(foly_boruta_layer$finalDecision))
foly_boruta_layer_score = as.data.frame(foly_boruta_layer$ImpHistory)
foly_boruta_layer_score$shadowMax = NULL
foly_boruta_layer_score$shadowMean = NULL
foly_boruta_layer_score$shadowMin = NULL
foly_boruta_layer_out = rbind(foly_boruta_layer_score, foly_boruta_layer_decision)
write.csv(foly_boruta_layer_out, "foly_boruta_layer_out.csv")


# Treatment effect per layer

organic_cazy_data = subset(cazy.data,data$Layer == "Organic")
mineral_cazy_data = subset(cazy.data,data$Layer == "Mineral")
organic_foly_data = subset(foly.data,data$Layer == "Organic")
mineral_foly_data = subset(foly.data,data$Layer == "Mineral")

min_data_env = droplevels(subset(data$Treatment,data$Layer == "Mineral"))
org_data_env = droplevels(subset(data$Treatment,data$Layer == "Organic"))

cazy4 = cbind(mineral_cazy_data, min_data_env)
names(cazy4)[221] = "Treatment"
cazy5 = cbind(organic_cazy_data, org_data_env)
names(cazy5)[221] = "Treatment"

foly4 = cbind(mineral_foly_data, min_data_env)
names(foly4)[12] = "Treatment"
foly5 = cbind(organic_foly_data, org_data_env)
names(foly5)[12] = "Treatment"

mineral_cazy_boruta_treatment = Boruta(Treatment ~ ., data = cazy4, 
                                       doTrace=2, ntree=1000, maxRuns=1000)
mineral_cazy_boruta_treatment_decision = t(as.data.frame(mineral_cazy_boruta_treatment$finalDecision))
mineral_cazy_boruta_treatment_score = as.data.frame(mineral_cazy_boruta_treatment$ImpHistory)
mineral_cazy_boruta_treatment_score$shadowMax = NULL
mineral_cazy_boruta_treatment_score$shadowMean = NULL
mineral_cazy_boruta_treatment_score$shadowMin = NULL
mineral_cazy_boruta_treatment_out = rbind(mineral_cazy_boruta_treatment_score, mineral_cazy_boruta_treatment_decision)
write.csv(mineral_cazy_boruta_treatment_out, 
          "mineral_cazy_boruta_treatment.csv")


organic_cazy_boruta_treatment = Boruta(Treatment ~ ., data = cazy5, 
                                       doTrace=2, ntree=1000, maxRuns=1000)
organic_cazy_boruta_treatment_decision = t(as.data.frame(organic_cazy_boruta_treatment$finalDecision))
organic_cazy_boruta_treatment_score = as.data.frame(organic_cazy_boruta_treatment$ImpHistory)
organic_cazy_boruta_treatment_score$shadowMax = NULL
organic_cazy_boruta_treatment_score$shadowMean = NULL
organic_cazy_boruta_treatment_score$shadowMin = NULL
organic_cazy_boruta_treatment_out = rbind(organic_cazy_boruta_treatment_score, organic_cazy_boruta_treatment_decision)
write.csv(organic_cazy_boruta_treatment_out, 
          "organic_cazy_boruta_treatment.csv")


### 

mineral_foly_boruta_treatment = Boruta(Treatment ~ ., data = foly4, 
                                       doTrace=2, ntree=1000, maxRuns=1000)
mineral_foly_boruta_treatment_decision = t(as.data.frame(mineral_foly_boruta_treatment$finalDecision))
mineral_foly_boruta_treatment_score = as.data.frame(mineral_foly_boruta_treatment$ImpHistory)
mineral_foly_boruta_treatment_score$shadowMax = NULL
mineral_foly_boruta_treatment_score$shadowMean = NULL
mineral_foly_boruta_treatment_score$shadowMin = NULL
mineral_foly_boruta_treatment_out = rbind(mineral_foly_boruta_treatment_score, mineral_foly_boruta_treatment_decision)
write.csv(mineral_foly_boruta_treatment_out, 
          "mineral_foly_boruta_treatment.csv")


organic_foly_boruta_treatment = Boruta(Treatment ~ ., data = foly5, 
                                       doTrace=2, ntree=1000, maxRuns=1000)
organic_foly_boruta_treatment_decision = t(as.data.frame(organic_foly_boruta_treatment$finalDecision))
organic_foly_boruta_treatment_score = as.data.frame(organic_foly_boruta_treatment$ImpHistory)
organic_foly_boruta_treatment_score$shadowMax = NULL
organic_foly_boruta_treatment_score$shadowMean = NULL
organic_foly_boruta_treatment_score$shadowMin = NULL
organic_foly_boruta_treatment_out = rbind(organic_foly_boruta_treatment_score, organic_foly_boruta_treatment_decision)
write.csv(organic_foly_boruta_treatment_out, 
          "organic_foly_boruta_treatment.csv")


sessionInfo()

# R version 2.15.0 (2012-03-30)
# Platform: x86_64-pc-mingw32/x64 (64-bit)

# locale:
# [1] LC_COLLATE=English_United States.1252  LC_CTYPE=English_United States.1252   
# [3] LC_MONETARY=English_United States.1252 LC_NUMERIC=C                          
# [5] LC_TIME=English_United States.1252    

# attached base packages:
#  [1] stats     graphics  grDevices utils     datasets  methods   base     

# other attached packages:
#  [1] Boruta_3.0.0       rFerns_0.3.3       randomForest_4.6-7 ggplot2_0.9.3.1   

# loaded via a namespace (and not attached):
# [1] colorspace_1.2-4   dichromat_2.0-0    digest_0.6.3       grid_2.15.0        gtable_0.1.2      
# [6] labeling_0.2       MASS_7.3-23        munsell_0.4.2      plyr_1.8           proto_0.3-10      
# [11] RColorBrewer_1.0-5 reshape2_1.2.2     scales_0.2.3       stringr_0.6.2      tools_2.15.0

#save.image("Random_forest_and_Boruta.RData")
#load("Random_forest_and_Boruta.RData")
rm(list=ls())
