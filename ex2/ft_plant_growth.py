# **************************************************************************** #i
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rajarada <rajarada@learner.42.tech>        #+#  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 00:46:41 by rajarada          #+#    #+#              #
#    Updated: 2026/02/18 01:13:50 by rama             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self.height = height
        self.old = old
    def ft_get_info(self):
        print(self.name, ":", self.height,"cm,", self.old, "days old")
    def grow(self):
        self.height = self.height + 1
    def age(self):
        self.old = self.old + 1

if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.ft_get_info()
    for i in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.ft_get_info()
    print("Growth this week: +6cm")
