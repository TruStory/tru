print("Compute tru inflation over time...\n")

def print_pools(userPool, validatorPool, communityPool, stakeholderPool):
  print("user pool " + f'{userPool:,.2f}' + " validator pool " + f'{validatorPool:,.2f}' + " community pool " + f'{communityPool:,.2f}' + " stakeholder pool " + f'{stakeholderPool:,.2f}')

# current numbers
# total supply = user balances + pending stake
# user balances = 196,825tru
# pending stake =  21,570tru
# total suppy   = 218,395tru
# almost 10% tru staked

userPool        = 5000000.00  # 5,000,000tru
validatorPool   = 1000000.00  # 1,000,000tru
communityPool   = 1000000.00  # 1,000,000tru
stakeholderPool = 0.00        # 0tru

totalSupply = userPool + validatorPool + communityPool + stakeholderPool
print_pools(userPool, validatorPool, communityPool, stakeholderPool)
print("total initial supply: "+ f'{totalSupply:,.2f}')

userAlloc = 0.4
validatorAlloc = 0.2
communityAlloc = 0.2
stakeholderAlloc = 0.2

# inflation should be tied to total amount staked...
# b/c need leave adequate amount of token liquid for trade
# cosmos inflation changes between 20% and 70% (high staking to low staking)
# inflation goes from 20% (when nearly 66% staked) to 70% (when closer to 0% staked)
inflationRate = 0.5 # because we have low staking (10%)
print("inflation           : %.2f percent" % (inflationRate * 100))

# play with these values
# fixed interest
# userInterest = 1.05 #105%
# valInterest = 1.05  #105%
# variable interest based on inflation
userInterest = inflationRate * 0.75
valInterest = inflationRate * 0.75
print("user interest       : %.2f percent" % (userInterest * 100))
print("validator interest  : %.2f percent" % (valInterest * 100))

agreeStake = 30.0
argumentStake = 10.0
period = 7
milli = 1000
agreeReward = (agreeStake * userInterest) * (7/365)
print("agree reward   : %.2f tru, %.2f mtru" % (agreeReward, agreeReward * milli))
argumentReward  = (argumentStake * userInterest) * (7/365)
print("argument reward: %.2f tru, %.2f mtru" % (argumentReward, argumentReward * milli))

initialGift = 300.0
usersPerMonth = 250
givenToUsersYearly = usersPerMonth * 12 * initialGift
# inputs from other currencies (DAI, ETH, Atom, etc.)
externalFunds = givenToUsersYearly * 2
totalUserOwned = 0.0

totalValidatorStaked = validatorPool * 0.66
validatorPool = validatorPool - totalValidatorStaked
totalSupply = userPool + validatorPool + communityPool + stakeholderPool
print_pools(userPool, validatorPool, communityPool, stakeholderPool)
print("")

for year in range(0,10):
  annualProvision = inflationRate * totalSupply
  print("year %d" % (year +1))
  print("annual inflation: " + f'{annualProvision:,.2f}')

  # increase pools
  userPool = userPool + (annualProvision * userAlloc)
  validatorPool = validatorPool + (annualProvision * validatorAlloc)
  communityPool = communityPool + (annualProvision * communityAlloc)
  stakeholderPool = stakeholderPool + (annualProvision * stakeholderAlloc)
  
  # account for new user gifts
  userPool = userPool - givenToUsersYearly
  totalUserOwned = totalUserOwned + givenToUsersYearly

  # account for user staking...
  # assume 1/2 of all given TRU and external inputs are staked
  amountStaked = (givenToUsersYearly * 0.5) + (externalFunds * 0.5)
  stakingInterest = amountStaked * userInterest * 5
  # deduct staking interest from user pool
  userPool = userPool - stakingInterest

  # account for validator staking
  validatorInterest = totalValidatorStaked * valInterest
  validatorPool = validatorPool - validatorInterest

  print_pools(userPool, validatorPool, communityPool, stakeholderPool)

  totalSupply = userPool + givenToUsersYearly + stakingInterest + validatorPool + validatorInterest + communityPool + stakeholderPool
  # totalSupply = userPool + userOwned + validatorPool + validatorInterest + communityPool + stakeholderPool
  print("total supply         : " + f'{totalSupply:,.2f}')
  print("total user owned     : " + f'{totalUserOwned:,.2f}')
  print("total validator owned: " + f'{totalValidatorStaked:,.2f}')
  print("")
