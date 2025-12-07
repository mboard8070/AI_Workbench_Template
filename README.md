# AI_Workbench_Template
This is a generalized template for AI projects using the DGX workflow
#########

# Universal AI Workbench Template (2025)

One repo → infinite AI projects on DGX Spark / B200 / H100.

## 5-minute start

```bash
git clone https://github.com/mboard8070/AI_Workbench_Template.git my-new-project
cd my-new-project

# Edit only this file
nano config/project.yaml          # ← change name, model, data paths, etc.

# Import into Workbench
nvwb projects import .

# Launch
# → Click JupyterLab or VS Code in the Workbench GUI

