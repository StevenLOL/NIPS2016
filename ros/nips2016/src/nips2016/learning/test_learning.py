
from environment_explauto.environment import TestEnvironment
from learning import Learning

        
if __name__ == "__main__":
    
    print "Create environment"
    environment = TestEnvironment()
    
    print "Create agent"
    learning = Learning(environment)
    learning.start()
    
    print
    print "Do 500 autonomous steps:" 
    for i in range(500):
        context = environment.get_current_context()
        m = learning.produce(context)
        s = environment.update(m)
        learning.perceive(s)
        
#     print "Do 1 arm demonstration"
#     m_demo_traj = np.zeros((25, 4)) + 0.001
#     m_demo = environment.torsodemo2m(m_demo_traj)
#     s = environment.update(m_demo)
#     learning.perceive(s, m_demo=m_demo)
    
    print
    print "Do 1 joystick demonstration to show how to produce light"
    j_demo = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.2, 0.001, 0., 0., 0., 0., 0.]
    s = environment.get_current_context() + j_demo + [0.]*20 + [0.2]*20 + [0.2]*20 + [0.1]*10 + [0.]*10
    #print "j_demo", s
    learning.perceive(s, j_demo=True)
    
    print "Now ask to produce light..."
    learning.produce(environment.get_current_context(), "s_light")
    
    
    
    print
    print "Saving current data to file"
    learning.save("../../../../../data", "test")
    
#     print "Data before saving"
#     print learning.agent.t
#     print learning.agent.interests_evolution["mod1"][-10:]
#     print learning.agent.progresses_evolution["mod1"][-10:]
#     print learning.agent.chosen_modules[-10:]
#     print len(learning.agent.modules["mod1"].sensorimotor_model.model.imodel.fmodel.dataset)
#     print len(learning.agent.modules["mod2"].sensorimotor_model.model.imodel.fmodel.dataset)
#     print learning.agent.modules["mod1"].interest_model.current_interest
    
    print
    print "Do 500 autonomous steps:" 
    for i in range(500):
        context = environment.get_current_context()
        m = learning.produce(context)
        s = environment.update(m)
        learning.perceive(s)
    
    print "Rebuilding agent from file"
    learning.restart("../../../../../data", "test", 2001)
        
#     print "Data after rebuilding"
#     print learning.agent.t
#     print learning.agent.interests_evolution["mod1"][-10:]
#     print learning.agent.progresses_evolution["mod1"][-10:]
#     print learning.agent.chosen_modules[-10:]
#     print len(learning.agent.modules["mod1"].sensorimotor_model.model.imodel.fmodel.dataset)
#     print len(learning.agent.modules["mod2"].sensorimotor_model.model.imodel.fmodel.dataset)
#     print learning.agent.modules["mod1"].interest_model.current_interest
    
    print
    print "Do 500 autonomous steps:" 
    for i in range(500):
        context = environment.get_current_context()
        m = learning.produce(context)
        s = environment.update(m)
        learning.perceive(s)
        
    print "\nPloting interests..."
    learning.plot()