print("Compute tru inflation over time...\n")

def print_pools(userPool, validatorPool, communityPool, stakeholderPool):
  print("user pool " + f'{userPool:,.2f}' + " validator pool " + f'{validatorPool:,.2f}' + " community pool " + f'{communityPool:,.2f}' + " stake pool " + f'{stakeholderPool:,.2f}')

# current numbers
# total supply = user balances + pending stake
# user balances = 196,825tru
# pending stake =  21,570tru
# total suppy   = 218,395tru
# almost 10% tru staked

userPool = 2000000.00         # 2,000,000tru
validatorPool = 1000000.00    # 1,000,000tru
communityPool = 1000000.00    # 1,000,000tru
stakeholderPool = 1000000.00  # 1,000,000tru

totalSupply = userPool + validatorPool + communityPool + stakeholderPool
print_pools(userPool, validatorPool, communityPool, stakeholderPool)
print("total initial supply: "+ f'{totalSupply:,.2f}' + "\n")

userAlloc = 0.4
validatorAlloc = 0.2
communityAlloc = 0.2
stakeholderAlloc = 0.2

# inflation should be tied to total amount staked...
# b/c need leave adequate amount of token liquid for trade
# cosmos inflation changes between 20% and 70% (high staking to low staking)
# inflation goes from 20% (when nearly 66% staked) to 70% (when closer to 0% staked)
inflation = 0.6 # because we have low staking (10%)

# play with these values
userInterest = 1.0 #105%
valInterest = 1.0  #105%

totalUserOwned = 0.0
totalValidatorOwned = 1000000.0

for year in range(0,10):
  annualProvision = inflation * totalSupply
  print("year %d" % (year +1))
  print("annual provision: " + f'{annualProvision:,.2f}')

  # increase pools
  userPool = userPool + (annualProvision * userAlloc)
  validatorPool = validatorPool + (annualProvision * validatorAlloc)
  communityPool = communityPool + (annualProvision * communityAlloc)
  stakeholderPool = stakeholderPool + (annualProvision * stakeholderAlloc)
  
  # account for new user gifts
  userOwned = 250 * 12 * 300 # 250 users a month
  userPool = userPool - userOwned
  totalUserOwned = totalUserOwned + userOwned

  # account for staking...
  # if 66% user funds are being staked
  userStaked = totalUserOwned * 0.66
  userStakedInterest = userStaked * userInterest
  userPool = userPool - userStakedInterest

  # if 66% validator funds are being staked
  # valStaked = totalValidatorOwned * 0.66
  # valStakedInterest = valStaked * valInterest
  # validatorPool = validatorPool - valStakedInterest

  print_pools(userPool, validatorPool, communityPool, stakeholderPool)

  # totalSupply = userPool + userOwned + userStakedInterest + validatorPool + valStakedInterest + communityPool + stakeholderPool
  totalSupply = userPool + userOwned + userStakedInterest + validatorPool + communityPool + stakeholderPool

  # total supply with no staking...
  # totalSupply = userPool + userOwned + validatorPool + communityPool + stakeholderPool
  print("total user owned:      " + f'{totalUserOwned:,.2f}')
  print("total validator owned: " + f'{totalValidatorOwned:,.2f}')
  print("")
