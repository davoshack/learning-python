from collections import defaultdict

class RewardPoints:
    def __init__(self):
        self.customers = defaultdict(int)
        
    def earn_points(self, customer_name, points):
        if points > 0:
            if self.customers[customer_name] == 0:
                self.customers[customer_name] += 500
            self.customers[customer_name] += points
    
    def spend_points(self, customer_name, points):
        if customer_name not in self.customers or points <= 0:
            return 0
    
        if self.customers[customer_name] < points:
            return self.customers[customer_name]
     
        self.customers[customer_name] -= points
        return self.customers[customer_name]
        
        
if __name__ == "__main__":
    rewardPoints = RewardPoints()
    rewardPoints.earn_points('John', 520)
    print(rewardPoints.spend_points('John', 200))