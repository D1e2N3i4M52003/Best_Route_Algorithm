import random
elite_chromosomse = 1
Population_Size = 20
tournament_size = 5
mutationrate = 0.01
print("Please type the time you want the route to be in minutes:")
userTimeM = input()
userTimeM = int(userTimeM)
userTime = userTimeM*60
bookmarkedDestinations = {"g"}
print("Please type the number of the destinations you definetely want to visit:")
bDestination = input()
bDestination = int(bDestination)
print("Please type the exact names of the destinations")
for i in range(bDestination):
    bookmarkedDestinations.add(bDestination)
    bDestination = input()
print("Money")
money = input()
money = int(money)
print("Number of people")
brPeople = input()
brPeople = int(brPeople)
agepeople = []
print("Age")
for i in range(brPeople):
    age = input()
    age = int(age)
    agepeople.append(age)
Code = {
    0: "Academy of Fine Arts, Picture Gallery",
    1: "Albertina",
    2: "Anker Clock",
    3: "Archives of the Austrian Resistance",
    4: "Belvedere 21",
    5: "Burgtheater",
    6: "St. Charles Church",
    7: "Chocolate Museum Vienna",
    8: "Church of the Augustinian Friars",
    9: "Crime Museum",
    10: "Danube Tower",
    11: "Sigmund Freud Museum"
}
PriceCode = {
    0: "Adult",
    1: "Children under 19",
    2: "Adults under 26",
    3: "65+",
    4: "special needs",
    5: "Students",
    6: "5-14",
    7: "group 10p+",
    8: "12-18",
    9: "19-27",
    10: "under 6"
}
Price = [
    [12, 0, -1, 9, -1, 9, -1, 9, -1, -1, -1],
    [16.90, 0, 11.90, 12.90, 7, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [15, -1, -1, 12, 10, 12, 8, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [9, -1, -1, -1, -1, -1, -1, -1, 6, 3, -1],
    [14.50, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]
]
Time = [
    [0, 480, 1140, 1200, 1920, 960, 600, 2880, 540, 1860, 5400, 1800],
    [480, 0, 600, 720, 2100, 780, 720, 2340, 120, 1560, 4920, 1260],
    [1140, 600, 0, 180, 2580, 960, 1260, 1800, 540, 780, 4380, 960],
    [1200, 720, 180, 0, 2760, 780, 1380, 1920, 660, 780, 4500, 780],
    [1920, 2100, 2580, 2760, 0, 2820, 1440, 3300, 2160, 3360, 6060, 3420],
    [960, 780, 960, 780, 2820, 0, 1440, 2700, 660, 1500, 5160, 840],
    [600, 720, 1260, 1380, 1440, 1440, 0, 2460, 840, 1920, 5220, 2040],
    [2880, 2340, 1800, 1920, 3300, 2700, 2460, 0, 2340, 1380, 3000, 2520],
    [540, 120, 540, 660, 2160, 660, 840, 2340, 0, 1380, 4920, 1260],
    [1860, 1560, 780, 780, 3360, 1500, 1920, 1380, 1380, 0, 3840, 1140],
    [5400, 4920, 4380, 4500, 6060, 5160, 5220, 3000, 4920, 3840, 0, 4560],
    [1800, 1260, 960, 780, 3420, 840, 2040, 2520, 1260, 1140, 4560, 0]
]
Sight = [
    [0, 650, 1500, 1700, 2600, 1300, 750, 3300, 750, 2400, 7000, 2500],
    [650, 0, 850, 1000, 2700, 1100, 1000, 3100, 130, 1900, 6400, 1800],
    [1500, 850, 0, 250, 3400, 1200, 1700, 4200, 750, 1100, 5700, 1400],
    [1700, 1000, 250, 0, 3600, 1000, 1900, 2600, 900, 1100, 5800, 1200],
    [2600, 2700, 3400, 3600, 0, 3600, 1800, 2400, 2800, 4300, 7800, 4500],
    [1300, 1100, 1200, 1000, 3600, 0, 1900, 3000, 950, 1900, 6800, 1200],
    [750, 1000, 1700, 1900, 1800, 1900, 0, 3700, 1100, 2600, 6700, 2800],
    [3300, 3100, 4200, 2600, 2400, 3000, 3700, 0, 3000, 1800, 3800, 3100],
    [750, 130, 750, 900, 2800, 950, 1100, 3000, 0, 1800, 6300, 1700],
    [2400, 1900, 1100, 1100, 4300, 1900, 2600, 1800, 1800, 0, 5000, 1400],
    [7000, 6400, 5700, 5800, 7800, 6800, 6700, 3800, 6300, 5000, 0, 6000],
    [2500, 1800, 1400, 1200, 4500, 1200, 2800, 3100, 1700, 1400, 6000, 0],
]
print(agepeople)


class Chromosome:

    def __CountPrice(self, des):
        price2 = 0
        for j in range(brPeople):
            q = agepeople[j]
            r = 0
            if q > 65 and Price[des][3] != -1:
                if r == 0:
                    price2 += Price[des][3]
                    r = 1
            if q < 26 and Price[des][2] != -1:
                if r == 0:
                    price2 += Price[des][2]
                    r = 1
            if 19 <= q < 27 and Price[des][9] != -1:
                if r == 0:
                    price2 += Price[des][9]
                    r = 1
            if q < 19 and Price[des][1] != -1:
                if r == 0:
                    price2 += Price[des][1]
                    r = 1
            if 12 <= q <= 18 and Price[des][8] != -1:
                if r == 0:
                    price2 += Price[des][8]
                    r = 1
            if 5 <= q <= 14 and Price[des][6] != -1:
                if r == 0:
                    price2 += Price[des][6]
                    r = 1
            if q < 6 and Price[des][10] != -1:
                if r == 0:
                    price2 += Price[des][10]
                    r = 1
            if brPeople >= 10:
                price2 += Price[des][7] * brPeople
            if r == 0:
                price2 += Price[des][0]
            if price2 == -1:
                price2 = 0
            """"print(q, agepeople[j], j, Price[des][j], price2)"""
        return price2

    def __init__(self):
        self.genes = []
        genes1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        n = 12
        self._fitness = 0
        self.countbd = 0
        self.weight = 0
        self.price = 0
        index1 = random.randint(0, n - 1)
        n -= 1
        self.duration = 0
        x = genes1[index1]
        if self.__CountPrice(x) > -1:
            self.price += self.__CountPrice(index1)
            """"print(self.price, Price[x][0], genes1[index1])"""

        if bookmarkedDestinations.__contains__(Code[index1]):
            self.weight += 100
            self.countbd += 1
        self.genes.append(genes1[index1])
        genes1.__delitem__(index1)
        i1 = 0
        self.count = 1
        o = random.randint(0, n - 1)
        while i1 < o:
            index1 = random.randint(0, n - 1)
            x = genes1[index1]
            y = self.genes[i1]
            duration1 = Time[x][y]
            if self.duration + duration1 > userTime:
                break
            self.duration += duration1
            if self.__CountPrice(x) > -1:
                self.price += self.__CountPrice(x)
                """"print(self.price, Price[x][0], genes1[index1])"""
            if bookmarkedDestinations.__contains__(Code[x]):
                self.weight += 100
                self.countbd += 1
            self.genes.append(genes1[index1])
            genes1.__delitem__(index1)
            n -= 1
            i1 += 1
            self.count += 1
        """"print("new chrom")"""""
        if money < self.price:
            self.weight = 0
        """ def get_test(self, index1, index2):
        print(Sight[index2], " ", Sight[index1], " ", self.duration)
      """

    def get_genes(self):
        return self.genes

    def get_duration(self):
        return self.duration

    def get_fitness(self):
        self._fitness = 0
        self._fitness += self.count * 1000 + self.duration / 10000 + self.weight * 10
        if money < self.price:
            self._fitness = 0
        return self._fitness

    def get_price(self):
        return self.price

    def get_str_(self):
        return self.genes.__str__()


class Population:
    def __init__(self, size):
        self.chromosomes = []
        i = 0
        while i < size:
            chromosome = Chromosome()
            self.chromosomes.append(chromosome)
            i += 1

    def get_chromosomes(self):
        return self.chromosomes


class GeneticAlgorithm:
    @staticmethod
    def evolve(pop):
        return GeneticAlgorithm._crossover_population(pop)

    @staticmethod
    def _crossover_population(pop):
        crosover_pop = Population(0)
        for i in range(elite_chromosomse + 1):
            crosover_pop.get_chromosomes().append(pop.get_chromosomes()[i])
        i = elite_chromosomse
        while i < Population_Size:
            crome1 = GeneticAlgorithm.tournament_selection_population(pop).get_chromosomes()[0]
            crome2 = GeneticAlgorithm.tournament_selection_population(pop).get_chromosomes()[0]
            crosover_pop.get_chromosomes().append(GeneticAlgorithm.cross_chromosomes(crome1, crome2))
            i += 1
        return crosover_pop

    @staticmethod
    def cross_chromosomes(chromosome1, chromosome2):
        cross_chrom = Chromosome()
        k = 0
        o = 0
        i = 0
        while cross_chrom.get_duration() > userTime:
            if i % 2 == 0:
                if o != chromosome2.get_genes().__len__():
                    cross_chrom.get_genes().append(chromosome2.get_genes()[o])
                    chromosome1.get_genes().remove(chromosome2.get_genes()[o])
            else:
                if k != chromosome1.get_genes().__len__():
                    cross_chrom.get_genes().append(chromosome1.get_genes()[k])
                    chromosome2.get_genes().remove(chromosome1.get_genes()[k])
            i += 1
        return cross_chrom

    @staticmethod
    def tournament_selection_population(pop):
        tour_pop = Population(0)
        i = 1
        while i < tournament_size:
            tour_pop.get_chromosomes().append(pop.get_chromosomes()[random.randint(0, Population_Size - 1)])
            i += 1
        tour_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tour_pop


    def max_fittnes(pop):
        max = 0
        for x in pop.get_chromosomes():
            if x.get_fitness > max:
                max = x.get_fitness()
        return max


    @staticmethod
    def mutate_chrom(chrom):
        genes_mh = []
        j=0
        """print(chrom.get_genes())"""
        for i in range(len(Code)-1):
            if chrom.get_genes().__contains__(i):
                if j!=chrom.get_genes().__len__():
                    j+=1
            else :
                genes_mh.append(i)
                """print("Appending")
                print(i)"""
        n = genes_mh.__len__()
        e=0
        if n>0:
            for i in range(chrom.get_genes().__len__()):
                k=random.random()
                if k < mutationrate:
                    if n<=1:
                        e=0
                        """print(e, n,k)"""
                    else:
                        """print(n, k)"""
                        e=random.randint(0, n-1)
                        """print(e)"""
                        chrom.get_genes()[i] = genes_mh[e]
                        """print("mutation")"""
        return chrom

    @staticmethod
    def _mutate_population(pop):
        for i in range(elite_chromosomse, Population_Size):
            GeneticAlgorithm.mutate_chrom(pop.get_chromosomes()[i])
        return pop


def _print_population(pop, gen_number):
    print("\n--------------------------------")
    print("Generation# ", gen_number, "Fitest chromosome fitness", pop.get_chromosomes()[0].get_fitness)
    print("--------------------------------")
    i = 0
    for x in pop.get_chromosomes():
        print("Generation# ", i, " : ", x.get_genes(), "Fitness: ", x.get_fitness(), "Price: ", x.get_price(), "Duration: ", x.get_duration())
        i += 1


population = Population(Population_Size)
population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
i = 0
j = 0
"""_print_population(population, i)"""
maxf = population.get_chromosomes()[0].get_fitness()

while j<100:
    population = GeneticAlgorithm.evolve(population)
    population = GeneticAlgorithm._mutate_population(population)
    population.get_chromosomes().sort(key=lambda x:x.get_fitness(), reverse=True)
    i = i+1
    j = j+1
    """_print_population(population, j)"""
    if(population.get_chromosomes()[0].get_fitness()>maxf):
        j = 0
        maxf=population.get_chromosomes()[0].get_fitness()
for x in population.get_chromosomes():
    for p in x.get_genes():
        print(Code[p])
    print("Ghromosome# ", 1, " : ", x.get_genes(), "Fitness: ", x.get_fitness(), "Price: ", x.get_price(), "Duration: ",
          x.get_duration())
    break
