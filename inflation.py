print("Compute tru inflation over time...\n")

# todo
# account for staking limits
# what % is being staked right now?

userPool = 2000000.00
validatorPool = 1000000.00
communityPool = 1000000.00
stakeholderPool = 1000000.00
totalSupply = userPool + validatorPool + communityPool + stakeholderPool
print("user pool " + f'{userPool:,.2f}' + " val pool " + f'{validatorPool:,.2f}' + " comm pool " + f'{communityPool:,.2f}' + " stake pool " + f'{stakeholderPool:,.2f}')
print("total initial supply: "+ f'{totalSupply:,.2f}' + "\n")

userAlloc = 0.4
validatorAlloc = 0.2
communityAlloc = 0.2
stakeholderAlloc = 0.2

# inflation should be tied to total amount staked because
# -leave adequate amount of token liquid for trade
# -re-use cosmos code
# inflation is between 0.2 and 0.7
inflation = 0.2

# play with these values
userInterest = 1.05
valInterest = 1.05

for year in range(0,10):
  annualProvision = inflation * totalSupply
  print("year %d" % (year +1))
  print("annual provision: " + f'{annualProvision:,.2f}')

  # increase pools
  userPool = userPool + (annualProvision * userAlloc)
  validatorPool = validatorPool + (annualProvision * validatorAlloc)
  communityPool = communityPool + (annualProvision * communityAlloc)
  stakeholderPool = stakeholderPool + (annualProvision * stakeholderAlloc)
  
  # if 66% userPool was being staked
  userStaked = userPool  * 0.66
  userStakedInterest = userStaked * userInterest
  userPool = userPool - userStakedInterest

  # if 66% validatorPool was being staked
  valStaked = validatorPool  * 0.66
  valStakedInterest = valStaked * valInterest
  validatorPool = validatorPool - valStakedInterest

  print("user pool " + f'{userPool:,.2f}' + " val pool " + f'{validatorPool:,.2f}' + " comm pool " + f'{communityPool:,.2f}' + " stake pool " + f'{stakeholderPool:,.2f}')
  totalSupply = userPool + userStakedInterest + validatorPool + valStakedInterest + communityPool + stakeholderPool
  print("")