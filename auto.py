import subprocess
import shutil
import os


results_dir = "./allure-results"
report_dir = "./allure-report"


if os.path.exists(results_dir):
  shutil.rmtree(results_dir)
if os.path.exists(report_dir):
  shutil.rmtree(report_dir)


# Pytest 実行
subprocess.run(["pytest", "--alluredir", results_dir])

# Allure レポート生成
subprocess.run(["allure", "generate", results_dir, "--clean", "-o", report_dir])

# ブラウザで表示
subprocess.run(["allure", "open", report_dir])