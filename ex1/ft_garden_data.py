# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rajarada <rajarada@learner.42.tech>        #+#  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/17 23:38:54 by rajarada          #+#    #+#              #
#    Updated: 2026/02/18 01:16:35 by rama             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self.height = height
        self.old = old
    def ft_garden_data(self):
        print(self.name, ":", self.height,"cm,", self.old, "days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Mint", 15, 10),
        Plant("Tulip", 20, 20)
        ]

    for i in range(3):
        plants[i].ft_garden_data()
