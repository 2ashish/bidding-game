import random


def create_sample():
	nn = []
	for i in range(35):
		nn.append(random.random()/10)
	return nn

def first_pop(pop_size):
	pop = []
	for i in range(pop_size):
		pop.append(create_sample())
	return pop

def evalnn(nn,coin1,coin2,pos1,pos2,draw):
	coin1/=100
	coin2/=100
	pos1/=10
	pos2/=10
	nn[25]+= coin1*nn[0] + pos1*nn[5] + coin2*nn[10] + pos2*nn[15] + draw*nn[20]
	nn[26]+= coin1*nn[1] + pos1*nn[6] + coin2*nn[11] + pos2*nn[16] + draw*nn[21]
	nn[27]+= coin1*nn[2] + pos1*nn[7] + coin2*nn[12] + pos2*nn[17] + draw*nn[22]
	nn[28]+= coin1*nn[3] + pos1*nn[8] + coin2*nn[13] + pos2*nn[18] + draw*nn[23]
	nn[29]+= coin1*nn[4] + pos1*nn[9] + coin2*nn[14] + pos2*nn[19] + draw*nn[24]

	ans = nn[25]*nn[30] + nn[26]*nn[31] + nn[27]*nn[32] + nn[28]*nn[33] +nn[29]*nn[34]
	ans = int(ans*coin1*100)
	if(ans<0):
		ans = 0
	if(ans>coin1*100):
		ans = coin1*100
	return ans

def disp(pos,coin1,coin2,bid1,bid2,draw):
	seq =""
	for i in range(11):
		if i==pos:
			seq+="x"
		else:
			seq+="o"
	print(seq,coin1,coin2,bid1,bid2,draw)
	input()

def play(nn1,nn2,draw):
	pos =5
	coin1 = 100
	coin2 = 100
	fit1 = 0
	fit2 = 0
	#disp(pos,coin1,coin2,0,0,draw)
	move =0
	while pos!=0 and pos!=10 and move<200:
		move+=1
		bid1 = evalnn(nn1,coin1,coin2,pos,10-pos,draw)
		bid2 = evalnn(nn2,coin2,coin1,10-pos,pos,-1*draw)
		
		if(draw ==1):
			if(bid1>bid2):
				pos-=1
				coin1-=bid1
				fit1-=bid1-bid2
			if(bid2>bid1):
				pos+=1
				coin2-=bid2
				fit2-=bid2-bid1
			if(bid1==bid2):
				pos-=1
				coin1-=bid1
				draw*=-1
		else:
			if(bid1>bid2):
				pos-=1
				coin1-=bid1
				fit1-=bid1-bid2
			if(bid2>bid1):
				pos+=1
				coin2-=bid2
				fit2-=bid2-bid1
			if(bid1==bid2):
				pos+=1
				coin2-=bid2
				draw*=-1
		#print(fit1,fit2)
		#disp(pos,coin1,coin2,bid1,bid2,draw)
		if coin1==0:
			#print("player 2 wins")
			fit1-=200
			break
		if coin2==0:
			#print("player 1 wins")
			fit2=-200
			break
	if pos==0:
		fit1+=100
		fit2-=100
	if pos==10:
		fit1-=100
		fit2+=100
	if move==200:
		fit1-=100
		fit2-=100
	#print(fit1,fit2)
	return fit1

def pop_fitness(new_pop,prev_pop):
	fit_pop = {}
	#print(new_pop[0])
	for nn1 in range(len(new_pop)):
		fit = 0
		for nn2 in range(len(prev_pop)):
			fit+=play(new_pop[nn1],prev_pop[nn2],1)
		#print(fit)
		fit_pop[str(nn1)] = fit
	return sorted(fit_pop.items(), key = lambda t: t[1],reverse = True )

# def select_pop(fit_pop,pop,pop_size):
# 	for i 

nn1 = create_sample()
nn2 = create_sample()
#fit =  play(nn1,nn2,1)
#print(fit)

pop_size = 50
max_gen = 1
new_pop = first_pop(pop_size)
prev_pop = first_pop(2*pop_size/5)

for gen in range(max_gen):
	fit_pop = pop_fitness(new_pop,prev_pop)
	for i in range(50):
		print(fit_pop[i][1])

	

