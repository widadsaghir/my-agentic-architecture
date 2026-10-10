import os
import argparse
from crewai import Agent, Task, Crew, Process

def run_architecture_platform():
    parser = argparse.ArgumentParser(description="Multi-Agent Architecture Platform (AAP)")
    parser.add_argument("--language", type=str, default="English", help="Target language for output (e.g. English, French)")
    parser.add_argument("--input", type=str, required=True, help="Raw framing notes or project request")
    args = parser.parse_args()

    print(f"Initializing Multi-Agent Architecture Platform in [{args.language}]...")
    print(f"Input Request: {args.input}")

    # Define Agent Manager (Orchestrator)
    manager = Agent(
        role='Lead Enterprise Architecture Manager',
        goal='Orchestrate the multi-agent dream team to produce comprehensive TOGAF/SAFe compliant architecture deliverables.',
        backstory='Experienced Enterprise Architect leading end-to-end IT transformations and multi-agent systems.',
        verbose=True
    )

    # Define Solution Architect Agent
    solution_architect = Agent(
        role='Solution & Infrastructure Architect',
        goal='Design robust, agnostic technical architectures (Cloud, Hybrid, or On-Premise).',
        backstory='Expert in resilient systems design, well-architected frameworks, and infrastructure patterns.',
        verbose=True
    )

    # Define Task
    design_task = Task(
        description=f"Analyze the following request: '{args.input}'. Propose a preliminary technical architecture approach in {args.language}.",
        expected_output="A structured technical architecture outline containing infrastructure choices and rationale.",
        agent=solution_architect
    )

    # Crew Setup
    crew = Crew(
        agents=[solution_architect],
        tasks=[design_task],
        process=Process.sequential,
        manager_agent=manager,
        verbose=True
    )

    result = crew.kickoff()
    print("\n=== EXECUTION RESULT ===")
    print(result)

if __name__ == "__main__":
    run_architecture_platform()
