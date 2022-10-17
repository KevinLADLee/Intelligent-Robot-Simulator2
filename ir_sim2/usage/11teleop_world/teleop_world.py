from ir_sim2.env import EnvBase
import numpy as np
import matplotlib.pyplot as plt

env = EnvBase(world_name = 'teleop_world.yaml', control_mode='keyboard')
# env = EnvBase(world_name = 'teleop_world_car.yaml', control_mode='keyboard')

for i in range(3000):

    env.step(env.key_vel, vel_id=env.key_id)
    env.render(show_traj=True)

    if env.done(): 
        print('done')
        break
    
    env.reset(env.done_list(), 'any')  # 'all'; 'any'

print('TIME DONE')
env.end(show_text=True)