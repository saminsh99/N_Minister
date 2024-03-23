n = 4
p_s = 200
import random as rnd
def init(population_size,n): #جمعیت اولیه 
    population_list =[]
    for i in range(population_size):
        new_member = []
        for j in range(n):
            new_member.append(rnd.randint(1,n))
        population_list.append(new_member)
    
    return
population = init(p_s,n)
def cross_over(population_list):
    for i in range(0, len(population_list),2):
        child1 = population_list[i][:len(population_list[0])//2] + population[i+1][len(population[0])//2:len(population[0])-1]+[0]
        child2 = population[i+1][len(population[0])//2:len(population[0])-1] + population_list[i][:len(population_list[0])//2]+[0]

        population_list.append(child1)
        population_list.append(child2)
    return population_list
population = init(p_s,n)
population = cross_over(population)
print(population[0])
print(population[1])
