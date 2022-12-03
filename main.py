from van import Van

my_van = Van()



class movement():
  def move_forward(num):
    for i in range(num):
      my_van.move_forwards()
  def turn(num, direction):
    if direction == left:
      for i in range(num):
        my_van.turn_left()
    elif direction == right:
      for i in range(num):
        my_van.turn_right()
  def auto_move():
    while True:
      if my_van.at_destination():
        print("Arrived")
        break
      if my_van.is_road_forward():
        movement.move_forward(1)
      elif my_van.is_road_left():
        movement.turn(1, left)
      elif my_van.is_road_right():
        movement.turn(1, right)
      elif my_van.at_dead_end():
        my_van.turn_around()

      elif my_van.at_red_traffic_light():
          my_van.wait()
          while True:
            my_van.at_green_traffic_light()
            break
       
    
       

movement.auto_move()
