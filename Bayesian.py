
def PAB(PA, PB, PBA):
    return PBA * PA / PB
#need to work out probs of each coin given a series of flip results
#first need a n choose k function
#need factorial function
import math
def n_choose_k(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def prob_of_result(result):
    flips = sum(result) # Number of flips
    heads = result[0] # Number of heads
    tails = result[1] # Number of tails
    #find prior probability of this result
    return n_choose_k(flips, heads) * (1/2)**flips
#find probability of getting this result given each coin
def prob_of_result_given_coin(result, coin): # coin is [P(Heads), P(Tails)]
    flips = sum(result) # Number of flips
    heads = result[0] # Number of heads
    tails = result[1] # Number of tails
    #find likelihood of this result
    return n_choose_k(flips, heads) * (coin[0])**heads * (coin[1])**tails
def prob_of_coin_given_result(result, coin): # coin is [P(Heads), P(Tails)]
    PA = prob_of_coin
    PB = prob_of_result(result)
    PBA = prob_of_result_given_coin(result, coin)
    return PAB(PA, PB, PBA)
#list all possible results given number of flips
def results(flips):
    return [[heads, flips-heads] for heads in range(flips+1)]
#find probabilities for coin given a number of flips
def probs_coin(flips, coin):
    return [[result, prob_of_coin_given_result(result, coin)] for result in results(flips)]

coins = [[2/3, 1/3], [1/3, 2/3]]
prob_of_coin = 1/len(coins)
flips = 5
print(prob_of_result([5,0]))
print(prob_of_result_given_coin([5,0], coins[0]))
print(prob_of_coin_given_result([5,0], coins[0]))

#problem: prob of result changes based on certainty...
#flips are not independent