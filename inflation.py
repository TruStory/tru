print("Compute tru inflation over time...\n")

def print_pools(userPool, validatorPool, communityPool, stakeholderPool):
  print("user pool " + f'{userPool:,.2f}' + " validator pool " + f'{validatorPool:,.2f}' + " community pool " + f'{communityPool:,.2f}' + " stakeholder pool " + f'{stakeholderPool:,.2f}')

# current numbers
# total supply = user balances + pending stake
# user balances = 196,825tru
# pending stake =  21,570tru
# total suppy   = 218,395tru
# almost 10% tru staked

userPool        = 2500000.00  # 2,500,000tru
validatorPool   = 1000000.00  # 1,000,000tru
communityPool   = 0.00        # 0tru
stakeholderPool = 0.00        # 0tru

totalSupply = userPool + validatorPool + communityPool + stakeholderPool
print_pools(userPool, validatorPool, communityPool, stakeholderPool)
print("initial supply    : "+ f'{totalSupply:,.2f}')

userAlloc        = 0.4
validatorAlloc   = 0.2
communityAlloc   = 0.2
stakeholderAlloc = 0.2

inflationRate = 0.7 # because we have low staking (10%)
print("inflation         : %.2f percent" % (inflationRate * 100))

# play with these values
# variable interest based on inflation
userInterestRate = inflationRate * 0.75
valInterestRate = inflationRate * 0.75
print("user interest     : %.2f percent" % (userInterestRate * 100))
print("validator interest: %.2f percent" % (valInterestRate * 100))

agreeStake = 30.0
argumentStake = 10.0
period = 7
milli = 1000
agreeReward = (agreeStake * userInterestRate) * (7/365)
print("agree reward      : %.2f tru, %.2f mtru" % (agreeReward, agreeReward * milli))
argumentReward  = (argumentStake * userInterestRate) * (7/365)
print("argument reward   : %.2f tru, %.2f mtru" % (argumentReward, argumentReward * milli))

initialGift = 300.0
usersPerMonth = 250
givenToUsersYearly = usersPerMonth * 12 * initialGift
# inputs from other currencies (DAI, ETH, Atom, etc.)
externalFunds = givenToUsersYearly * 2

totalUserOwned = 0.0
totalValidatorOwned = 0.0
print("")

for year in range(0,5):
  annualProvision = inflationRate * totalSupply
  print("year %d" % (year +1))
  print("annual inflation  : " + f'{annualProvision:,.2f}')

  # increase pools
  userPool = userPool + (annualProvision * userAlloc)
  validatorPool = validatorPool + (annualProvision * validatorAlloc)
  communityPool = communityPool + (annualProvision * communityAlloc)
  stakeholderPool = stakeholderPool + (annualProvision * stakeholderAlloc)
  # print_pools(userPool, validatorPool, communityPool, stakeholderPool)

  # update total supply
  totalSupply = userPool + validatorPool + communityPool + stakeholderPool
  print("total supply      : " + f'{totalSupply:,.2f}')
 
  # account for new user gifts
  userPool = userPool - givenToUsersYearly
  totalUserOwned = totalUserOwned + givenToUsersYearly

  # account for user staking...
  # assume 1/2 of all given TRU and external inputs are staked
  amountTruStaked = (givenToUsersYearly * 0.5)
  amountOtherStaked = (externalFunds * 0.5)
  totalAmountStaked = amountTruStaked + amountOtherStaked
  stakingInterest = totalAmountStaked * userInterestRate
  # deduct user  staking from user pool
  stakingTotal = amountTruStaked + stakingInterest
  userPool = userPool - stakingTotal
  totalUserOwned = totalUserOwned + stakingTotal

  # account for validator staking (50% of validator pool is staked)
  validatorStaked = validatorPool * 0.50
  print("validator staked  : " + f'{validatorStaked:,.2f}')
  validatorInterest = validatorStaked * valInterestRate
  print("validator interest: " + f'{validatorInterest:,.2f}')
  validatorTotal = validatorStaked + validatorInterest
  validatorPool = validatorPool - validatorTotal
  totalValidatorOwned = totalValidatorOwned + validatorTotal

  print_pools(userPool, validatorPool, communityPool, stakeholderPool)

  print("total user owned  : " + f'{totalUserOwned:,.2f}')
  print("validator owned   : " + f'{totalValidatorOwned:,.2f}')
  print("")
