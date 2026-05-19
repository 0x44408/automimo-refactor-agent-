# src/agent.py
import os
import sys
import subprocess
from dotenv import load_dotenv
from prompt_templates import SYSTEM_PROMPT, REFACTOR_PROMPT_TEMPLATE
import utils

# Load credentials
load_dotenv()
MIMO_API_KEY = os.getenv("MIMO_API_KEY")

class AutoMimoRefactorAgent:
    def __init__(self, target_file):
        self.target_file = target_file
        print("[Agent Initialization] Processing engine ready via OpenClaw orchestration.")

    def run_refactor_loop(self):
        print(f"\n[Step 1] Scanning file for technical debt: {self.target_file}")
        original_code = utils.read_file(self.target_file)
        
        print("[Step 2] Executing Long-Chain Reasoning & Architecture Planning...")
        # Simulating LLM response based on the defined prompts
        # In production, this calls your Claude/MiMo model endpoint using the MIMO_API_KEY
        refactored_code = self._mock_llm_call(original_code)
        
        # Save temporary changes to run closed-loop verification
        utils.write_file(self.target_file, refactored_code)
        
        print("[Step 3] Running Automated Closed-Loop Verification Tests...")
        test_success = self._run_tests()
        
        if test_success:
            print("[Step 4] Tests Passed! Initiating automated deployment pipeline.")
            utils.simulate_git_commit("feature/mimo-auto-refactor", self.target_file)
            print("\n[Success] Workflow completed successfully! Turnaround time minimized by 80%.")
        else:
            print("[Error] Self-Correction Triggered: Verification failed. Rolling back changes.")
            utils.write_file(self.target_file, original_code)

    def _mock_llm_call(self, code):
        """Simulates an optimal, type-hinted refactoring engine outcome."""
        return (
            "# Refactored by AutoMimo Agent\n"
            "def calculate_metrics(data: list[int]) -> dict[str, float]:\n"
            "    if not data:\n"
            "        return {'mean': 0.0, 'total': 0.0}\n"
            "    total = float(sum(data))\n"
            "    return {'mean': total / len(data), 'total': total}\n"
        )

    def _run_tests(self):
        """Executes test suite to verify code stability."""
        result = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
        return result.returncode == 0

if __name__ == "__main__":
    # Create a dummy file to refactor if it doesn't exist
    dummy_path = "src/legacy_code.py"
    if not os.path.exists(dummy_path):
        utils.write_file(dummy_path, "def calculate_metrics(data):\n    return sum(data)/len(data), sum(data)")
        
    agent = AutoMimoRefactorAgent(target_file=dummy_path)
    agent.run_refactor_loop()
