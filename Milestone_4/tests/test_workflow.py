from orchestrator.workflow_manager import WorkflowManager


def test():

    manager = WorkflowManager()

    result = manager.run_workflow("AI")

    assert result["metrics"]["workflow_status"] == "Completed"

    print("Workflow Test Passed")


test()
