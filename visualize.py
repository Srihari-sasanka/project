import pygraphviz as pgv

def build_and_visualize_graph():
    G = pgv.AGraph(directed=True)

    # Add nodes
    G.add_node("Start", label="Start")
    G.add_node("SkillMatch", label="Skill Match Agent")
    G.add_node("ModeCheck", label="Mode & Availability Check Agent")
    G.add_node("LocationCheck", label="Location Filter Agent")
    G.add_node("RatingSelect", label="Rating Selection Agent")
    G.add_node("AssignTechnician", label="Assign Technician")
    G.add_node("End", label="End")

    # Add flow edges
    G.add_edge("Start", "SkillMatch")
    G.add_edge("SkillMatch", "ModeCheck")
    G.add_edge("ModeCheck", "LocationCheck", label="if mode == 'onsite'")
    G.add_edge("ModeCheck", "RatingSelect", label="if mode == 'remote'")
    G.add_edge("LocationCheck", "RatingSelect")
    G.add_edge("RatingSelect", "AssignTechnician")
    G.add_edge("AssignTechnician", "End")

    # Visualize and save
    G.layout(prog="dot")
    G.draw("technician_agent_workflow.png")
    print("✅ Graph saved as technician_agent_workflow.png")

if __name__ == "__main__":
    build_and_visualize_graph()
