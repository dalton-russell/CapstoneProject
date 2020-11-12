getwd()

#Reading the table

data <- read.csv("Inpatient_data.csv", header = T)

head(data)

attach(data)

# Number of days in hospital

data$CLM_ADMSN_DT <- as.Date(as.character(data$CLM_ADMSN_DT), format='%Y%m%d')
data$NCH_BENE_DSCHRG_DT <- as.Date(as.character(data$NCH_BENE_DSCHRG_DT), format='%Y%m%d')
data$NumofDays = abs(data$CLM_ADMSN_DT - data$NCH_BENE_DSCHRG_DT)
head(data[,"CLM_ADMSN_DT"])

plot(data$NumofDays, CLM_PMT_AMT)

# Random sampling of the data to see any trends
set.seed(123)
index <- sample(1:nrow(data), 1000)
data.sample <- data[index, ]

# Plotting Number of days admitted in the hospital and Claim utilization days against claim amount
head(data.sample)
plot(data.sample$NumofDays, data.sample$CLM_PMT_AMT)
plot(data.sample$CLM_UTLZTN_DAY_CNT, data.sample$CLM_PMT_AMT)

boxplot(CLM_PMT_AMT)

# Deleting columns with no values in them (HCPCS_CD_# has no values in them)
head(data[,37:81])
unique(data[,37:81])
data.filtered <- data[,-c(37:81)] # dropped 45 columns

# Combining 11 categorical variables into one column
head(data.filtered[,45:55])
data.filtered$Chrnc_cond = apply(data.filtered[,45:56], 1, function(x) names(x)[as.logical(as.numeric(as.character(x)))])
data.filtered$Chrnc_cond
data.filtered <- data.filtered[,-c(45:55)] # dropping 10 categorical columns that had been converted to 1 col

# Coorelation of attributes

set.seed(7)
library(caret)

corMatrix <- cor(data.filtered[,c(7,8,14:17)])
print(corMatrix)
highlyCorrelated <- findCorrelation(corMatrix, cutoff = 0.5)
print(highlyCorrelated)
# we can see that features selected are not highly coorelated. Hence, we don't need to drop features.

summary(data.filtered)
unique(data.filtered$NCH_BENE_IP_DDCTBL_AMT)
# There are fixed deductible amount which consist of 4 amounts.

# Ranking features by importance
#control <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
#model <- train(data.filtered$CLM_PMT_AMT ~. , data = data.filtered, method = "lvq", trControl = control, na.action = na.exclude)

# Boxplot of Sex vs Claim Payment Amount
par(mfrow=c(1,2))
boxplot(data.filtered$CLM_PMT_AMT ~ data.filtered$Inpatient.BENE_SEX_IDENT_CD, ylab="Claim Payment", xlab="Sex")
# We can see that there are no differences in the claim payment amount for different sex. They have about the same mean.

# Average Claims amount paid for each state
avg_state <- aggregate(x = data.filtered$CLM_PMT_AMT,
          by = list(data.filtered$Inpatient.SP_STATE_CODE),
          FUN = mean)
highestState <- max(avg_state)
lowestState <- min(avg_state$x)
differenceH <- highestState - mean(avg_state$x)
differenceL <- abs(lowestState - mean(avg_state$x))

# State 28 has the highest average amount of claims amount paid which is about $10899.84, and it is $1331.11 more than the mean among all the states
# State 51 has the lowest average amount of claims amount paid which is about $7793, and it is $1775.93 less than the mean among all the states.

# Average Claims amount paid for each race
avg_race <- aggregate(x = data.filtered$CLM_PMT_AMT,
                       by = list(data.filtered$Inpatient.BENE_RACE_CD),
                       FUN = mean)
library(ggplot2)
ggplot(avg_race, aes(x = avg_race$Group.1, y = avg_race$x, color=avg_race$Group.1)) + geom_point(size = 3)
