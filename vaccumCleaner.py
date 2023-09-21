import python_actr

class VacuumAgent(python_actr.ACTR):
    goal = python_actr.Buffer()

    def init(self):
        self.goal.set("initialize_set_cleaning_goal")

    # ---- Cleaning Mode: Swirl Pattern ---- #

    def initialize_set_cleaning_goal(self, goal="initialize_set_cleaning_goal"):
        self.goal.set("cleaning_mode swirl_pattern")

    def cleaning_mode_swirl_pattern(self, goal="cleaning_mode swirl_pattern"):
      
        print("Cleaning Mode: Swirl Pattern")

    
        self.goal.set("random_movement")

    def random_movement(self, goal="random_movement"):
      
        print("Random Movement")

    
        self.goal.set("random_turn")

    def random_turn(self, goal="random_turn"):
   
        print("Random Turn")

     
        self.goal.set("check_cleaning_progress")

    def check_cleaning_progress(self, goal="check_cleaning_progress"):
     
        cleaning_progress = self.calculate_cleaning_progress()  # 计算清扫进度

        if cleaning_progress >= 100:
         
            self.goal.set("stop")
        else:
          
            self.goal.set("cleaning_mode swirl_pattern")

    def calculate_cleaning_progress(self):
     
        return 0 #means not finish

    # ---- Wall Tracing Mode ---- #

    def wall_detected(self, goal="wall_detected"):
    
        print("Wall Detected")

    
        self.goal.set("switch_to_wall_tracing_mode")

    def switch_to_wall_tracing_mode(self, goal="switch_to_wall_tracing_mode"):
     
        print("Switching to Wall Tracing Mode")

       
        self.goal.set("move_along_wall")

    def move_along_wall(self, goal="move_along_wall"):
        if not self.obstacle_detected():
           
            print("Moving along the wall")
        else:
           
            self.adjust_path()

    def obstacle_detected(self):
        
        return False

    def adjust_path(self):
       
        print("Adjusting path")


agent = VacuumAgent()


agent.init()
while agent.goal.chunk != "stop":
    agent.run(1)
