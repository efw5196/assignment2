import python_actr
from python_actr.actr import *

class PizzaBuilder(ACTR):
    goal = Buffer()
    my_pizza = []

    def cook_pizza(self, pizza_ingred):
        return "_".join(pizza_ingred)

    def init(self):
        self.goal.set("build_pizza choose_crust")

    def choose_crust(self, goal="build_pizza choose_crust"):
        self.my_pizza.append("thin_crust")
        self.goal.set("build_pizza place_meat")

    def place_meat(self, goal="build_pizza place_meat"):
        self.my_pizza.append("pepperoni")
        self.goal.set("build_pizza add_sauce")

    def add_sauce(self, goal="build_pizza add_sauce"):
        self.my_pizza.append("tomato_sauce")
        self.goal.set("build_pizza sprinkle_cheese")

    def sprinkle_cheese(self, goal="build_pizza sprinkle_cheese"):
        self.my_pizza.append("mozzarella_cheese")
        self.goal.set("cook_pizza")

    def cook_pizza(self, goal="cook_pizza"):
        self.my_pizza = self.cook_pizza(self.my_pizza)
        print("Mmmmmm my " + self.my_pizza + " pizza is gooooood!")
        self.stop()

class EmptyEnvironment(python_actr.Model):
    pass

env_name = EmptyEnvironment()
agent_name = PizzaBuilder()
env_name.agent = agent_name
python_actr.log_everything(env_name)
env_name.run()
