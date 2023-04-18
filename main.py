import random
import matplotlib.pyplot as plt

class Person():
    def __init__(self) -> None:
        self.boards = []
        self.colors = []
        self.nums = []

    def add_board(self, board):
        if len(self.boards) == 3:
            return False

        self.boards.append(board)
        self.nums.append(board["num"])
        self.colors.append(board["color"])
        self.nums_set = set(self.nums)
    
    def check(self):

        if self.check_leopard():
            # 是豹子
            return "leopard"
        else:
            if self.check_pair():
                return "pair"
            else:
                if self.check_straight():
                    if self.check_golden_flower():
                        return "golden_flower_straight"
                    return "straight"
                if self.check_golden_flower():
                    return "golden_flower"
                return "None"
    #检查豹子
    def check_leopard(self):
        if len(self.nums_set) == 1:
            return True
        return False
    
    #检查对子
    def check_pair(self):
        if len(self.nums_set) == 2:
            return True
        return False
            

    # 检查金花           
    def check_golden_flower(self):
        if(len(set(self.colors))) == 1:
            return True
        else:
            return False
        
    # # 检查顺子
    # def check_straight(self):
    #     # 检查是否为顺子
    #     if self.nums_set == ["J", "Q", "K"] or self.nums_set == [10, "J", "Q"] or self.nums_set == [9, 10, "J"]:
    #         return True
    #     else:
    #         for num in self.nums:
    #             if type(num) == type("str"):
    #                 self.nums.remove(num)
    #         if len(self.nums) != 3:
    #             return None
                
    #         self.nums.sort()
    #         num1 = self.nums[0]
    #         num2 = self.nums[1]
    #         num3 = self.nums[2]

    #         if num2 - num1 == 1:
    #             if num3 - num2 == 1:
    #                return True
    #             else:
    #                 return False
    #         return False
    
    # 检查顺子
    def check_straight(self):
        self.nums.sort()
        num1 = self.nums[0]
        num2 = self.nums[1]
        num3 = self.nums[2]

        if num2 - num1 == 1:
            if num3 - num2 == 1:
                return True
            else:
                return False
        return False
                
            
            

class Card():
    def __init__(self) -> None:
        self.colors = ["spade", "heart", "club", "dianmond"]
        # self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        
        all_board = []
        for i in self.colors:
            for j in self.nums:
                dict1 = {}
                dict1["color"] = i
                dict1["num"] = j
                all_board.append(dict1)

        self.board = all_board
        self.shuffle_card()

    # 洗牌
    def shuffle_card(self):
        random.shuffle(self.board) 

    # 拿牌
    def take_out(self):
        out_board = self.board.pop()
        return out_board

    # 牌数量
    def __len__(self):
        return len(self.board)

# 单人模拟
def single_player(epochs=1):

    # x_label = ["leopard", "pair", "golden_flower_straight", "straight", "golden_flower", "single"]

    x_label = ["leopard", "pair", "golden_flower_straight", "straight", "golden_flower"]


    leopard_num = 0
    pair_num = 0
    golden_flower_straight_num = 0
    straight_num = 0
    golden_flower_num = 0
    single_num = 0

    for epoch in range(epochs):
        card = Card()
        person = Person()

        for i in range(3):
            person.add_board(card.take_out()) 

        result = person.check()
        if result == "leopard":
            leopard_num += 1
        elif result == "pair":
            pair_num += 1
        elif result == "golden_flower_straight":
            golden_flower_straight_num += 1
        elif result == "straight":
            straight_num += 1
        elif result == "golden_flower":
            golden_flower_num += 1
        else:
            single_num += 1
        # print("person's boards is {}, reslut is {}".format(person.boards, result))
    
    # y_lable = [leopard_num / epochs,
    #             pair_num / epochs ,
    #             golden_flower_straight_num / epochs, 
    #             straight_num / epochs, 
    #             golden_flower_num / epochs, 
    #             single_num / epochs]
    
    y_lable = [leopard_num / epochs,
                pair_num / epochs ,
                golden_flower_straight_num / epochs, 
                straight_num / epochs, 
                golden_flower_num / epochs, 
                ]
    
    print(y_lable)

    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False


    # plt.plot(x_label, y_lable)
    # plt.plot(x_label, y_lable, color='r',marker='o',linestyle='dashed')

    
    for i in range(len(x_label)):
        plt.bar(x_label[i],y_lable[i])    

    plt.xlabel('category')
    plt.ylabel("probability")
    plt.title('Golden Flower')
    plt.savefig("1.png")
        
        
def multiplayer(epochs=1, player_num=4):
    x_label = ["leopard", "pair", "golden_flower_straight", "straight", "golden_flower"]


    leopard_num = 0
    pair_num = 0
    golden_flower_straight_num = 0
    straight_num = 0
    golden_flower_num = 0
    single_num = 0

    for epoch in range(epochs):
        card = Card()
        for player in range(player_num):
            locals()['person_' + str(player)] = Person()

        for i in range(3):
            for player in range(player_num):
                locals()['person_' + str(player)].add_board(card.take_out()) 

        result = locals()['person_0'].check()
        if result == "leopard":
            leopard_num += 1
        elif result == "pair":
            pair_num += 1
        elif result == "golden_flower_straight":
            golden_flower_straight_num += 1
        elif result == "straight":
            straight_num += 1
        elif result == "golden_flower":
            golden_flower_num += 1
        else:
            single_num += 1

    y_lable = [leopard_num / epochs,
                pair_num / epochs ,
                golden_flower_straight_num / epochs, 
                straight_num / epochs, 
                golden_flower_num / epochs, 
                ]
    
    print(y_lable)

    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False

    
    for i in range(len(x_label)):
        plt.bar(x_label[i],y_lable[i])    

    plt.xlabel('category')
    plt.ylabel("probability")
    plt.title('Golden Flower')
    plt.savefig("2.png")
    

def main():
    single_player(1000000)
    multiplayer(1000000, player_num=4)
    multiplayer(1000000, player_num=8)
    multiplayer(1000000, player_num=12)

    print("over")

if __name__ == "__main__":
    main()